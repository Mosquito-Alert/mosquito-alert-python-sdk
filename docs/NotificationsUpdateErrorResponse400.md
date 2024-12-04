# NotificationsUpdateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_update_error_response400 import NotificationsUpdateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsUpdateErrorResponse400 from a JSON string
notifications_update_error_response400_instance = NotificationsUpdateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(NotificationsUpdateErrorResponse400.to_json())

# convert the object into a dict
notifications_update_error_response400_dict = notifications_update_error_response400_instance.to_dict()
# create an instance of NotificationsUpdateErrorResponse400 from a dict
notifications_update_error_response400_from_dict = NotificationsUpdateErrorResponse400.from_dict(notifications_update_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


