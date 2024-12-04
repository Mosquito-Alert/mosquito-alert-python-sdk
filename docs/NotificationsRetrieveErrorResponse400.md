# NotificationsRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.notifications_retrieve_error_response400 import NotificationsRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsRetrieveErrorResponse400 from a JSON string
notifications_retrieve_error_response400_instance = NotificationsRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(NotificationsRetrieveErrorResponse400.to_json())

# convert the object into a dict
notifications_retrieve_error_response400_dict = notifications_retrieve_error_response400_instance.to_dict()
# create an instance of NotificationsRetrieveErrorResponse400 from a dict
notifications_retrieve_error_response400_from_dict = NotificationsRetrieveErrorResponse400.from_dict(notifications_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


