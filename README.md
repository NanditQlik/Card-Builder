# Adaptive Card Builder

A Python library for generating [Adaptive Card](https://adaptivecards.io/) JSON components, supporting both class-based and functional APIs. Build complex cards for Microsoft Teams, Qlik, and other platforms with reusable, composable Python functions and classes.

## Features

- **Class-based API**: Use the `AAACards` class to build App Analysis Agent cards and components.
- **Functional API**: Create Adaptive Card elements (TextBlock, Container, ColumnSet, etc.) with simple functions.
- **Qlik/Teams Extensions**: Includes helpers for Qlik charts, skeletons, tags, and advanced actions.
- **No external dependencies**: Only requires `msteamsadaptivecardbuilder` (see requirements).
- **Easy JSON export**: Utilities to prettify and convert cards to JSON.

## Project Structure

```
Card-Builder/
├── src/
│   └── adaptive_card_builder/
│       ├── __init__.py
│       ├── elements.py
│       ├── utils.py
│       └── cards/
│           ├── __init__.py
│           └── aaa_cards.py
├── examples/
│   └── aaa_cards_example.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

### Class-based API: `AAACards`

```python
from adaptive_card_builder import AAACards, prettify_json

aaa = AAACards()

# Create a top bar component
bar = aaa.create_top_bar("Performance", "Total Sales")
print(prettify_json(bar))

# Create a chart section
chart = aaa.create_chart({"chartType": "barchart"}, [{"chartType": "linechart"}])
print(prettify_json(chart))

# Create buttons for a card
buttons = aaa.create_buttons(
    add_to_sheet=True,
    sheet_list_actions=[
        {"title": "Sheet 1", "sheetId": "1", "iconUrl": "AddOutline"},
        {"title": "Sheet 2", "sheetId": "2", "iconUrl": "AddOutline"},
    ],
    is_narrative_set=False,
    card={},
)
print(prettify_json(buttons))
```

### Functional API: Element Functions

```python
from adaptive_card_builder import text_block, container, column_set, column, image, action_set, fact_set

card_body = [
    text_block("Hello, World!", size="Large"),
    container([
        text_block("This is inside a container.")
    ]),
    column_set([
        column([text_block("Left")]),
        column([text_block("Right")]),
    ]),
]
```

## Example

See [`examples/aaa_cards_example.py`](examples/aaa_cards_example.py) for a full async example using the `AAACards` class.

## API Overview

### Class: `AAACards`
- `create_skeleton()` – Qlik skeleton loading section
- `create_top_bar(analysisType, title)` – Top bar for analysis cards
- `create_chart(chart, alternative_chart_types, title=None, **kwargs)` – Chart section
- `menuList(sheetData)` – Generate menu dropdown actions
- `create_buttons(add_to_sheet, sheet_list_actions, is_narrative_set, card)` – Button sets for cards

### Element Functions
- `text_block(text, **kwargs)`
- `container(items, **kwargs)`
- `column_set(columns, **kwargs)`
- `column(items, width=None, **kwargs)`
- `image(url, **kwargs)`
- `action_set(actions, **kwargs)`
- `fact_set(facts, **kwargs)`
- Input elements: `input_text`, `input_number`, `input_date`, `input_time`, `input_toggle`, `input_choice_set`
- Qlik/Teams: `qlik_chart`, `qlik_skeleton`, `qlik_tag`, `action_show_modal`, `action_toggle_visibility`, `action_menu_dropdown`, `action_execute`
- Utilities: `prettify_json(card)`, `to_dict(card_obj)`

## Requirements

- Python 3.7+
- `msteamsadaptivecardbuilder` (see `requirements.txt`)

---

*For more details, see the code and examples in this repository.* 