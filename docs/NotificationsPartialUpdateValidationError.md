# NotificationsPartialUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[NotificationsPartialUpdateError]**](NotificationsPartialUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_partial_update_validation_error import NotificationsPartialUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsPartialUpdateValidationError from a JSON string
notifications_partial_update_validation_error_instance = NotificationsPartialUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(NotificationsPartialUpdateValidationError.to_json())

# convert the object into a dict
notifications_partial_update_validation_error_dict = notifications_partial_update_validation_error_instance.to_dict()
# create an instance of NotificationsPartialUpdateValidationError from a dict
notifications_partial_update_validation_error_from_dict = NotificationsPartialUpdateValidationError.from_dict(notifications_partial_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


