"""
Core functionality for Adaptive Card generation using the msteamsadaptivecardbuilder library.
"""

from msteamsadaptivecardbuilder import AdaptiveCard
from typing import List, Optional, Any

async def create_card(
    body: Optional[List[Any]] = None,
    actions: Optional[List[Any]] = None,
    version: str = "1.2",
    **kwargs
) -> AdaptiveCard:
    """
    Create an Adaptive Card with the specified elements using the AdaptiveCard class.
    Args:
        body: List of card body elements (msteamsadaptivecardbuilder elements)
        actions: List of card actions (msteamsadaptivecardbuilder actions)
        version: Adaptive Card schema version
        **kwargs: Additional properties to include in the card
    Returns:
        AdaptiveCard instance
    """
    card = AdaptiveCard(version=version, **kwargs)
    if body:
        for item in body:
            card.add(item)
    if actions:
        for action in actions:
            card.add(action)
    return card

# Validation can be custom or omitted, as msteamsadaptivecardbuilder may not have a validate method.
def validate_card(card: AdaptiveCard) -> bool:
    try:
        # Basic check for body attribute
        return hasattr(card, 'body')
    except Exception:
        return False 