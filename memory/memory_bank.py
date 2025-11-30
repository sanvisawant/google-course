from typing import Dict, List

class SimpleMemoryBank:
    """Long-term memory (very simple). Stores short facts per user."""
    def __init__(self):
        self.memories: Dict[str, List[str]] = {}

    def remember(self, user_id: str, fact: str) -> None:
        self.memories.setdefault(user_id, []).append(fact)

    def retrieve(self, user_id: str):
        return self.memories.get(user_id, [])

    def clear(self, user_id: str) -> None:
        self.memories[user_id] = []
