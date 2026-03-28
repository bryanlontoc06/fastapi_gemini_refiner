from abc import abstractmethod


class AIPlatform:
    @abstractmethod
    def refine(self, message: str) -> str:
        """Refine the input message and return the refined version."""
        pass
