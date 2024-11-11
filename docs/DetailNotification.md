# DetailNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**expert_id** | **int** | Expert sending the notification | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**title** | **str** |  | [readonly] 
**body** | **str** |  | [readonly] 
**seen** | **bool** |  | [readonly] 

## Example

```python
from mosquito_alert_api.models.detail_notification import DetailNotification

# TODO update the JSON string below
json = "{}"
# create an instance of DetailNotification from a JSON string
detail_notification_instance = DetailNotification.from_json(json)
# print the JSON string representation of the object
print(DetailNotification.to_json())

# convert the object into a dict
detail_notification_dict = detail_notification_instance.to_dict()
# create an instance of DetailNotification from a dict
detail_notification_from_dict = DetailNotification.from_dict(detail_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


