"""
Functions for creating Adaptive Card elements using the msteamsadaptivecardbuilder library.
"""

from msteamsadaptivecardbuilder import (
    TextBlock,
    Image,
    Container,
    ColumnSet,
    Column,
    FactSet,
    Fact,
    ActionSet,
    ActionSubmit,
    ActionOpenUrl,
    ActionShowCard,
)
from typing import List, Dict, Any, Optional, Union


def text_block(text: str, **kwargs) -> TextBlock:
    return TextBlock(text=text, **kwargs)


def container(items: List, **kwargs) -> Container:
    return Container(items=items, **kwargs)


def column_set(columns: List, **kwargs) -> ColumnSet:
    return ColumnSet(columns=columns, **kwargs)


def column(items: List, width: Optional[str] = None, **kwargs) -> Column:
    params = {"items": items}
    if width is not None:
        params["width"] = width
    params.update(kwargs)
    return Column(**params)


def image(url: str, **kwargs) -> Image:
    return Image(url=url, **kwargs)


def fact_set(facts: List[dict], **kwargs) -> FactSet:
    fact_objs = [Fact(title=f["title"], value=f["value"]) for f in facts]
    return FactSet(facts=fact_objs, **kwargs)


def action_set(actions: List, **kwargs) -> ActionSet:
    return ActionSet(actions=actions, **kwargs)


# Input Elements


def input_text(
    id: str,
    placeholder: Optional[str] = None,
    value: Optional[str] = None,
    is_multiline: Optional[bool] = None,
    max_length: Optional[int] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Create an Input.Text element.

    Args:
        id: Unique identifier for the input
        placeholder: Placeholder text
        value: Default value
        is_multiline: Whether the input supports multiple lines
        max_length: Maximum number of characters
        **kwargs: Additional properties

    Returns:
        Input.Text element dictionary
    """
    element = {"type": "Input.Text", "id": id}

    if placeholder:
        element["placeholder"] = placeholder
    if value:
        element["value"] = value
    if is_multiline is not None:
        element["isMultiline"] = is_multiline
    if max_length:
        element["maxLength"] = max_length

    # Add any additional properties
    element.update(kwargs)

    return element


def input_number(
    id: str,
    placeholder: Optional[str] = None,
    value: Optional[Union[int, float]] = None,
    min: Optional[Union[int, float]] = None,
    max: Optional[Union[int, float]] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Create an Input.Number element.

    Args:
        id: Unique identifier for the input
        placeholder: Placeholder text
        value: Default value
        min: Minimum value
        max: Maximum value
        **kwargs: Additional properties

    Returns:
        Input.Number element dictionary
    """
    element = {"type": "Input.Number", "id": id}

    if placeholder:
        element["placeholder"] = placeholder
    if value is not None:
        element["value"] = value
    if min is not None:
        element["min"] = min
    if max is not None:
        element["max"] = max

    # Add any additional properties
    element.update(kwargs)

    return element


def input_date(
    id: str, placeholder: Optional[str] = None, value: Optional[str] = None, **kwargs
) -> Dict[str, Any]:
    """
    Create an Input.Date element.

    Args:
        id: Unique identifier for the input
        placeholder: Placeholder text
        value: Default value (YYYY-MM-DD format)
        **kwargs: Additional properties

    Returns:
        Input.Date element dictionary
    """
    element = {"type": "Input.Date", "id": id}

    if placeholder:
        element["placeholder"] = placeholder
    if value:
        element["value"] = value

    # Add any additional properties
    element.update(kwargs)

    return element


def input_time(
    id: str, placeholder: Optional[str] = None, value: Optional[str] = None, **kwargs
) -> Dict[str, Any]:
    """
    Create an Input.Time element.

    Args:
        id: Unique identifier for the input
        placeholder: Placeholder text
        value: Default value (HH:MM format)
        **kwargs: Additional properties

    Returns:
        Input.Time element dictionary
    """
    element = {"type": "Input.Time", "id": id}

    if placeholder:
        element["placeholder"] = placeholder
    if value:
        element["value"] = value

    # Add any additional properties
    element.update(kwargs)

    return element


def input_toggle(
    id: str,
    title: str,
    value: Optional[str] = None,
    value_on: Optional[str] = None,
    value_off: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Create an Input.Toggle element.

    Args:
        id: Unique identifier for the input
        title: Toggle title
        value: Default value
        value_on: Value when toggle is on
        value_off: Value when toggle is off
        **kwargs: Additional properties

    Returns:
        Input.Toggle element dictionary
    """
    element = {"type": "Input.Toggle", "id": id, "title": title}

    if value:
        element["value"] = value
    if value_on:
        element["valueOn"] = value_on
    if value_off:
        element["valueOff"] = value_off

    # Add any additional properties
    element.update(kwargs)

    return element


def input_choice_set(
    id: str,
    choices: List[Dict[str, str]],
    placeholder: Optional[str] = None,
    value: Optional[str] = None,
    is_multi_select: Optional[bool] = None,
    style: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    Create an Input.ChoiceSet element.

    Args:
        id: Unique identifier for the input
        choices: List of choice dictionaries with 'title' and 'value' keys
        placeholder: Placeholder text
        value: Default selected value(s)
        is_multi_select: Whether multiple selections are allowed
        style: Choice style (Compact, Expanded)
        **kwargs: Additional properties

    Returns:
        Input.ChoiceSet element dictionary
    """
    element = {"type": "Input.ChoiceSet", "id": id, "choices": choices}

    if placeholder:
        element["placeholder"] = placeholder
    if value:
        element["value"] = value
    if is_multi_select is not None:
        element["isMultiSelect"] = is_multi_select
    if style:
        element["style"] = style

    # Add any additional properties
    element.update(kwargs)

    return element


# Action Elements


def action_submit(
    title: str, data: Optional[Dict[str, Any]] = None, **kwargs
) -> Dict[str, Any]:
    """
    Create an Action.Submit element.

    Args:
        title: Action title
        data: Data to submit
        **kwargs: Additional properties

    Returns:
        Action.Submit element dictionary
    """
    element = {"type": "Action.Submit", "title": title}

    if data:
        element["data"] = data

    # Add any additional properties
    element.update(kwargs)

    return element


def action_open_url(title: str, url: str, **kwargs) -> Dict[str, Any]:
    """
    Create an Action.OpenUrl element.

    Args:
        title: Action title
        url: URL to open
        **kwargs: Additional properties

    Returns:
        Action.OpenUrl element dictionary
    """
    element = {"type": "Action.OpenUrl", "title": title, "url": url}
    element.update(kwargs)
    return element


def action_show_card(title: str, card: Dict[str, Any], **kwargs) -> Dict[str, Any]:
    """
    Create an Action.ShowCard element.

    Args:
        title: Action title
        card: Card to show
        **kwargs: Additional properties

    Returns:
        Action.ShowCard element dictionary
    """
    element = {"type": "Action.ShowCard", "title": title, "card": card}
    element.update(kwargs)
    return element


def qlik_chart(
    chart: Dict[str, Any], alternativeChartTypes: List[Dict[str, Any]], **kwargs
) -> Dict[str, Any]:
    """
    Create an Qlik.Chart element.

    Args:
        chart: Action title
        alternativeChartTypes: Card to show
        **kwargs: Additional properties

    Returns:
        Qlik.Chart element dictionary
    """
    element = {
        "type": "Qlik.Chart",
        "chart": chart,
        "defaultChartType": chart["chartType"],
        "alternativeChartTypes": alternativeChartTypes,
    }
    element.update(kwargs)
    return element


def qlik_skeleton(
    variant: str,
    width: str | None = None,
    height: str | None = None,
) -> Dict[str, Any]:
    """
    Create an Qlik.Skeleton element.

    Args:
        variant: Type of skeleton "text" | "circle" | "rectangle" | "Button" | "IconButton" | "Input" | "InputField"
        alternativeChartTypes: Card to show
        **kwargs: Additional properties

    Returns:
        Qlik.Skeleton element dictionary
    """
    element = {"type": "Qlik.Skeleton", "variant": variant, "isSkeleton": True}

    if width:
        element["width"] = width
    if height:
        element["height"] = height

    return element


def qlik_tag(
    text: str,
    size: str,
    color: str,
) -> Dict[str, Any]:
    """
    Create an Qlik.Tag element.

    Args:
        variant: Type of skeleton "text" | "circle" | "rectangle" | "Button" | "IconButton" | "Input" | "InputField"
        alternativeChartTypes: Card to show
        **kwargs: Additional properties

    Returns:
        Qlik.Tag element dictionary
    """
    element = {"type": "Qlik.Tag", "text": text, "size": size, "color": color}

    return element


def action_show_modal(
    iconUrl: str,
    title: str | None = None,
    style: str = "default",
    size: str = "small",
    **kwargs,
) -> Dict[str, Any]:
    """
    Create an Action.ShowModal element.

    Args:
        iconUrl: Icon URL
        title: Action title
        style: Action style
        size: Action size
        **kwargs: Additional properties

    Returns:
        Action.ShowModal element dictionary
    """
    element = {"type": "Action.ShowModal", "style": style, "size": size}
    if iconUrl:
        element["iconUrl"] = iconUrl
    if title:
        element["title"] = title

    element.update(kwargs)
    return element


def action_toggle_visibility(
    title: str, targetElements: List[str], **kwargs
) -> Dict[str, Any]:
    """
    Create an Action.ToggleVisibility element.

    Args:
        title: Action title
        targetElements: List of target elements
        **kwargs: Additional properties
    """
    element = {
        "type": "Action.ToggleVisibility",
        "title": title,
        "targetElements": targetElements,
    }
    element.update(kwargs)
    return element


def action_menu_dropdown(title: str, **kwargs) -> Dict[str, Any]:
    element = {"type": "Action.MenuDropdown", "title": title}
    element.update(kwargs)
    return element


def action_execute(
    title: str, sheetID: str, sheetIcon: str, **kwargs
) -> Dict[str, Any]:
    element = {
        type: "Action.Execute",
        title: title,
        sheetId: sheetId,
        sheetIcon: sheetIcon,
    }
    element.update(kwargs)
    return element
