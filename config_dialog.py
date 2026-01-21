# -*- coding: utf-8 -*-
"""
Browser Navigation Config Dialog
"""
from aqt.qt import *
from aqt import mw
from aqt.utils import tooltip
import random

class BrowserNavigationConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        config = mw.addonManager.getConfig(__name__)
        
        self.show_back_button = config.get("show_back_button", True)
        self.show_forward_button = config.get("show_forward_button", True)
        
        self.setWindowTitle("Browser Navigation Buttons Configuration")
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)
        
        layout = QVBoxLayout()
        
        # Title label
        title_label = QLabel("<h2>Browser Navigation Buttons</h2>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Separator
        separator = self.create_separator()
        layout.addWidget(separator)
        
        # Description
        desc_label = QLabel(
            "Add back (◀) and forward (▶) navigation buttons to the browser\n"
            "to navigate through your search history like a web browser."
        )
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(desc_label)
        
        layout.addSpacing(20)
        
        # Options section
        options_label = QLabel("<b>Button Visibility:</b>")
        layout.addWidget(options_label)
        
        # Back button checkbox
        self.back_button_checkbox = self.create_checkbox(
            "Show back button (◀) - Navigate to previous searches",
            "show_back_button"
        )
        layout.addWidget(self.back_button_checkbox)
        
        # Forward button checkbox
        self.forward_button_checkbox = self.create_checkbox(
            "Show forward button (▶) - Navigate to next searches",
            "show_forward_button"
        )
        layout.addWidget(self.forward_button_checkbox)
        
        layout.addSpacing(10)
        
        # Keyboard shortcuts info
        shortcuts_label = QLabel(
            "<i>Keyboard Shortcuts: Alt+Left (back) | Alt+Right (forward)</i>"
        )
        shortcuts_label.setStyleSheet("color: gray;")
        layout.addWidget(shortcuts_label)
        
        layout.addStretch()
        
        # Separator before buttons
        separator2 = self.create_separator()
        layout.addWidget(separator2)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_config)
        save_button.setFixedWidth(100)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_config)
        cancel_button.setFixedWidth(100)
        
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def create_separator(self):
        """Create a horizontal separator line"""
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("border: 1px solid gray")
        return separator
    
    def create_checkbox(self, label, attribute_name):
        """Create a checkbox with handler"""
        checkbox = QCheckBox(label, self)
        checkbox.setChecked(getattr(self, attribute_name))
        
        def handler(state):
            setattr(self, attribute_name, state == Qt.CheckState.Checked)
        
        checkbox.stateChanged.connect(handler)
        return checkbox
    
    def save_config(self):
        """Save configuration"""
        config = mw.addonManager.getConfig(__name__)
        
        config["show_back_button"] = self.show_back_button
        config["show_forward_button"] = self.show_forward_button
        
        mw.addonManager.writeConfig(__name__, config)
        
        emoticons = [":-)", ":-D", ";-)"]
        selected_emoticon = random.choice(emoticons)
        tooltip(f"Configuration saved {selected_emoticon}<br>Restart Anki or reopen the browser to see changes.")
        
        self.accept()
    
    def cancel_config(self):
        """Cancel configuration changes"""
        emoticons = [":-/", ":-O", ":-|"]
        selected_emoticon = random.choice(emoticons)
        tooltip(f"Canceled {selected_emoticon}")
        
        self.reject()

def show_config_dialog():
    """Show the configuration dialog"""
    dialog = BrowserNavigationConfigDialog(mw)
    dialog.exec()