# NotificationsCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[NotificationsCreateError]**](NotificationsCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_create_validation_error import NotificationsCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsCreateValidationError from a JSON string
notifications_create_validation_error_instance = NotificationsCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(NotificationsCreateValidationError.to_json())

# convert the object into a dict
notifications_create_validation_error_dict = notifications_create_validation_error_instance.to_dict()
# create an instance of NotificationsCreateValidationError from a dict
notifications_create_validation_error_from_dict = NotificationsCreateValidationError.from_dict(notifications_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


