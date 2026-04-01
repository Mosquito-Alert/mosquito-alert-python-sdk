# CreateUserMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuids** | **List[UUID]** |  | 
**content** | [**MessageContentRequest**](MessageContentRequest.md) | The content of the message | 

## Example

```python
from mosquito_alert.models.create_user_message_request import CreateUserMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserMessageRequest from a JSON string
create_user_message_request_instance = CreateUserMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserMessageRequest.to_json())

# convert the object into a dict
create_user_message_request_dict = create_user_message_request_instance.to_dict()
# create an instance of CreateUserMessageRequest from a dict
create_user_message_request_from_dict = CreateUserMessageRequest.from_dict(create_user_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


