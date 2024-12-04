# NotificationsCreateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_create_error_response400 import NotificationsCreateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsCreateErrorResponse400 from a JSON string
notifications_create_error_response400_instance = NotificationsCreateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(NotificationsCreateErrorResponse400.to_json())

# convert the object into a dict
notifications_create_error_response400_dict = notifications_create_error_response400_instance.to_dict()
# create an instance of NotificationsCreateErrorResponse400 from a dict
notifications_create_error_response400_from_dict = NotificationsCreateErrorResponse400.from_dict(notifications_create_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


