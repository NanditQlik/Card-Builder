"""
Example showing how to use the AAACards class-based approach.
"""

import sys
import os
import asyncio

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from adaptive_card_builder import AAACards, prettify_json


async def example_individual_components():
    """Example: Create individual components using AAACards class."""
    print("=== Individual Components Example ===")

    # Create AAACards instance
    aaa = AAACards()

    # Sample data
    app_name = "MyApplication"
    title = "Performance Analysis Report"
    subtitle = "Real-time metrics and insights"
    status = "active"
    timestamp = "2023-12-25 10:30:00"
    icon_url = "https://example.com/app-icon.png"

    # Create individual components
    print("\n1. Top Bar Component:")
    chart = aaa.create_chart({"chartType": "barchart"}, [{}, {}])
    skeleton = aaa.create_skeleton()
    toppbar = aaa.create_top_bar("Calculated measure (KPI)", "Total Sales")
    # print(chart)
    # print(skeleton)

    # top_bar_dict = await top_bar.to_dict()
    # print(prettify_json(top_bar_dict))

    # print("\n2. Title Component:")
    # title_section = aaa.create_title(title, subtitle, icon_url)
    # title_dict = await title_section.to_dict()
    # print(prettify_json(title_dict))

    # print("\n3. Status Indicator:")
    # status_indicator = aaa.create_status_indicator(status)
    # status_dict = await status_indicator.to_dict()
    # print(prettify_json(status_dict))

    # print("\n4. App Header:")
    # app_header = aaa.create_app_header(app_name, icon_url)
    # header_dict = await app_header.to_dict()
    # print(prettify_json(header_dict))

    # """Example: Show different status types."""
    # print("\n=== Different Statuses Example ===")

    # # Create AAACards instance
    # aaa = AAACards()

    # statuses = ["active", "completed", "error", "warning"]

    # for status in statuses:
    #     print(f"\nStatus: {status.upper()}")
    #     top_bar = aaa.create_top_bar("TestApp", status, "2023-12-25 10:30:00")
    #     top_bar_dict = await top_bar.to_dict()
    #     print(prettify_json(top_bar_dict))


async def main():
    """Run all examples."""
    print("Adaptive Card Builder - AAACards Class Examples")
    print("=" * 60)

    await example_individual_components()

    print("\n" + "=" * 60)
    print("All examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
