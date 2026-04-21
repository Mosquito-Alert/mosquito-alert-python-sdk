# CreateUserMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**sender_user** | [**SimpleUser**](SimpleUser.md) |  | [readonly] 
**content** | [**MessageContent**](MessageContent.md) | The content of the message | 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.create_user_message import CreateUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMessage from a JSON string
create_user_message_instance = CreateUserMessage.from_json(json)
# print the JSON string representation of the object
print(CreateUserMessage.to_json())

# convert the object into a dict
create_user_message_dict = create_user_message_instance.to_dict()
# create an instance of CreateUserMessage from a dict
create_user_message_from_dict = CreateUserMessage.from_dict(create_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


