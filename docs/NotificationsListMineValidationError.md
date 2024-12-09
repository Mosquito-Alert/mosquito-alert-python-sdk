# NotificationsListMineValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[NotificationsListMineError]**](NotificationsListMineError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_list_mine_validation_error import NotificationsListMineValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsListMineValidationError from a JSON string
notifications_list_mine_validation_error_instance = NotificationsListMineValidationError.from_json(json)
# print the JSON string representation of the object
print(NotificationsListMineValidationError.to_json())

# convert the object into a dict
notifications_list_mine_validation_error_dict = notifications_list_mine_validation_error_instance.to_dict()
# create an instance of NotificationsListMineValidationError from a dict
notifications_list_mine_validation_error_from_dict = NotificationsListMineValidationError.from_dict(notifications_list_mine_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


