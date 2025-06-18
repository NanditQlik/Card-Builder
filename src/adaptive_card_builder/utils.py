"""
Utility functions for Adaptive Card operations using the official adaptivecards library.
"""

from adaptivecards.adaptivecard import AdaptiveCard
from .elements import text_block, image, fact_set
from adaptivecards.containers import ActionSet
from typing import List, Optional
import json

def merge_cards(*cards: AdaptiveCard) -> AdaptiveCard:
    if not cards:
        raise ValueError("At least one card must be provided")
    merged_card = AdaptiveCard()
    for card in cards:
        if hasattr(card, 'body') and card.body:
            merged_card.body.extend(card.body)
        if hasattr(card, 'actions') and card.actions:
            merged_card.actions.extend(card.actions)
    return merged_card

def create_simple_card(
    title: str,
    subtitle: Optional[str] = None,
    text: Optional[str] = None,
    image_url: Optional[str] = None,
    actions: Optional[List] = None
) -> AdaptiveCard:
    body = [text_block(title, size="Large", weight="Bolder")]
    if subtitle:
        body.append(text_block(subtitle, size="Medium", is_subtle=True))
    if image_url:
        body.append(image(image_url))
    if text:
        body.append(text_block(text, wrap=True))
    card = AdaptiveCard()
    card.body = body
    if actions:
        card.actions = actions
    return card

def create_form_card(
    title: str,
    inputs: List,
    submit_action_title: str = "Submit",
    cancel_action_title: Optional[str] = None
) -> AdaptiveCard:
    from .elements import action_set
    body = [text_block(title, size="Large", weight="Bolder")]
    body.extend(inputs)
    
    actions = [{
        "type": "Action.Submit",
        "title": submit_action_title
    }]
    
    if cancel_action_title:
        actions.append({
            "type": "Action.OpenUrl",
            "title": cancel_action_title,
            "url": "#"
        })
    
    actions_section = action_set(actions)
    card = AdaptiveCard()
    card.body = body
    card.actions = [actions_section]
    return card

def create_list_card(
    title: str,
    items: List[str],
    show_numbers: bool = True
) -> AdaptiveCard:
    body = [text_block(title, size="Large", weight="Bolder")]
    for i, item in enumerate(items, 1):
        prefix = f"{i}. " if show_numbers else "• "
        body.append(text_block(prefix + item, wrap=True))
    card = AdaptiveCard()
    card.body = body
    return card

def create_fact_card(
    title: str,
    facts: List[dict]
) -> AdaptiveCard:
    body = [
        text_block(title, size="Large", weight="Bolder"),
        fact_set(facts)
    ]
    card = AdaptiveCard()
    card.body = body
    return card

def create_media_card(
    title: str,
    subtitle: Optional[str],
    text: Optional[str],
    media_url: str,
    media_type: str = "image"
) -> AdaptiveCard:
    body = [text_block(title, size="Large", weight="Bolder")]
    if subtitle:
        body.append(text_block(subtitle, size="Medium", is_subtle=True))
    if media_type == "image":
        body.append(image(media_url))
    else:
        body.append(text_block(f"Media: {media_url}"))
    if text:
        body.append(text_block(text, wrap=True))
    card = AdaptiveCard()
    card.body = body
    return card

def _recursive_render(obj):
    if hasattr(obj, 'render') and callable(obj.render):
        return _recursive_render(obj.render())
    elif isinstance(obj, list):
        return [_recursive_render(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: _recursive_render(v) for k, v in obj.items()}
    else:
        return obj

def prettify_json(card: AdaptiveCard, indent: int = 2) -> str:
    rendered = _recursive_render(card)
    return json.dumps(rendered, indent=indent)

def validate_element(element: dict) -> bool:
    """
    Basic validation for an Adaptive Card element.
    
    Args:
        element: Element dictionary
        
    Returns:
        True if valid, False otherwise
    """
    try:
        if not isinstance(element, dict):
            return False
        
        if "type" not in element:
            return False
        
        # Basic type validation
        valid_types = {
            "TextBlock", "Container", "ColumnSet", "Column", "Image",
            "ActionSet", "FactSet", "Input.Text", "Input.Number",
            "Input.Date", "Input.Time", "Input.Toggle", "Input.ChoiceSet",
            "Action.Submit", "Action.OpenUrl", "Action.ShowCard"
        }
        
        if element["type"] not in valid_types:
            return False
        
        return True
        
    except Exception:
        return False

def extract_input_values(card: AdaptiveCard) -> dict:
    """
    Extract all input values from a card.
    
    Args:
        card: AdaptiveCard instance
        
    Returns:
        Dictionary of input IDs and their values
    """
    input_values = {}
    
    def extract_from_element(element):
        if isinstance(element, dict):
            if element.get("type", "").startswith("Input.") and "id" in element:
                input_values[element["id"]] = element.get("value")
            
            # Recursively check nested elements
            for value in element.values():
                if isinstance(value, list):
                    for item in value:
                        extract_from_element(item)
                elif isinstance(value, dict):
                    extract_from_element(value)
    
    for element in card.body:
        extract_from_element(element)
    
    return input_values

def get_card_size(card: AdaptiveCard) -> dict:
    """
    Get the approximate size of a card in terms of elements.
    
    Args:
        card: AdaptiveCard instance
        
    Returns:
        Dictionary with body_count and actions_count
    """
    return {
        "body_count": len(card.body),
        "actions_count": len(card.actions)
    } 