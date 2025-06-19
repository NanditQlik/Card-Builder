"""
App Analysis Agent (AAA) Cards - Class-based implementation.
Provides methods for creating various components of AAA cards using msteamsadaptivecardbuilder.
"""

from typing import List, Dict, Any, Optional
from msteamsadaptivecardbuilder import (
    AdaptiveCard,
    TextBlock,
    Image,
    Container,
    ColumnSet,
    Column,
    ActionSet,
    ActionSubmit,
    ActionOpenUrl,
    ActionShowCard,
)
from ..elements import (
    action_show_modal,
    text_block,
    container,
    column_set,
    column,
    image,
    action_set,
    qlik_chart,
    qlik_skeleton,
    qlik_tag,
)
import json


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


class AAACards:
    """
    App Analysis Agent Cards class.
    Provides methods for creating various components of AAA cards.
    """

    def __init__(self):
        """Initialize the AAACards class."""

    def create_skeleton(self) -> List[Dict[str, Any]]:
        """
        Create a Skeleton section for App Analysis Agent card.
        Returns:
            List of all the skeletons needed for App-Analysis-Agentlik.Chart element dictionary
        """

        return [
            to_dict(
                column_set(
                    [
                        column(
                            [qlik_skeleton(variant="text", width="100%")],
                            **{
                                "verticalContentAlignment": "top",
                                "width": "75%",
                                "isSkeleton": True,
                            },
                        )
                    ]
                )
            ),
            qlik_skeleton(variant="rectangle", width="100%", height="300px"),
            to_dict(column_set([], **{"spacing": "padding", "isSkeleton": True})),
        ]

    def create_top_bar(
        self, analysisType: str, title: str | bool = False
    ) -> Dict[str, Any]:
        """
        Create the top bar component for App Analysis Agent card.

        Args:
            analysisType: Type of analysis (e.g., "performance", "usage", "errors")
            title: Title of the analysis (optional)
        """

        column_set1 = column_set(
            columns=[
                column(
                    items=[qlik_tag(text=analysisType, size="s", color="info")],
                    **{"spacing": "small", "verticalContentAlignment": "top"},
                ),
                column(items=[], width="stretch"),
                column(
                    items=[
                        action_set(
                            actions=[action_show_modal(iconUrl="Maximize")],
                            **{"color": "info", "addPaddingLeft": True},
                        )
                    ],
                    **{"verticalContentAlignment": "top"},
                ),
            ]
        )

        column_set2 = column_set(
            columns=[
                column(
                    items=(
                        [
                            qlik_skeleton(variant="rectangle", height="24px"),
                            qlik_skeleton(variant="rectangle", height="24px"),
                        ]
                        if type(title) is bool
                        else [
                            text_block(
                                title,
                                size="large",
                                weight="bolder",
                                **{"isSubtle": False, "wrap": True, "content": True},
                            )
                        ]
                    ),
                    **{"verticalContentAlignment": "top", "spacing": "small"},
                ),
            ],
            **{"spacing": "small"},
        )

        finalElement = container(
            items=[column_set1, column_set2],
        )

        print(to_dict(finalElement))

        return to_dict(finalElement)

    def create_chart(
        self,
        chart: Dict[str, Any],
        alternative_chart_types: List[Dict[str, Any]],
        title: Optional[str] = None,
        **kwargs,
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
        return qlik_chart(chart, alternative_chart_types, **kwargs)
