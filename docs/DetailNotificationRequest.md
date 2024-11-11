# DetailNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen** | **bool** |  | 

## Example

```python
from mosquito_alert_api.models.detail_notification_request import DetailNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetailNotificationRequest from a JSON string
detail_notification_request_instance = DetailNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(DetailNotificationRequest.to_json())

# convert the object into a dict
detail_notification_request_dict = detail_notification_request_instance.to_dict()
# create an instance of DetailNotificationRequest from a dict
detail_notification_request_from_dict = DetailNotificationRequest.from_dict(detail_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


