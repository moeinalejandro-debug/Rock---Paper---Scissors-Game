# Rock, Paper, Scissors

A command-line Rock, Paper, Scissors game built with Python.

## Features

- Play against the computer
- Random computer choices
- Score tracking
- 10 points for each win
- Colored terminal output
- Player name input
- Shortcuts for moves (`r`, `p`, `s`)
- Replay support
- Final score summary
- Input validation
- Keyboard interruption handling

## Requirements

- Python 3.x

No external libraries are required.

## Installation

Clone the repository:

```bash
git clone <https://github.com/moeinalejandro-debug/Rock---Paper---Scissors-Game>
```

Navigate to the project directory:

```bash
cd <YOUR_PROJECT_DIRECTORY>
```

Run the game:

```bash
python main.py
```

## How to Play

Enter your name and choose one of the available moves.

| Input | Action |
|---|---|
| `rock` or `r` | Rock |
| `paper` or `p` | Paper |
| `scissors` or `s` | Scissors |
| `quit` | Exit and display final results |

After each round, choose whether to continue playing, exit, or display the final results.

## Scoring

| Result | Points |
|---|---:|
| Win | 10 |
| Loss | 0 for the player; 10 for the computer |
| Tie | No points |

## Technologies

- Python
- `random`
- `time`
- ANSI escape codes

## Project Structure

```text
rock-paper-scissors/
├── test.py
└── README.md
```

## Concepts Used

- Functions
- Lists, dictionaries, and sets
- Loops and conditional statements
- User input and validation
- Random selection
- String manipulation
- Formatted strings
- Exception handling
- Main-module execution

## Future Improvements

- Best-of-3 and Best-of-5 modes
- Custom winning score
- Match statistics
- Persistent scores using JSON
- Difficulty levels
- Unit tests
- Graphical user interface

## License

No license has been specified yet.
