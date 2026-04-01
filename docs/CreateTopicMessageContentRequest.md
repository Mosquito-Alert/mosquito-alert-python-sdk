# CreateTopicMessageContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedTopicMessageTitleRequest**](LocalizedTopicMessageTitleRequest.md) | Provide the message&#39;s title in all supported languages for this topic | 
**body** | [**LocalizedTopicMessageBodyRequest**](LocalizedTopicMessageBodyRequest.md) | Provide the message&#39;s body in all supported languages for this topic | 

## Example

```python
from mosquito_alert.models.create_topic_message_content_request import CreateTopicMessageContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicMessageContentRequest from a JSON string
create_topic_message_content_request_instance = CreateTopicMessageContentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTopicMessageContentRequest.to_json())

# convert the object into a dict
create_topic_message_content_request_dict = create_topic_message_content_request_instance.to_dict()
# create an instance of CreateTopicMessageContentRequest from a dict
create_topic_message_content_request_from_dict = CreateTopicMessageContentRequest.from_dict(create_topic_message_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


