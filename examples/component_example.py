"""
Example showing component-based card building for App Analysis Agent.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from adaptive_card_builder import (
    create_aaa_top_bar,
    create_aaa_title,
    create_aaa_chart,
    create_aaa_actions,
    create_aaa_card,
    prettify_json
)


def example_individual_components():
    """Example: Create individual components for App Analysis Agent."""
    print("=== Individual Components Example ===")
    
    # Sample data
    app_name = "MyApplication"
    title = "Performance Analysis Report"
    subtitle = "Real-time metrics and insights"
    status = "active"
    timestamp = "2023-12-25 10:30:00"
    icon_url = "https://example.com/app-icon.png"
    
    chart_data = {
        "type": "bar",
        "data": [
            {"label": "CPU Usage", "value": 75},
            {"label": "Memory Usage", "value": 60},
            {"label": "Network I/O", "value": 45}
        ],
        "summary": "Overall performance is good with CPU usage at 75%"
    }
    
    primary_action = {
        "type": "submit",
        "title": "View Details",
        "data": {"action": "view_details", "app_id": "myapp-123"}
    }
    
    secondary_actions = [
        {
            "type": "url",
            "title": "Open Dashboard",
            "url": "https://dashboard.example.com/myapp"
        },
        {
            "type": "submit",
            "title": "Export Report",
            "data": {"action": "export", "format": "pdf"}
        }
    ]
    
    # Create individual components
    print("\n1. Top Bar Component:")
    top_bar = create_aaa_top_bar(app_name, status, timestamp)
    print(prettify_json(top_bar))
    
    print("\n2. Title Component:")
    title_section = create_aaa_title(title, subtitle, icon_url)
    print(prettify_json(title_section))
    
    print("\n3. Chart Component:")
    chart_section = create_aaa_chart(chart_data, chart_type="bar", title="Performance Metrics")
    print(prettify_json(chart_section))
    
    print("\n4. Actions Component:")
    actions_section = create_aaa_actions(primary_action, secondary_actions)
    print(prettify_json(actions_section))


def example_complete_card():
    """Example: Create complete App Analysis Agent card."""
    print("\n=== Complete Card Example ===")
    
    # Sample data
    app_name = "MyApplication"
    title = "Performance Analysis Report"
    subtitle = "Real-time metrics and insights"
    status = "active"
    timestamp = "2023-12-25 10:30:00"
    icon_url = "https://example.com/app-icon.png"
    
    chart_data = {
        "type": "bar",
        "data": [
            {"label": "CPU Usage", "value": 75},
            {"label": "Memory Usage", "value": 60},
            {"label": "Network I/O", "value": 45}
        ],
        "summary": "Overall performance is good with CPU usage at 75%"
    }
    
    primary_action = {
        "type": "submit",
        "title": "View Details",
        "data": {"action": "view_details", "app_id": "myapp-123"}
    }
    
    secondary_actions = [
        {
            "type": "url",
            "title": "Open Dashboard",
            "url": "https://dashboard.example.com/myapp"
        },
        {
            "type": "submit",
            "title": "Export Report",
            "data": {"action": "export", "format": "pdf"}
        }
    ]
    
    # Create complete card
    # card = create_aaa_card(
    #     app_name=app_name,
    #     title=title,
    #     chart_data=chart_data,
    #     status=status,
    #     subtitle=subtitle,
    #     timestamp=timestamp,
    #     icon_url=icon_url,
    #     primary_action=primary_action,
    #     secondary_actions=secondary_actions
    # )
    
    print(prettify_json(card))


def example_different_statuses():
    """Example: Show different status types."""
    print("\n=== Different Statuses Example ===")
    
    statuses = ["active", "completed", "error", "warning"]
    
    for status in statuses:
        print(f"\nStatus: {status.upper()}")
        top_bar = create_aaa_top_bar("TestApp", status, "2023-12-25 10:30:00")
        print(prettify_json(top_bar))


def example_streaming_simulation():
    """Example: Simulate streaming components one by one."""
    print("\n=== Streaming Simulation Example ===")
    
    import time
    
    app_name = "StreamingApp"
    title = "Real-time Analysis"
    chart_data = {
        "chartType": "line",
        "data": [{"label": "Time", "value": 100}],
        "summary": "Real-time data streaming"
    }
    
    components = [
        # ("Top Bar", create_aaa_top_bar(app_name, "active", "2023-12-25 10:30:00")),
        # ("Title", create_aaa_title(title, "Live streaming data")),
        ("Chart", create_aaa_chart(chart_data, [chart_data,chart_data])),
        # ("Actions", create_aaa_actions({
        #     "type": "submit",
        #     "title": "Stop Streaming",
        #     "data": {"action": "stop_stream"}
        # }))
    ]
    
    for i, (component_name, component) in enumerate(components, 1):
        print(f"\nStreaming component {i}/4: {component_name}")
        time.sleep(0.5)  # Simulate processing time
        print(prettify_json(component))


if __name__ == "__main__":
    print("Adaptive Card Builder - Component-Based Examples")
    print("=" * 60)
    
    # example_individual_components()
    # example_complete_card()
    # example_different_statuses()
    example_streaming_simulation()
    
    print("\n" + "=" * 60)
    print("All examples completed!") 


