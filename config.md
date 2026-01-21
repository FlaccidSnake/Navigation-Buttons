# Browser Navigation Buttons Configuration

## Settings

### show_back_button

**Type:** Boolean  
**Default:** true

Show or hide the back button (◀) to navigate to previous searches.

- **true**: Back button is visible
- **false**: Back button is hidden

### show_forward_button

**Type:** Boolean  
**Default:** true

Show or hide the forward button (▶) to navigate to next searches.

- **true**: Forward button is visible
- **false**: Forward button is hidden

## Examples

**Both buttons visible (default):**
```json
{
    "show_back_button": true,
    "show_forward_button": true
}
```

**Only back button:**
```json
{
    "show_back_button": true,
    "show_forward_button": false
}
```

**Only forward button:**
```json
{
    "show_back_button": false,
    "show_forward_button": true
}
```

**Hide both buttons (disable addon):**
```json
{
    "show_back_button": false,
    "show_forward_button": false
}
```

## Keyboard Shortcuts

- **Alt+Left**: Go back in search history
- **Alt+Right**: Go forward in search history

Note: Shortcuts work even if buttons are hidden via config.

## How to Change Settings

1. Open Anki
2. Go to **Tools → Add-ons**
3. Select **Browser Navigation Buttons**
4. Click the **Config** button
5. Change `show_back_button` or `show_forward_button` to `true` or `false`
6. Click **OK**
7. **Restart Anki** or reopen the browser for changes to take effect

## Notes

- Search history is tracked per browser window session
- Closing and reopening the browser resets the history
- The buttons are disabled (grayed out) when you can't go back/forward
- Executing a new search while in the middle of history will erase forward history (like a web browser)