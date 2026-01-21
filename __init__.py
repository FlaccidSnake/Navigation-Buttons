# -*- coding: utf-8 -*-
"""
Anki Add-on: Browser Navigation Buttons
Adds back/forward navigation buttons for search history.
Copyright: 2026
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""

from . import browser_navigation
from .config_dialog import show_config_dialog
from aqt import mw

# Register config action
mw.addonManager.setConfigAction(__name__, show_config_dialog)