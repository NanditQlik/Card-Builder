"""
Adaptive Card Builder - A Python helper library for generating Adaptive Card JSON components.
"""

from .elements import (
    text_block,
    container,
    column_set,
    column,
    image,
    action_set,
    fact_set,
)
from .utils import prettify_json

# Import card builders
from .cards import AAACards

__version__ = "0.2.0"
__author__ = "Adaptive Card Builder"

__all__ = [
    # Elements
    "text_block",
    "container",
    "column_set",
    "column",
    "image",
    "action_set",
    "fact_set",
    # Utils
    "prettify_json",
    # Card Classes
    "AAACards",
]
