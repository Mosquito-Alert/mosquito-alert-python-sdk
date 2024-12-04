# NotificationsPartialUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.notifications_partial_update_error import NotificationsPartialUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsPartialUpdateError from a JSON string
notifications_partial_update_error_instance = NotificationsPartialUpdateError.from_json(json)
# print the JSON string representation of the object
print(NotificationsPartialUpdateError.to_json())

# convert the object into a dict
notifications_partial_update_error_dict = notifications_partial_update_error_instance.to_dict()
# create an instance of NotificationsPartialUpdateError from a dict
notifications_partial_update_error_from_dict = NotificationsPartialUpdateError.from_dict(notifications_partial_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


