import asyncio
from msteamsadaptivecardbuilder import (
    AdaptiveCard, TextBlock, Container, ColumnSet, Column, 
    Image, ActionSet, ActionSubmit, ActionOpenUrl
)

async def test_api():
    # Create a simple card
    card = AdaptiveCard()
    text = TextBlock("Hello World")
    card.add(text)
    
    # Test to_dict method
    result = await card.to_dict()
    print("Card as dict:", result)
    
    # Test to_json method
    json_result = await card.to_json()
    print("Card as JSON:", json_result)
    
    # Test Container
    print("\n--- Testing Container ---")
    container = Container()
    container_text = TextBlock("Container text")
    container.add(container_text)
    print("Container:", await container.to_dict())
    
    # Test ColumnSet and Column
    print("\n--- Testing ColumnSet ---")
    column_set = ColumnSet()
    column1 = Column()
    column1.add(TextBlock("Column 1"))
    column2 = Column()
    column2.add(TextBlock("Column 2"))
    column_set.add(column1)
    column_set.add(column2)
    print("ColumnSet:", await column_set.to_dict())
    
    # Test Actions
    print("\n--- Testing Actions ---")
    action_set = ActionSet()
    submit_action = ActionSubmit("Submit", data={"action": "submit"})
    url_action = ActionOpenUrl("Open URL", "https://example.com")
    action_set.add(submit_action)
    action_set.add(url_action)
    print("ActionSet:", await action_set.to_dict())

if __name__ == "__main__":
    asyncio.run(test_api()) 