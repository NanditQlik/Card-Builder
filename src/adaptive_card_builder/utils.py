from typing import List, Optional
import json


def _recursive_render(obj):
    if hasattr(obj, "render") and callable(obj.render):
        return _recursive_render(obj.render())
    elif isinstance(obj, list):
        return [_recursive_render(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: _recursive_render(v) for k, v in obj.items()}
    else:
        return obj


def prettify_json(card, indent: int = 2) -> str:
    rendered = _recursive_render(card)
    return json.dumps(rendered, indent=indent)
    """
    Get the approximate size of a card in terms of elements.
    
    Args:
        card: AdaptiveCard instance
        
    Returns:
        Dictionary with body_count and actions_count
    """
    return {"body_count": len(card.body), "actions_count": len(card.actions)}


def to_dict(card_obj):
    return json.loads(
        json.dumps(
            card_obj,
            default=(
                lambda o: (
                    o.__dict__
                    if hasattr(o, "type") and o.type != "AdaptiveCard"
                    else {}
                )
            ),
        )
    )
