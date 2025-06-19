"""
App Analysis Agent (AAA) Cards - Class-based implementation.
Provides methods for creating various components of AAA cards using msteamsadaptivecardbuilder.
"""

from typing import List, Dict, Any, Optional
from adaptive_card_builder.utils import to_dict
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
    action_show_card,
)
import json


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

    def menuList(self, sheetData: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        Generate a list of Action.Execute dicts for the menu dropdown based on sheetData.
        """
        actions = []
        for sheet in sheetData:
            actions.append(
                {
                    "type": "Action.Execute",
                    "title": sheet["title"],
                    "sheetId": sheet["sheetId"],
                    "iconUrl": sheet["iconUrl"],
                    "style": "quiet",
                    "fullWidth": True,
                    "verb": "addToNewSheet",
                }
            )
        return actions

    def create_buttons(
        self,
        add_to_sheet,
        sheet_list_actions,
        is_narrative_set: bool,
        card: Dict[str, Any],
    ):
        """
        Create buttons sections for App Analysis Agent card.
        having 2 buttons in one row and one button below that row
        """
        button_column_set1 = column(
            items=[
                action_set(
                    actions=[
                        action_show_card(
                            title="Assumptions",
                            card=card,
                            **{
                                "activeIconUrl": "ViewDisabledOutline",
                                "activeTitle": "Assumptions",
                                "iconUrl": "ViewOutline",
                                "fullWidth": True,
                                "isEnabled": True,
                                "layout": {
                                    "width": "100%",
                                    "margin": "8px 0 16px",
                                    "boxShadow": "none",
                                    "boxSizing": "border-box",
                                    "border": "none",
                                    "backgroundColor": "transparent",
                                },
                                "size": "small",
                                "style": "quiet",
                                "type": "Action.ShowCard",
                            },
                        )
                    ]
                )
            ],
            verticalContentAlignment="center",
            width="stretch",
        )

        button_column_set2 = column(
            items=[
                action_set(
                    actions=[
                        {
                            "type": "Action.ToggleVisibility",
                            "title": "Elaborate",
                            "targetElements": [
                                "moreText",
                                "elaborate",
                                "HideElaboration",
                            ],
                            "actionId": "elaborate",
                            "fullWidth": True,
                            "iconUrl": "AnswersOutline",
                            "isEnabled": True,
                            "size": "small",
                            "style": "quiet",
                            "verb": "elaborate",
                        }
                    ]
                )
            ],
            id="elaborate",
            isVisible=True,
            verticalContentAlignment="center",
            width="stretch",
        )

        button_column_set3 = column(
            items=[
                action_set(
                    actions=[
                        {
                            "type": "Action.ToggleVisibility",
                            "title": "Hide elaboration",
                            "targetElements": [
                                "moreText",
                                "elaborate",
                                "HideElaboration",
                            ],
                            "actionId": "elaborate",
                            "fullWidth": True,
                            "iconUrl": "ViewDisabled",
                            "isEnabled": True,
                            "size": "small",
                            "style": "quiet",
                            "verb": "elaborate",
                        }
                    ]
                )
            ],
            id="HideElaboration",
            isVisible=False,
            verticalContentAlignment="center",
            width="stretch",
        )

        button_row2_column1 = column(
            items=[
                action_set(
                    actions=[
                        {
                            "type": "Action.MenuDropdown",
                            "title": "Add this chart to sheet...",
                            "actions": sheet_list_actions,
                            "data_size": "small",
                            "fullWidth": True,
                            "style": "quiet",
                            "size": "small",
                            "iconUrl": "AddOutline",
                        }
                    ]
                )
            ],
            verticalContentAlignment="center",
            width="stretch",
        )

        buttonsRow1 = column_set(
            columns=[button_column_set1, button_column_set2, button_column_set3],
            **{"separator": True},
        )
        buttonsRow2 = column_set(columns=[button_row2_column1], **{"separator": True})

        actionSet = (
            container(items=[buttonsRow1, buttonsRow2], separator=True)
            if add_to_sheet
            else container(items=[buttonsRow1, buttonsRow2], separator=True)
        )
        print(to_dict(actionSet))
        return to_dict(actionSet)
