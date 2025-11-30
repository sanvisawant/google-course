from typing import Dict, List, Any

class InMemorySessionService:
    """Store short-lived session events per user id."""
    def __init__(self):
        self.sessions: Dict[str, List[Dict[str, Any]]] = {}

    def add_event(self, user_id: str, event: Dict[str, Any]) -> None:
        self.sessions.setdefault(user_id, []).append(event)

    def get_events(self, user_id: str):
        return self.sessions.get(user_id, [])

    def clear(self, user_id: str) -> None:
        self.sessions[user_id] = []
