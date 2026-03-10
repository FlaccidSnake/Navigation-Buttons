# -*- coding: utf-8 -*-
"""
Anki Add-on: Browser Navigation Buttons
Adds back/forward navigation buttons for search history.
Copyright: 2026
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""
from aqt.qt import *
from aqt import gui_hooks, mw
from aqt.utils import tooltip

# Search history tracking
search_history = []
history_position = -1
navigating = False  # Flag to prevent history updates during navigation

def get_config():
    """Get addon configuration"""
    config = mw.addonManager.getConfig(__name__)
    if config is None:
        return {"show_back_button": True, "show_forward_button": True}
    return config

def add_navigation_buttons(browser):
    """Add back/forward navigation buttons to the right of search bar"""
    global search_history, history_position
    
    config = get_config()
    
    # Reset history for new browser window
    search_history = []
    history_position = -1
    
    # Hook into the browser's search function to track ALL searches
    original_search = browser.search_for
    
    def wrapped_search(*args, **kwargs):
        # First argument is the search text
        if args:
            on_search_executed(browser, args[0])
        return original_search(*args, **kwargs)
    
    browser.search_for = wrapped_search
    
    # Get the grid layout (same as refresh button approach)
    layout = browser.form.gridLayout
    
    # Create back button
    if config.get("show_back_button", True):
        back_button = QToolButton()
        back_button.setText("◀")
        back_button.setToolTip("Go back in search history (Alt+Left)")
        back_button.setAutoRaise(True)
        back_button.setFixedWidth(30)
        back_button.setFixedHeight(25)
        back_button.setEnabled(False)
        browser._search_back_button = back_button
        
        # Add to grid at row 0, next available column
        layout.addWidget(back_button, 0, layout.columnCount())
    else:
        browser._search_back_button = None
    
    # Create forward button  
    if config.get("show_forward_button", True):
        forward_button = QToolButton()
        forward_button.setText("▶")
        forward_button.setToolTip("Go forward in search history (Alt+Right)")
        forward_button.setAutoRaise(True)
        forward_button.setFixedWidth(30)
        forward_button.setFixedHeight(25)
        forward_button.setEnabled(False)
        browser._search_forward_button = forward_button
        
        # Add to grid at row 0, next available column
        layout.addWidget(forward_button, 0, layout.columnCount())
    else:
        browser._search_forward_button = None
    
    # Connect click handlers
    if browser._search_back_button:
        browser._search_back_button.clicked.connect(
            lambda: navigate_back(browser, browser._search_back_button, browser._search_forward_button)
        )
    
    if browser._search_forward_button:
        browser._search_forward_button.clicked.connect(
            lambda: navigate_forward(browser, browser._search_back_button, browser._search_forward_button)
        )
    
    # Add keyboard shortcuts
    if config.get("show_back_button", True):
        back_shortcut = QShortcut(QKeySequence("Alt+Left"), browser)
        back_shortcut.activated.connect(lambda: navigate_back(browser, browser._search_back_button, browser._search_forward_button))
    
    if config.get("show_forward_button", True):
        forward_shortcut = QShortcut(QKeySequence("Alt+Right"), browser)
        forward_shortcut.activated.connect(lambda: navigate_forward(browser, browser._search_back_button, browser._search_forward_button))

def on_search_executed(browser, search_text):
    """Track when a search is executed"""
    global search_history, history_position, navigating
    
    # Don't track if we're navigating through history
    if navigating:
        return
    
    # Don't add empty searches or duplicates of the last search
    if not search_text.strip():
        return
    
    if search_history and history_position >= 0 and search_history[history_position] == search_text:
        return
    
    # If we're in the middle of history, truncate forward history
    if history_position < len(search_history) - 1:
        search_history = search_history[:history_position + 1]
    
    # Add new search to history
    search_history.append(search_text)
    history_position = len(search_history) - 1
    
    # Update button states
    update_button_states(browser)

def navigate_back(browser, back_button, forward_button):
    """Navigate to previous search in history"""
    global search_history, history_position, navigating
    
    if history_position > 0:
        navigating = True
        history_position -= 1
        search = search_history[history_position]
        
        browser.form.searchEdit.setEditText(search)
        browser.search_for(search)
        
        update_button_states(browser)
        navigating = False

def navigate_forward(browser, back_button, forward_button):
    """Navigate to next search in history"""
    global search_history, history_position, navigating
    
    if history_position < len(search_history) - 1:
        navigating = True
        history_position += 1
        search = search_history[history_position]
        
        browser.form.searchEdit.setEditText(search)
        browser.search_for(search)
        
        update_button_states(browser)
        navigating = False

def update_button_states(browser):
    """Update enabled/disabled state of navigation buttons"""
    global search_history, history_position
    
    # Update back button
    if hasattr(browser, '_search_back_button') and browser._search_back_button:
        browser._search_back_button.setEnabled(history_position > 0)
    
    # Update forward button
    if hasattr(browser, '_search_forward_button') and browser._search_forward_button:
        browser._search_forward_button.setEnabled(history_position < len(search_history) - 1)

# Register the hook to add buttons when browser opens
gui_hooks.browser_will_show.append(add_navigation_buttons)