# MessageTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code for the topic. | 
**description** | **str** | Description for the topic, in english. | 

## Example

```python
from mosquito_alert.models.message_topic import MessageTopic

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTopic from a JSON string
message_topic_instance = MessageTopic.from_json(json)
# print the JSON string representation of the object
print(MessageTopic.to_json())

# convert the object into a dict
message_topic_dict = message_topic_instance.to_dict()
# create an instance of MessageTopic from a dict
message_topic_from_dict = MessageTopic.from_dict(message_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


