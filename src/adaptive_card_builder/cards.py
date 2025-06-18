"""
Card-specific component builders for different card types.
"""

from typing import List, Dict, Any, Optional
from msteamsadaptivecardbuilder import (
    AdaptiveCard, TextBlock, Image, Container, ColumnSet, Column, ActionSet,
    ActionSubmit, ActionOpenUrl, ActionShowCard
)

from .elements import text_block, container, column_set, column, image, action_set, qlik_chart
from .core import create_card


# ============================================================================
# APP ANALYSIS AGENT (AAA) CARD COMPONENTS
# ============================================================================

def create_aaa_top_bar(
    app_name: str,
    status: str = "active",
    timestamp: Optional[str] = None,
    **kwargs
) -> Container:
    """
    Create the top bar component for App Analysis Agent card.
    
    Args:
        app_name: Name of the application being analyzed
        status: Status of the analysis (active, completed, error)
        timestamp: Timestamp of the analysis
        **kwargs: Additional properties
        
    Returns:
        Container with top bar elements
    """
    status_colors = {
        "active": "Good",
        "completed": "Good", 
        "error": "Attention",
        "warning": "Warning"
    }
    
    status_color = status_colors.get(status.lower(), "Default")
    
    # Status indicator
    status_text = text_block(
        f"● {status.upper()}",
        color=status_color,
        size="Small",
        weight="Bolder"
    )
    
    # App name
    app_title = text_block(
        app_name,
        size="Large",
        weight="Bolder"
    )
    
    # Timestamp (if provided)
    elements = [status_text, app_title]
    if timestamp:
        time_text = text_block(
            timestamp,
            size="Small",
            is_subtle=True
        )
        elements.append(time_text)
    
    return container(
        items=elements,
        style="Emphasis",
        **kwargs
    )


def create_aaa_title(
    title: str,
    subtitle: Optional[str] = None,
    icon_url: Optional[str] = None,
    **kwargs
) -> Container:
    """
    Create the title section for App Analysis Agent card.
    
    Args:
        title: Main title text
        subtitle: Subtitle text (optional)
        icon_url: URL for title icon (optional)
        **kwargs: Additional properties
        
    Returns:
        Container with title elements
    """
    elements = []
    
    # Icon and title in a column set
    if icon_url:
        title_column_set = column_set([
            column([
                image(icon_url, size="Small", width="24px", height="24px")
            ], width="auto"),
            column([
                text_block(title, size="Large", weight="Bolder")
            ], width="stretch")
        ])
        elements.append(title_column_set)
    else:
        elements.append(text_block(title, size="Large", weight="Bolder"))
    
    if subtitle:
        elements.append(text_block(subtitle, size="Medium", is_subtle=True))
    
    return container(items=elements, **kwargs)


def create_aaa_chart(
    chart: Dict[str, Any],
    alternativeChartTypes: List[Dict[str, Any]],
    title: Optional[str] = None,
    **kwargs
) ->  Dict[str, Any]:
    """
    Create a chart section for App Analysis Agent card.
    
    Args:
        chart_data: Chart data dictionary
        chart_type: Type of chart (bar, line, pie, etc.)
        title: Chart title (optional)
        **kwargs: Additional properties
        
    Returns:
        Container with chart elements
    """
    
    return qlik_chart(
        chart,
        alternativeChartTypes,
        **kwargs
    )


def create_aaa_actions(
    primary_action: Optional[Dict[str, Any]] = None,
    secondary_actions: Optional[List[Dict[str, Any]]] = None,
    **kwargs
) -> ActionSet:
    """
    Create actions section for App Analysis Agent card.
    
    Args:
        primary_action: Primary action configuration
        secondary_actions: List of secondary action configurations
        **kwargs: Additional properties
        
    Returns:
        ActionSet with configured actions
    """
    actions = []
    
    # Create action objects manually since adaptivecards doesn't have an actions module
    def create_action(action_config: Dict[str, Any]):
        if action_config.get("type") == "submit":
            return ActionSubmit(title=action_config["title"], data=action_config.get("data", {}))
        elif action_config.get("type") == "url":
            return ActionOpenUrl(title=action_config["title"], url=action_config["url"])
        return None
    
    # Add primary action
    if primary_action:
        action_obj = create_action(primary_action)
        if action_obj:
            actions.append(action_obj)
    
    # Add secondary actions
    if secondary_actions:
        for action_config in secondary_actions:
            action_obj = create_action(action_config)
            if action_obj:
                actions.append(action_obj)
    
    return action_set(actions, **kwargs)


def create_aaa_card(
    app_name: str,
    title: str,
    chart_data: Dict[str, Any],
    status: str = "active",
    subtitle: Optional[str] = None,
    timestamp: Optional[str] = None,
    icon_url: Optional[str] = None,
    primary_action: Optional[Dict[str, Any]] = None,
    secondary_actions: Optional[List[Dict[str, Any]]] = None,
    **kwargs
) -> AdaptiveCard:
    """
    Create a complete App Analysis Agent card.
    
    Args:
        app_name: Name of the application being analyzed
        title: Main title for the analysis
        chart_data: Data for the chart component
        status: Analysis status
        subtitle: Subtitle text (optional)
        timestamp: Analysis timestamp (optional)
        icon_url: Title icon URL (optional)
        primary_action: Primary action configuration (optional)
        secondary_actions: Secondary actions list (optional)
        **kwargs: Additional properties
        
    Returns:
        Complete AdaptiveCard instance
    """
    # Create individual components
    top_bar = create_aaa_top_bar(app_name, status, timestamp)
    title_section = create_aaa_title(title, subtitle, icon_url)
    chart_section = create_aaa_chart(chart_data)
    actions_section = create_aaa_actions(primary_action, secondary_actions)
    
    # Combine all components
    body = [top_bar, title_section, chart_section]
    actions = [actions_section] if actions_section.actions else []
    
    return create_card(body=body, actions=actions, **kwargs)


# ============================================================================
# GENERIC COMPONENT BUILDERS
# ============================================================================

def create_top_bar(
    title: str,
    status: Optional[str] = None,
    status_color: Optional[str] = None,
    **kwargs
) -> Container:
    """
    Create a generic top bar component.
    
    Args:
        title: Top bar title
        status: Status text (optional)
        status_color: Status color (optional)
        **kwargs: Additional properties
        
    Returns:
        Container with top bar elements
    """
    elements = []
    
    if status:
        status_text = text_block(
            status,
            color=status_color or "Default",
            size="Small",
            weight="Bolder"
        )
        elements.append(status_text)
    
    title_text = text_block(title, size="Large", weight="Bolder")
    elements.append(title_text)
    
    return container(items=elements, style="Emphasis", **kwargs)


def create_title_section(
    title: str,
    subtitle: Optional[str] = None,
    icon_url: Optional[str] = None,
    **kwargs
) -> Container:
    """
    Create a generic title section.
    
    Args:
        title: Main title
        subtitle: Subtitle (optional)
        icon_url: Icon URL (optional)
        **kwargs: Additional properties
        
    Returns:
        Container with title elements
    """
    return create_aaa_title(title, subtitle, icon_url, **kwargs)


def create_chart_section(
    chart_data: Dict[str, Any],
    chart_type: str = "bar",
    title: Optional[str] = None,
    **kwargs
) -> Container:
    """
    Create a generic chart section.
    
    Args:
        chart_data: Chart data
        chart_type: Chart type
        title: Chart title (optional)
        **kwargs: Additional properties
        
    Returns:
        Container with chart elements
    """
    return create_aaa_chart(chart_data, chart_type, title, **kwargs)


def create_actions_section(
    actions: List[Dict[str, Any]],
    **kwargs
) -> ActionSet:
    """
    Create a generic actions section.
    
    Args:
        actions: List of action configurations
        **kwargs: Additional properties
        
    Returns:
        ActionSet with configured actions
    """
    action_objects = []
    
    for action_config in actions:
        if action_config.get("type") == "submit":
            action_objects.append(ActionSubmit(title=action_config["title"], data=action_config.get("data", {})))
        elif action_config.get("type") == "url":
            action_objects.append(ActionOpenUrl(title=action_config["title"], url=action_config["url"]))
    
    return action_set(action_objects, **kwargs) 