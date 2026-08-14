# MessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**sender_user** | [**SimpleUser**](SimpleUser.md) |  | [readonly] 
**content** | [**MessageListContent**](MessageListContent.md) |  | [readonly] 
**target** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.message_list import MessageList

# TODO update the JSON string below
json = "{}"
# create an instance of MessageList from a JSON string
message_list_instance = MessageList.from_json(json)
# print the JSON string representation of the object
print(MessageList.to_json())

# convert the object into a dict
message_list_dict = message_list_instance.to_dict()
# create an instance of MessageList from a dict
message_list_from_dict = MessageList.from_dict(message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


