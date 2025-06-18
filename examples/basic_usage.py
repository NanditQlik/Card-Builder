"""
Basic usage examples for the Adaptive Card Builder library (now using the official adaptivecards library).
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from adaptive_card_builder import (
    create_card, text_block, container, column_set, column, image,
    action_set, fact_set
)
from adaptive_card_builder.utils import (
    create_simple_card, create_form_card, create_list_card,
    create_fact_card, create_media_card, prettify_json
)
from adaptivecards.actions import Submit, OpenUrl


def example_simple_card():
    """Example: Create a simple card with text."""
    print("=== Simple Card Example ===")
    
    card = create_card(
        body=[
            text_block("Hello, World!", size="Large", weight="Bolder"),
            text_block("This is a simple Adaptive Card created with Python.", wrap=True)
        ]
    )
    
    print(prettify_json(card))
    print()


def example_card_with_image():
    """Example: Create a card with an image."""
    print("=== Card with Image Example ===")
    
    card = create_card(
        body=[
            text_block("Beautiful Sunset", size="Large", weight="Bolder"),
            image(
                url="https://picsum.photos/400/200",
                alt_text="A beautiful sunset image",
                size="Medium"
            ),
            text_block("This is a beautiful sunset image from Lorem Picsum.", wrap=True)
        ]
    )
    
    print(prettify_json(card))
    print()


def example_card_with_columns():
    """Example: Create a card with columns."""
    print("=== Card with Columns Example ===")
    
    card = create_card(
        body=[
            text_block("Two Column Layout", size="Large", weight="Bolder"),
            column_set([
                column([
                    text_block("Left Column", weight="Bolder"),
                    text_block("This is the left column content.", wrap=True)
                ], width="auto"),
                column([
                    text_block("Right Column", weight="Bolder"),
                    text_block("This is the right column content.", wrap=True)
                ], width="stretch")
            ])
        ]
    )
    
    print(prettify_json(card))
    print()


def example_card_with_facts():
    """Example: Create a card with facts."""
    print("=== Card with Facts Example ===")
    
    card = create_card(
        body=[
            text_block("User Profile", size="Large", weight="Bolder"),
            fact_set([
                {"title": "Name", "value": "John Doe"},
                {"title": "Email", "value": "john.doe@example.com"},
                {"title": "Age", "value": "30"},
                {"title": "Location", "value": "New York, NY"}
            ])
        ]
    )
    
    print(prettify_json(card))
    print()


def example_form_card():
    """Example: Create a form card with inputs."""
    print("=== Form Card Example ===")
    
    from adaptivecards.elements import InputText, InputNumber, InputDate, InputToggle, InputChoiceSet, Choice
    inputs = [
        InputText(id="name", placeholder="Enter your full name"),
        InputText(id="email", placeholder="Enter your email address"),
        InputNumber(id="age", placeholder="Enter your age", min=0, max=120),
        InputDate(id="birthdate", placeholder="Select your birth date"),
        InputToggle(id="newsletter", title="Subscribe to newsletter", value="false"),
        InputChoiceSet(
            id="country",
            choices=[
                Choice(title="United States", value="US"),
                Choice(title="Canada", value="CA"),
                Choice(title="United Kingdom", value="UK")
            ],
            placeholder="Select your country"
        )
    ]
    card = create_form_card(
        title="Registration Form",
        inputs=inputs,
        submit_action_title="Submit",
        cancel_action_title="Cancel"
    )
    
    print(prettify_json(card))
    print()


def example_card_with_actions():
    """Example: Create a card with multiple actions."""
    print("=== Card with Actions Example ===")
    
    card = create_card(
        body=[
            text_block("Action Buttons", size="Large", weight="Bolder"),
            text_block("This card demonstrates different types of actions.", wrap=True)
        ],
        actions=[
            Submit(title="Primary Action"),
            OpenUrl(title="Visit Website", url="https://adaptivecards.io"),
            Submit(title="Secondary Action")
        ]
    )
    
    print(prettify_json(card))
    print()


def example_utility_functions():
    """Example: Using utility functions."""
    print("=== Utility Functions Example ===")
    
    # Simple card
    simple_card = create_simple_card(
        title="Simple Card",
        subtitle="Created with utility function",
        text="This card was created using the create_simple_card utility function.",
        image_url="https://picsum.photos/300/150"
    )
    
    print("Simple Card:")
    print(prettify_json(simple_card))
    print()
    
    # Form card
    from adaptivecards.elements import InputText
    form_inputs = [
        InputText(id="username", placeholder="Username"),
        InputText(id="password", placeholder="Password", is_multiline=False)
    ]
    form_card = create_form_card(
        title="Login Form",
        inputs=form_inputs,
        submit_action_title="Login",
        cancel_action_title="Cancel"
    )
    
    print("Form Card:")
    print(prettify_json(form_card))
    print()
    
    # List card
    list_items = ["First item", "Second item", "Third item"]
    list_card = create_list_card("My List", list_items, show_numbers=True)
    
    print("List Card:")
    print(prettify_json(list_card))
    print()
    
    # Fact card
    facts = [
        {"title": "Status", "value": "Active"},
        {"title": "Last Login", "value": "2023-12-25 10:30 AM"},
        {"title": "Account Type", "value": "Premium"}
    ]
    fact_card = create_fact_card("Account Information", facts)
    
    print("Fact Card:")
    print(prettify_json(fact_card))
    print()
    
    # Media card
    media_card = create_media_card(
        title="Product Showcase",
        subtitle="Latest Product",
        text="Check out our latest product with amazing features!",
        media_url="https://picsum.photos/400/300",
        media_type="image"
    )
    
    print("Media Card:")
    print(prettify_json(media_card))
    print()


def example_complex_card():
    """Example: Create a complex card with multiple elements."""
    print("=== Complex Card Example ===")
    
    card = create_card(
        body=[
            # Header
            text_block("Product Dashboard", size="ExtraLarge", weight="Bolder"),
            text_block("Comprehensive overview of product metrics", size="Medium", is_subtle=True),
            
            # Main content in columns
            column_set([
                column([
                    text_block("Sales", weight="Bolder"),
                    text_block("$125,000", size="Large", color="Good"),
                    text_block("+12% from last month", size="Small", color="Good")
                ], width="auto"),
                column([
                    text_block("Orders", weight="Bolder"),
                    text_block("1,234", size="Large"),
                    text_block("+5% from last month", size="Small", color="Good")
                ], width="auto"),
                column([
                    text_block("Customers", weight="Bolder"),
                    text_block("567", size="Large"),
                    text_block("+8% from last month", size="Small", color="Good")
                ], width="auto")
            ]),
            
            # Divider
            text_block("", wrap=True),
            
            # Facts section
            fact_set([
                {"title": "Top Product", "value": "Widget Pro"},
                {"title": "Best Region", "value": "North America"},
                {"title": "Growth Rate", "value": "15.2%"}
            ]),
            
            # Action buttons
            action_set([
                Submit(title="View Details"),
                OpenUrl(title="Export Report", url="https://example.com/export"),
                Submit(title="Generate Report")
            ])
        ]
    )
    
    print(prettify_json(card))
    print()


if __name__ == "__main__":
    print("Adaptive Card Builder - Basic Usage Examples")
    print("=" * 50)
    print()
    
    # Run all examples
    # example_simple_card()
    # example_card_with_image()
    # example_card_with_columns()
    # example_card_with_facts()
    # example_form_card()
    # example_card_with_actions()
    # example_utility_functions()
    # example_complex_card()
    
    print("All examples completed!") 