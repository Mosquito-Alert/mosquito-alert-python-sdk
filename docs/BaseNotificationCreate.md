# BaseNotificationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert_api.models.base_notification_create import BaseNotificationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BaseNotificationCreate from a JSON string
base_notification_create_instance = BaseNotificationCreate.from_json(json)
# print the JSON string representation of the object
print(BaseNotificationCreate.to_json())

# convert the object into a dict
base_notification_create_dict = base_notification_create_instance.to_dict()
# create an instance of BaseNotificationCreate from a dict
base_notification_create_from_dict = BaseNotificationCreate.from_dict(base_notification_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


