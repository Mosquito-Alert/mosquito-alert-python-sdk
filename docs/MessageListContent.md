# MessageListContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedMessageTitle**](LocalizedMessageTitle.md) | Provide the message&#39;s title in all supported languages | 
**body** | [**LocalizedMessageBodyPreview**](LocalizedMessageBodyPreview.md) | Provide the message&#39;s body in all supported languages | 

## Example

```python
from mosquito_alert.models.message_list_content import MessageListContent

# TODO update the JSON string below
json = "{}"
# create an instance of MessageListContent from a JSON string
message_list_content_instance = MessageListContent.from_json(json)
# print the JSON string representation of the object
print(MessageListContent.to_json())

# convert the object into a dict
message_list_content_dict = message_list_content_instance.to_dict()
# create an instance of MessageListContent from a dict
message_list_content_from_dict = MessageListContent.from_dict(message_list_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


