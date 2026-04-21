# CreateTopicMessageContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedTopicMessageTitle**](LocalizedTopicMessageTitle.md) | Provide the message&#39;s title in all supported languages for this topic | 
**body** | [**LocalizedTopicMessageBody**](LocalizedTopicMessageBody.md) | Provide the message&#39;s body in all supported languages for this topic | 

## Example

```python
from mosquito_alert.models.create_topic_message_content import CreateTopicMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicMessageContent from a JSON string
create_topic_message_content_instance = CreateTopicMessageContent.from_json(json)
# print the JSON string representation of the object
print(CreateTopicMessageContent.to_json())

# convert the object into a dict
create_topic_message_content_dict = create_topic_message_content_instance.to_dict()
# create an instance of CreateTopicMessageContent from a dict
create_topic_message_content_from_dict = CreateTopicMessageContent.from_dict(create_topic_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


