# CreateTopicMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**sender_user** | [**SimpleUser**](SimpleUser.md) |  | [readonly] 
**content** | [**CreateTopicMessageContent**](CreateTopicMessageContent.md) | The content of the message for the topic | 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.create_topic_message import CreateTopicMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicMessage from a JSON string
create_topic_message_instance = CreateTopicMessage.from_json(json)
# print the JSON string representation of the object
print(CreateTopicMessage.to_json())

# convert the object into a dict
create_topic_message_dict = create_topic_message_instance.to_dict()
# create an instance of CreateTopicMessage from a dict
create_topic_message_from_dict = CreateTopicMessage.from_dict(create_topic_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


