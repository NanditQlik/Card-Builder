"""
Adaptive Card Builder - A Python helper library for generating Adaptive Card JSON components.
"""

from .core import create_card
from .elements import (
    text_block,
    container,
    column_set,
    column,
    image,
    action_set,
    fact_set
)
from .utils import (
    merge_cards, create_simple_card, create_form_card, create_list_card,
    create_fact_card, create_media_card, prettify_json
)

# Import card builders
from .cards import (
    # App Analysis Agent components
    create_aaa_top_bar,
    create_aaa_title,
    create_aaa_chart,
    create_aaa_actions,
    create_aaa_card,
    
    # Generic component builders
    create_top_bar,
    create_title_section,
    create_chart_section,
    create_actions_section
)

__version__ = "0.2.0"
__author__ = "Adaptive Card Builder"

__all__ = [
    # Core
    "create_card",
    
    # Elements
    "text_block",
    "container", 
    "column_set",
    "column",
    "image",
    "action_set",
    "fact_set",
    
    # Utils
    "merge_cards",
    "create_simple_card",
    "create_form_card", 
    "create_list_card",
    "create_fact_card",
    "create_media_card",
    "prettify_json",
    
    # App Analysis Agent Components
    "create_aaa_top_bar",
    "create_aaa_title", 
    "create_aaa_chart",
    "create_aaa_actions",
    "create_aaa_card",
    
    # Generic Components
    "create_top_bar",
    "create_title_section",
    "create_chart_section", 
    "create_actions_section"
] 