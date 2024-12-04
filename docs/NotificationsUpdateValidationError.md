# NotificationsUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[NotificationsUpdateError]**](NotificationsUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_update_validation_error import NotificationsUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsUpdateValidationError from a JSON string
notifications_update_validation_error_instance = NotificationsUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(NotificationsUpdateValidationError.to_json())

# convert the object into a dict
notifications_update_validation_error_dict = notifications_update_validation_error_instance.to_dict()
# create an instance of NotificationsUpdateValidationError from a dict
notifications_update_validation_error_from_dict = NotificationsUpdateValidationError.from_dict(notifications_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


