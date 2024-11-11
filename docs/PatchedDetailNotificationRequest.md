# PatchedDetailNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen** | **bool** |  | [optional] 

## Example

```python
from mosquito_alert_api.models.patched_detail_notification_request import PatchedDetailNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDetailNotificationRequest from a JSON string
patched_detail_notification_request_instance = PatchedDetailNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDetailNotificationRequest.to_json())

# convert the object into a dict
patched_detail_notification_request_dict = patched_detail_notification_request_instance.to_dict()
# create an instance of PatchedDetailNotificationRequest from a dict
patched_detail_notification_request_from_dict = PatchedDetailNotificationRequest.from_dict(patched_detail_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


