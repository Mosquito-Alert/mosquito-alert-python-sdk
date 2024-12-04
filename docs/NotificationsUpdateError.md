# NotificationsUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.notifications_update_error import NotificationsUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsUpdateError from a JSON string
notifications_update_error_instance = NotificationsUpdateError.from_json(json)
# print the JSON string representation of the object
print(NotificationsUpdateError.to_json())

# convert the object into a dict
notifications_update_error_dict = notifications_update_error_instance.to_dict()
# create an instance of NotificationsUpdateError from a dict
notifications_update_error_from_dict = NotificationsUpdateError.from_dict(notifications_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


