
from enum import Enum

from PySide6.QtCore import QObject, Signal


class AssistantStatus(Enum):
    READY = "SYSTEM READY"
    THINKING = "THINKING..."
    RESPONDING = "RESPONDING..."
    OFFLINE = "OFFLINE"
    ERROR = "ERROR"


class StateManager(QObject):

    status_changed = Signal(str)
    notification_received = Signal(str)

    def __init__(self):
        super().__init__()
        self._status = AssistantStatus.READY

    @property
    def status(self):
        return self._status

    def set_status(self, new_status):

        if not isinstance(new_status, AssistantStatus):
            raise ValueError("Invalid assistant status")

        if self._status == new_status:
            return

        self._status = new_status
        self.status_changed.emit(new_status.value)

        print(f"NEXUS STATUS: {new_status.value}")

    def notify(self, message):

        if not isinstance(message, str) or not message.strip():
            return

        self.notification_received.emit(message)
        print(f"NEXUS NOTIFICATION: {message}")

    def get_status(self):
        return self._status.value
