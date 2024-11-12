# MetaNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver_type** | **str** |  | 
**title_en** | **str** |  | 
**body_en** | **str** |  | 
**user_uuid** | **str** |  | 
**topic_code** | **str** |  | 

## Example

```python
from mosquito_alert.models.meta_notification_request import MetaNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetaNotificationRequest from a JSON string
meta_notification_request_instance = MetaNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(MetaNotificationRequest.to_json())

# convert the object into a dict
meta_notification_request_dict = meta_notification_request_instance.to_dict()
# create an instance of MetaNotificationRequest from a dict
meta_notification_request_from_dict = MetaNotificationRequest.from_dict(meta_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


