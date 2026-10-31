
import sys

from PySide6.QtWidgets import QApplication

from ui.island import NexusIsland
from ui.assistant_window import AssistantWindow


class NexusApplication:

    def __init__(self):
        self.app = QApplication(sys.argv)

        # Create assistant chat window
        self.assistant = AssistantWindow()

        # Create floating island
        self.island = NexusIsland()

        # Connect island to assistant
        self.island.set_assistant(self.assistant)

        # Show floating island
        self.island.show()

    def run(self):
        sys.exit(self.app.exec())


if __name__ == "__main__":
    nexus = NexusApplication()
    nexus.run()
