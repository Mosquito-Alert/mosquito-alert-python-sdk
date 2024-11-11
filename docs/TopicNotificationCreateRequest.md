# TopicNotificationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver_type** | **str** |  | 
**title_en** | **str** |  | 
**body_en** | **str** |  | 
**topic_code** | **str** |  | 

## Example

```python
from mosquito_alert_api.models.topic_notification_create_request import TopicNotificationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TopicNotificationCreateRequest from a JSON string
topic_notification_create_request_instance = TopicNotificationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TopicNotificationCreateRequest.to_json())

# convert the object into a dict
topic_notification_create_request_dict = topic_notification_create_request_instance.to_dict()
# create an instance of TopicNotificationCreateRequest from a dict
topic_notification_create_request_from_dict = TopicNotificationCreateRequest.from_dict(topic_notification_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


