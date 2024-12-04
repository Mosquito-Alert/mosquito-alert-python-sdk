# NotificationsListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.notifications_list_error import NotificationsListError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsListError from a JSON string
notifications_list_error_instance = NotificationsListError.from_json(json)
# print the JSON string representation of the object
print(NotificationsListError.to_json())

# convert the object into a dict
notifications_list_error_dict = notifications_list_error_instance.to_dict()
# create an instance of NotificationsListError from a dict
notifications_list_error_from_dict = NotificationsListError.from_dict(notifications_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


