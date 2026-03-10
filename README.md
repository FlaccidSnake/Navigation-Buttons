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

### Keyboard Shortcuts

- **Alt+Left**: Go back in search history
- **Alt+Right**: Go forward in search history

## Technical Notes

- Search history is stored per browser window session
- Closing and reopening the browser resets the history
- The addon uses a global flag to prevent history pollution during navigation
- Buttons are positioned to the left of the search bar using the grid layout

## Changelog

### Version 1.0.1
- Fixed bug where button symbols didn't appear after updating to Anki 25.09.2 

### Version 1.0.0
- Initial release
- Back/forward navigation buttons
- Keyboard shortcuts (Alt+Left/Right)
- Configurable button visibility
- Smart history management