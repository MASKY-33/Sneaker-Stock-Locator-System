# Sneaker Stock Locator System
This system checks whether a sneaker model exists in the warehouse and returns its storage location.
It uses a dictionary as a small database and a function to handle the lookup.

## Features
- Sneaker models stored in a dictionary
- Function locate_sneaker() handles the search
- Returns the correct shelf location if the model exists
- Returns “Model not in stock” for unknown models
- Handles disk‑related errors (IOError)
- Runs until the user types "stop"

# How to use
Type the sneaker model you are searching for.
Valid model → location shown.
Unknown model → clear message.
Type "stop" to exit.

 
## Learning Purpose
Practice with:
- dictionaries as a simple inventory database
- functions
- input validation
- basic warehouse lookup logic
- clean separation between logic and user interaction
