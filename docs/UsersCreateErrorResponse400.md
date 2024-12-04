# UsersCreateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.users_create_error_response400 import UsersCreateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateErrorResponse400 from a JSON string
users_create_error_response400_instance = UsersCreateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(UsersCreateErrorResponse400.to_json())

# convert the object into a dict
users_create_error_response400_dict = users_create_error_response400_instance.to_dict()
# create an instance of UsersCreateErrorResponse400 from a dict
users_create_error_response400_from_dict = UsersCreateErrorResponse400.from_dict(users_create_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

