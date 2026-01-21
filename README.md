# Browser Navigation Buttons

An Anki addon that adds back (◀) and forward (▶) navigation buttons to the browser, allowing you to navigate through your search history like a web browser.

## Features

- **Back Button (◀)**: Navigate to your previous search
- **Forward Button (▶)**: Navigate to your next search (after going back)
- **Smart History Management**: Works just like browser navigation
  - Going back and then executing a new search erases forward history
  - Buttons are disabled when there's nowhere to go
- **Keyboard Shortcuts**: 
  - Alt+Left to go back
  - Alt+Right to go forward
- **Configurable**: Toggle each button on/off independently

## Use Case
I got tired of searching for something, then clicking on a tag, then having to manually find my way back to where I was, or opening the history drop-down (which won't show where you were if you didn't actively search anything and were instead clicking through the sidebar). This makes the browser finally act like a web browser.

### Navigation Buttons

The buttons appear to the left of the search bar:

- Click **◀** to go to the previous search
- Click **▶** to go to the next search (after going back)
- Buttons are grayed out when you can't navigate in that direction

### Keyboard Shortcuts

- **Alt+Left**: Go back in search history
- **Alt+Right**: Go forward in search history

### How Search History Works

The addon tracks your search history just like a web browser:

1. Each time you execute a search (press Enter), it's added to history
2. Click ◀ to go back to previous searches
3. Click ▶ to return to where you were
4. If you go back and execute a new search, all forward history is erased

**Example:**
1. Search for "tag:hard" → History: [tag:hard]
2. Search for "deck:Spanish" → History: [tag:hard, deck:Spanish]
3. Click ◀ (back) → Now viewing "tag:hard"
4. Click ▶ (forward) → Back to "deck:Spanish"
5. Click ◀ then search "is:due" → History: [tag:hard, is:due]

## Technical Notes

- Search history is stored per browser window session
- Closing and reopening the browser resets the history
- The addon uses a global flag to prevent history pollution during navigation
- Buttons are positioned to the left of the search bar using the grid layout

## Changelog

### Version 1.0.0
- Initial release
- Back/forward navigation buttons
- Keyboard shortcuts (Alt+Left/Right)
- Configurable button visibility
- Smart history management