# MessagesTopicsSendValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[MessagesTopicsSendError]**](MessagesTopicsSendError.md) |  | 

## Example

```python
from mosquito_alert.models.messages_topics_send_validation_error import MessagesTopicsSendValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesTopicsSendValidationError from a JSON string
messages_topics_send_validation_error_instance = MessagesTopicsSendValidationError.from_json(json)
# print the JSON string representation of the object
print(MessagesTopicsSendValidationError.to_json())

# convert the object into a dict
messages_topics_send_validation_error_dict = messages_topics_send_validation_error_instance.to_dict()
# create an instance of MessagesTopicsSendValidationError from a dict
messages_topics_send_validation_error_from_dict = MessagesTopicsSendValidationError.from_dict(messages_topics_send_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


