
from PySide6.QtCore import QCoreApplication

from app.state_manager import (
    StateManager,
    AssistantStatus
)

app = QCoreApplication([])

state = StateManager()

# Listen for status changes
state.status_changed.connect(
    lambda value: print("UI RECEIVED STATUS:", value)
)

# Listen for notifications
state.notification_received.connect(
    lambda message: print("UI RECEIVED NOTIFICATION:", message)
)

print("INITIAL STATUS:", state.get_status())

state.set_status(AssistantStatus.THINKING)
state.notify("NEXUS is working!")

state.set_status(AssistantStatus.READY)

print("TEST COMPLETED SUCCESSFULLY")
