# NotificationsCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.notifications_create_error import NotificationsCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsCreateError from a JSON string
notifications_create_error_instance = NotificationsCreateError.from_json(json)
# print the JSON string representation of the object
print(NotificationsCreateError.to_json())

# convert the object into a dict
notifications_create_error_dict = notifications_create_error_instance.to_dict()
# create an instance of NotificationsCreateError from a dict
notifications_create_error_from_dict = NotificationsCreateError.from_dict(notifications_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


