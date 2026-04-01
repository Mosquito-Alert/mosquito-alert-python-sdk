# MessageContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedMessageTitleRequest**](LocalizedMessageTitleRequest.md) | Provide the message&#39;s title in all supported languages | 
**body** | [**LocalizedMessageBodyRequest**](LocalizedMessageBodyRequest.md) | Provide the message&#39;s body in all supported languages | 

## Example

```python
from mosquito_alert.models.message_content_request import MessageContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContentRequest from a JSON string
message_content_request_instance = MessageContentRequest.from_json(json)
# print the JSON string representation of the object
print(MessageContentRequest.to_json())

# convert the object into a dict
message_content_request_dict = message_content_request_instance.to_dict()
# create an instance of MessageContentRequest from a dict
message_content_request_from_dict = MessageContentRequest.from_dict(message_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


