# Adaptive Card Builder

A Python helper library for generating Adaptive Card JSON components. This library provides reusable functions to create various Adaptive Card elements like TextBlock, Container, Chart, and more. Now powered by the official [`adaptivecards`](https://pypi.org/project/adaptivecards/) library for full schema compatibility.

## Features

- Generate Adaptive Card JSON components using official Adaptive Cards Python classes
- Uses the [`adaptivecards`](https://pypi.org/project/adaptivecards/) library for schema compatibility
- Support for common Adaptive Card elements:
  - TextBlock
  - Container
  - ColumnSet and Column
  - Image
  - ActionSet
  - Input elements
  - And more...

## Project Structure

```
Card-Builder/
├── src/
│   └── adaptive_card_builder/
│       ├── __init__.py
│       ├── core.py
│       ├── elements.py
│       └── utils.py
├── examples/
│   └── basic_usage.py
├── requirements.txt
├── setup.py
└── README.md
```

## Usage

```python
from adaptive_card_builder import create_card, text_block
from adaptivecards.actions import Submit

# Create a simple card
card = create_card(
    body=[
        text_block("Hello, World!", size="Large"),
        text_block("This is a container with some content.")
    ],
    actions=[
        Submit(title="Submit")
    ]
)

# Get the JSON representation
print(card)
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## License

MIT License 