
import sys

from PySide6.QtWidgets import QApplication

from app.state_manager import StateManager
from ui.island import NexusIsland
from ui.assistant_window import AssistantWindow


class NexusApplication:

    def __init__(self):

        self.app = QApplication(sys.argv)
        self.app.setApplicationName("NEXUS")

        # Central application state
        self.state_manager = StateManager()

        # Create UI components
        self.assistant = AssistantWindow()
        self.island = NexusIsland()

        # Connect floating island and chat
        self.island.set_assistant(self.assistant)

        # Connect shared state manager
        self.island.set_state_manager(
            self.state_manager
        )

        self.assistant.set_state_manager(
            self.state_manager
        )

        # Start NEXUS
        self.island.show()

        print("================================")
        print("       NEXUS INITIALIZED")
        print("       SYSTEM READY")
        print("================================")

    def run(self):
        return self.app.exec()


if __name__ == "__main__":

    nexus = NexusApplication()
    sys.exit(nexus.run())
