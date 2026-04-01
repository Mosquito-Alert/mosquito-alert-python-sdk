# MessagesTopicsSendError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.messages_topics_send_error import MessagesTopicsSendError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesTopicsSendError from a JSON string
messages_topics_send_error_instance = MessagesTopicsSendError.from_json(json)
# print the JSON string representation of the object
print(MessagesTopicsSendError.to_json())

# convert the object into a dict
messages_topics_send_error_dict = messages_topics_send_error_instance.to_dict()
# create an instance of MessagesTopicsSendError from a dict
messages_topics_send_error_from_dict = MessagesTopicsSendError.from_dict(messages_topics_send_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


