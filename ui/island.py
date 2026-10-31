
from PySide6.QtCore import (
    Qt,
    QTimer,
    QPropertyAnimation,
    QEasingCurve,
    QRect,
)
from PySide6.QtGui import (
    QColor,
    QPainter,
    QLinearGradient,
    QPen,
)
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QGraphicsDropShadowEffect,
)


class NexusIsland(QWidget):

    def __init__(self):
        super().__init__()

        # Window dimensions
        self.compact_width = 270
        self.compact_height = 72

        self.expanded_width = 410
        self.expanded_height = 265

        self.expanded = False
        self.assistant = None

        self.dragging = False
        self.drag_offset = None
        self.press_position = None

        # Window configuration
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.resize(
            self.compact_width,
            self.compact_height
        )

        # Outer glow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(32)
        shadow.setColor(QColor(0, 190, 255, 100))
        shadow.setOffset(0, 0)

        self.setGraphicsEffect(shadow)

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            22, 15, 22, 15
        )
        self.main_layout.setSpacing(17)

        # Top section
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(11)

        self.status = QLabel("●")
        self.status.setStyleSheet("""
            color: #00F5C8;
            font-size: 15px;
            background: transparent;
            border: none;
        """)

        self.title = QLabel("NEXUS")
        self.title.setStyleSheet("""
            color: white;
            font-size: 17px;
            font-weight: bold;
            letter-spacing: 3px;
            background: transparent;
            border: none;
        """)

        self.activity = QLabel("SYSTEM READY")
        self.activity.setStyleSheet("""
            color: #9BA9C5;
            font-size: 9px;
            letter-spacing: 1px;
            background: transparent;
            border: none;
        """)

        self.top_layout.addWidget(self.status)
        self.top_layout.addWidget(self.title)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.activity)

        self.main_layout.addLayout(self.top_layout)

        # Expanded panel
        self.panel = QWidget()

        self.panel.setStyleSheet("""
            QWidget {
                background: transparent;
                border: none;
            }
        """)

        self.panel_layout = QVBoxLayout(self.panel)
        self.panel_layout.setContentsMargins(3, 3, 3, 3)
        self.panel_layout.setSpacing(12)

        self.welcome = QLabel("Hello, I'm NEXUS.")

        self.welcome.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
            background: transparent;
            border: none;
        """)

        self.description = QLabel(
            "Your personal AI desktop assistant."
        )

        self.description.setStyleSheet("""
            color: #A7B2C9;
            font-size: 12px;
            background: transparent;
            border: none;
        """)

        # Open chat button
        self.chat_button = QPushButton("OPEN AI CHAT")

        self.chat_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.chat_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #087FAD;
                border: 1px solid #168DBD;
                border-radius: 12px;
                padding: 12px;
                font-weight: bold;
                letter-spacing: 1px;
            }

            QPushButton:hover {
                background-color: #079FCB;
            }

            QPushButton:pressed {
                background-color: #075D82;
            }
        """)

        self.chat_button.clicked.connect(
            self.open_assistant
        )

        self.footer = QLabel(
            "LOCAL AI  •  WINDOWS ASSISTANT  •  V1.0"
        )

        self.footer.setStyleSheet("""
            color: #65748F;
            font-size: 9px;
            letter-spacing: 1px;
            background: transparent;
            border: none;
        """)

        self.panel_layout.addWidget(self.welcome)
        self.panel_layout.addWidget(self.description)
        self.panel_layout.addSpacing(8)
        self.panel_layout.addWidget(self.chat_button)
        self.panel_layout.addStretch()
        self.panel_layout.addWidget(self.footer)

        self.main_layout.addWidget(self.panel)

        self.panel.hide()

        # Resize animation
        self.animation = QPropertyAnimation(
            self, b"geometry", self
        )

        self.animation.setDuration(350)

        self.animation.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

        # Status pulse
        self.pulse_on = True

        self.pulse_timer = QTimer(self)

        self.pulse_timer.timeout.connect(
            self.animate_status
        )

        self.pulse_timer.start(750)

        # Initial position
        screen = self.screen()
        screen_geometry = screen.availableGeometry()

        x = (
            screen_geometry.x()
            + (
                screen_geometry.width()
                - self.compact_width
            ) // 2
        )

        y = screen_geometry.y() + 15

        self.move(x, y)

    # Connect assistant window
    def set_assistant(self, assistant):
        self.assistant = assistant

    # Open assistant chat
    def open_assistant(self):

        if self.assistant is None:
            print("NEXUS: Assistant window is not connected.")
            return

        self.assistant.show()
        self.assistant.raise_()
        self.assistant.activateWindow()

    # Status animation
    def animate_status(self):

        self.pulse_on = not self.pulse_on

        color = (
            "#00F5C8"
            if self.pulse_on
            else "#087F83"
        )

        self.status.setStyleSheet(f"""
            color: {color};
            font-size: 15px;
            background: transparent;
            border: none;
        """)

    # Expand and collapse
    def toggle_expansion(self):

        current = self.geometry()

        if not self.expanded:

            width = self.expanded_width
            height = self.expanded_height

            self.panel.show()
            self.activity.setText("ASSISTANT ACTIVE")

        else:

            width = self.compact_width
            height = self.compact_height

            self.panel.hide()
            self.activity.setText("SYSTEM READY")

        self.expanded = not self.expanded

        x = current.center().x() - width // 2
        y = current.y()

        target = QRect(
            x, y, width, height
        )

        self.animation.stop()

        self.animation.setStartValue(current)
        self.animation.setEndValue(target)

        self.animation.start()

    # Background drawing
    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        rect = self.rect().adjusted(
            2, 2, -2, -2
        )

        gradient = QLinearGradient(
            0, 0, self.width(), self.height()
        )

        gradient.setColorAt(
            0, QColor(18, 23, 40, 245)
        )

        gradient.setColorAt(
            0.5, QColor(13, 18, 34, 250)
        )

        gradient.setColorAt(
            1, QColor(25, 20, 48, 245)
        )

        painter.setBrush(gradient)

        painter.setPen(
            QPen(QColor(105, 145, 205, 100), 1)
        )

        painter.drawRoundedRect(
            rect, 34, 34
        )

        highlight = QLinearGradient(
            0, 0, self.width(), 0
        )

        highlight.setColorAt(
            0, QColor(0, 220, 255, 35)
        )

        highlight.setColorAt(
            0.5, QColor(130, 100, 255, 10)
        )

        highlight.setColorAt(
            1, QColor(170, 90, 255, 35)
        )

        painter.setBrush(
            Qt.BrushStyle.NoBrush
        )

        painter.setPen(
            QPen(highlight, 1.2)
        )

        painter.drawRoundedRect(
            rect.adjusted(1, 1, -1, -1),
            33, 33
        )

    # Mouse press
    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:

            self.dragging = False

            self.drag_offset = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

            self.press_position = (
                event.globalPosition().toPoint()
            )

    # Mouse movement
    def mouseMoveEvent(self, event):

        if (
            event.buttons()
            & Qt.MouseButton.LeftButton
            and self.drag_offset is not None
        ):

            current = event.globalPosition().toPoint()

            distance = (
                current - self.press_position
            ).manhattanLength()

            if distance > 6:

                self.dragging = True

                self.animation.stop()

                self.move(
                    current - self.drag_offset
                )

    # Mouse release
    def mouseReleaseEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:

            if not self.dragging:
                self.toggle_expansion()

            self.drag_offset = None
            self.press_position = None

    # Keyboard shortcut
    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:
            self.close()
