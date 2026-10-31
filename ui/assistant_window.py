
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QFrame,
    QSizePolicy,
)


class AssistantWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEXUS Assistant")
        self.resize(650, 720)

        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setStyleSheet("""
            QWidget {
                background-color: #0D1220;
                color: white;
                font-family: Segoe UI;
            }

            QLineEdit {
                background-color: #171F32;
                border: 1px solid #344563;
                border-radius: 15px;
                padding: 14px;
                color: white;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #00D9FF;
            }

            QPushButton {
                background-color: #087FAD;
                color: white;
                border: none;
                border-radius: 13px;
                padding: 12px 20px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #079FCB;
            }

            QScrollArea {
                border: none;
                background: transparent;
            }
        """)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(22, 20, 22, 20)
        self.main_layout.setSpacing(15)

        # Header
        header = QHBoxLayout()

        title = QLabel("NEXUS")
        title.setStyleSheet("""
            font-size: 23px;
            font-weight: bold;
            letter-spacing: 4px;
            color: #EAF7FF;
        """)

        subtitle = QLabel("AI DESKTOP ASSISTANT")
        subtitle.setStyleSheet("""
            color: #7D91B5;
            font-size: 10px;
            letter-spacing: 2px;
        """)

        header_text = QVBoxLayout()
        header_text.addWidget(title)
        header_text.addWidget(subtitle)

        self.connection_status = QLabel("● UI MODE")
        self.connection_status.setStyleSheet(
            "color: #00E5B0; font-size: 10px;"
        )

        header.addLayout(header_text)
        header.addStretch()
        header.addWidget(self.connection_status)

        self.main_layout.addLayout(header)

        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet(
            "color: #26334D; background: #26334D; max-height: 1px;"
        )
        self.main_layout.addWidget(divider)

        # Scrollable chat area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )
        self.chat_layout.setSpacing(14)

        self.scroll.setWidget(self.chat_container)
        self.main_layout.addWidget(self.scroll, 1)

        # Welcome message
        self.add_message(
            "NEXUS",
            "Hello! I'm NEXUS. My interface is ready. "
            "My AI brain will be connected in a later milestone.",
            False
        )

        # Input section
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText(
            "Message NEXUS..."
        )
        self.message_input.returnPressed.connect(
            self.send_message
        )

        send_button = QPushButton("SEND")
        send_button.clicked.connect(self.send_message)

        input_layout.addWidget(self.message_input, 1)
        input_layout.addWidget(send_button)

        self.main_layout.addLayout(input_layout)

        footer = QLabel(
            "NEXUS DEVELOPMENT BUILD  •  AI NOT CONNECTED"
        )
        footer.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        footer.setStyleSheet(
            "color: #65748F; font-size: 9px; letter-spacing: 1px;"
        )

        self.main_layout.addWidget(footer)

    def add_message(self, sender, message, is_user):

        bubble = QFrame()
        bubble.setMaximumWidth(450)
        bubble.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Minimum
        )

        if is_user:
            bubble.setStyleSheet("""
                QFrame {
                    background-color: #123B59;
                    border: 1px solid #17618B;
                    border-radius: 15px;
                }
            """)
        else:
            bubble.setStyleSheet("""
                QFrame {
                    background-color: #19243A;
                    border: 1px solid #2B3B59;
                    border-radius: 15px;
                }
            """)

        bubble_layout = QVBoxLayout(bubble)
        bubble_layout.setContentsMargins(14, 10, 14, 10)
        bubble_layout.setSpacing(5)

        sender_label = QLabel(sender)
        sender_label.setStyleSheet("""
            color: #00D9FF;
            font-size: 10px;
            font-weight: bold;
            background: transparent;
            border: none;
        """)

        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        message_label.setStyleSheet("""
            color: #EDF4FF;
            font-size: 13px;
            background: transparent;
            border: none;
        """)

        bubble_layout.addWidget(sender_label)
        bubble_layout.addWidget(message_label)

        row = QHBoxLayout()

        if is_user:
            row.addStretch()
            row.addWidget(bubble)
        else:
            row.addWidget(bubble)
            row.addStretch()

        self.chat_layout.addLayout(row)

        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )

    def send_message(self):

        message = self.message_input.text().strip()

        if not message:
            return

        self.add_message("YOU", message, True)
        self.message_input.clear()

        # Temporary response: real AI comes in M3.
        self.add_message(
            "NEXUS",
            "I received your message! My AI engine "
            "is not connected yet. We'll activate it "
            "when we reach M3.",
            False
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = AssistantWindow()
    window.show()

    sys.exit(app.exec())
