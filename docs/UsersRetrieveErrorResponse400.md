# UsersRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.users_retrieve_error_response400 import UsersRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of UsersRetrieveErrorResponse400 from a JSON string
users_retrieve_error_response400_instance = UsersRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(UsersRetrieveErrorResponse400.to_json())

# convert the object into a dict
users_retrieve_error_response400_dict = users_retrieve_error_response400_instance.to_dict()
# create an instance of UsersRetrieveErrorResponse400 from a dict
users_retrieve_error_response400_from_dict = UsersRetrieveErrorResponse400.from_dict(users_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


