# NotificationsPartialUpdateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_partial_update_error_response400 import NotificationsPartialUpdateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsPartialUpdateErrorResponse400 from a JSON string
notifications_partial_update_error_response400_instance = NotificationsPartialUpdateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(NotificationsPartialUpdateErrorResponse400.to_json())

# convert the object into a dict
notifications_partial_update_error_response400_dict = notifications_partial_update_error_response400_instance.to_dict()
# create an instance of NotificationsPartialUpdateErrorResponse400 from a dict
notifications_partial_update_error_response400_from_dict = NotificationsPartialUpdateErrorResponse400.from_dict(notifications_partial_update_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


