import os
import time
from collections import defaultdict
from typing import DefaultDict, List

from fastapi import HTTPException, status

# --- Constants ---
# For authenticated users
raw_auth_limit = os.getenv("AUTH_RATE_LIMIT")
raw_auth_window = os.getenv("AUTH_TIME_WINDOW_SECONDS")
if raw_auth_limit is None or raw_auth_window is None:
    raise ValueError(
        "ERROR: AUTH_RATE_LIMIT or AUTH_TIME_WINDOW_SECONDS is missing in .env file!"
    )
AUTH_RATE_LIMIT = int(raw_auth_limit)
AUTH_TIME_WINDOW_SECONDS = int(raw_auth_window)

# For unauthenticated "global" users
raw_globe_limit = os.getenv("GLOBAL_RATE_LIMIT")
raw_global_window = os.getenv("GLOBAL_TIME_WINDOW_SECONDS")
if raw_globe_limit is None or raw_global_window is None:
    raise ValueError(
        "ERROR: GLOBAL_RATE_LIMIT or GLOBAL_TIME_WINDOW_SECONDS is missing in .env file!"
    )
GLOBAL_RATE_LIMIT = int(raw_globe_limit)
GLOBAL_TIME_WINDOW_SECONDS = int(raw_global_window)

# --- In-memory storage for user requests ---
user_requests: DefaultDict[str, List[float]] = defaultdict(list)


# --- Throttling dependency ---
def apply_rate_limit(user_id: str):
    current_time = time.time()

    if user_id == "global_unauthenticated_user":
        rate_limit = GLOBAL_RATE_LIMIT
        time_window = GLOBAL_TIME_WINDOW_SECONDS
    else:
        rate_limit = AUTH_RATE_LIMIT
        time_window = AUTH_TIME_WINDOW_SECONDS

    # Filter out requests older than the time window
    user_requests[user_id] = [
        t for t in user_requests[user_id] if t > current_time - time_window
    ]

    print(
        f"User {user_id} has made {len(user_requests[user_id]) + 1} requests in the last {time_window} seconds."
    )
    print(f"User Requests: {user_requests}")

    if len(user_requests[user_id]) >= rate_limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please try again later.",
        )
    else:
        # For debugging: print current usage
        current_usage = len(user_requests[user_id])
        print(f"User {user_id}: {current_usage + 1}/{rate_limit} requests used.")

    user_requests[user_id].append(current_time)
    print(f"User Requests: {user_requests}")
    return True
