# CreateTopicMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**CreateTopicMessageContentRequest**](CreateTopicMessageContentRequest.md) | The content of the message for the topic | 

## Example

```python
from mosquito_alert.models.create_topic_message_request import CreateTopicMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicMessageRequest from a JSON string
create_topic_message_request_instance = CreateTopicMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTopicMessageRequest.to_json())

# convert the object into a dict
create_topic_message_request_dict = create_topic_message_request_instance.to_dict()
# create an instance of CreateTopicMessageRequest from a dict
create_topic_message_request_from_dict = CreateTopicMessageRequest.from_dict(create_topic_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


