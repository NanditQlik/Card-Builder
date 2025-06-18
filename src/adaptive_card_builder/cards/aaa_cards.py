"""
App Analysis Agent (AAA) Cards - Class-based implementation.
Provides methods for creating various components of AAA cards using msteamsadaptivecardbuilder.
"""

from typing import List, Dict, Any, Optional
from msteamsadaptivecardbuilder import (
    AdaptiveCard, TextBlock, Image, Container, ColumnSet, Column, ActionSet,
    ActionSubmit, ActionOpenUrl, ActionShowCard
)
from ..elements import text_block, container, column_set, column, image, action_set, qlik_chart


class AAACards:
    """
    App Analysis Agent Cards class.
    Provides methods for creating various components of AAA cards.
    """
    
    def __init__(self):
        """Initialize the AAACards class."""
        self.status_colors = {
            "active": "Good",
            "completed": "Good", 
            "error": "Attention",
            "warning": "Warning"
        }
    
    def create_top_bar(
        self,
        app_name: str,
        status: str = "active",
        timestamp: Optional[str] = None,
        **kwargs
    ) -> Container:
        """
        Create the top bar component for App Analysis Agent card.
        
        Args:
            app_name: Name of the application being analyzed
            status: Status of the analysis (active, completed, error, warning)
            timestamp: Timestamp of the analysis
            **kwargs: Additional properties
            
        Returns:
            Container with top bar elements
        """
        status_color = self.status_colors.get(status.lower(), "Default")
        
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
    
    def create_title(
        self,
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
    
    def create_chart(
        self,
        chart: Dict[str, Any],
        alternative_chart_types: List[Dict[str, Any]],
        title: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a chart section for App Analysis Agent card.
        
        Args:
            chart: Chart data dictionary
            alternative_chart_types: List of alternative chart types
            title: Chart title (optional)
            **kwargs: Additional properties
            
        Returns:
            Qlik.Chart element dictionary
        """
        return qlik_chart(
            chart,
            alternative_chart_types,
            **kwargs
        )
    
    def create_actions(
        self,
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
        
        def create_action(action_config: Dict[str, Any]):
            """Helper function to create action objects."""
            if action_config.get("type") == "submit":
                return ActionSubmit(
                    title=action_config["title"], 
                    data=action_config.get("data", {})
                )
            elif action_config.get("type") == "url":
                return ActionOpenUrl(
                    title=action_config["title"], 
                    url=action_config["url"]
                )
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
    
    async def create_card(
        self,
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
            title: Main title of the card
            chart_data: Chart data dictionary
            status: Status of the analysis
            subtitle: Subtitle text (optional)
            timestamp: Timestamp of the analysis (optional)
            icon_url: URL for title icon (optional)
            primary_action: Primary action configuration (optional)
            secondary_actions: List of secondary action configurations (optional)
            **kwargs: Additional properties
            
        Returns:
            Complete AdaptiveCard instance
        """
        # Create card components
        top_bar = self.create_top_bar(app_name, status, timestamp)
        title_section = self.create_title(title, subtitle, icon_url)
        chart_section = self.create_chart(chart_data, [chart_data, chart_data])  # Using same data as alternatives
        actions_section = self.create_actions(primary_action, secondary_actions)
        
        # Create the main card
        card = AdaptiveCard(version="1.2", **kwargs)
        
        # Add components to card
        card.add(top_bar)
        card.add(title_section)
        card.add(chart_section)
        card.add(actions_section)
        
        return card
    
    def create_simple_aaa_card(
        self,
        app_name: str,
        title: str,
        status: str = "active",
        **kwargs
    ) -> AdaptiveCard:
        """
        Create a simple App Analysis Agent card with minimal components.
        
        Args:
            app_name: Name of the application
            title: Card title
            status: Status of the analysis
            **kwargs: Additional properties
            
        Returns:
            Simple AdaptiveCard instance
        """
        top_bar = self.create_top_bar(app_name, status)
        title_section = self.create_title(title)
        
        card = AdaptiveCard(version="1.2", **kwargs)
        card.add(top_bar)
        card.add(title_section)
        
        return card
    
    def create_status_indicator(
        self,
        status: str,
        **kwargs
    ) -> TextBlock:
        """
        Create a standalone status indicator.
        
        Args:
            status: Status text
            **kwargs: Additional properties
            
        Returns:
            TextBlock with status indicator
        """
        status_color = self.status_colors.get(status.lower(), "Default")
        return text_block(
            f"● {status.upper()}",
            color=status_color,
            size="Small",
            weight="Bolder",
            **kwargs
        )
    
    def create_app_header(
        self,
        app_name: str,
        icon_url: Optional[str] = None,
        **kwargs
    ) -> Container:
        """
        Create an app header with name and optional icon.
        
        Args:
            app_name: Name of the application
            icon_url: URL for app icon (optional)
            **kwargs: Additional properties
            
        Returns:
            Container with app header
        """
        if icon_url:
            return container(
                items=[
                    column_set([
                        column([
                            image(icon_url, size="Small", width="24px", height="24px")
                        ], width="auto"),
                        column([
                            text_block(app_name, size="Large", weight="Bolder")
                        ], width="stretch")
                    ])
                ],
                **kwargs
            )
        else:
            return container(
                items=[
                    text_block(app_name, size="Large", weight="Bolder")
                ],
                **kwargs
            )
    
    def create_metric_display(
        self,
        metrics: List[Dict[str, Any]],
        title: Optional[str] = None,
        **kwargs
    ) -> Container:
        """
        Create a metrics display section.
        
        Args:
            metrics: List of metric dictionaries with 'label' and 'value' keys
            title: Section title (optional)
            **kwargs: Additional properties
            
        Returns:
            Container with metrics display
        """
        elements = []
        
        if title:
            elements.append(text_block(title, size="Medium", weight="Bolder"))
        
        # Create metric items
        for metric in metrics:
            metric_text = text_block(
                f"{metric['label']}: {metric['value']}",
                size="Small"
            )
            elements.append(metric_text)
        
        return container(items=elements, **kwargs) 