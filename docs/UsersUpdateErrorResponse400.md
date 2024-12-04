# UsersUpdateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.users_update_error_response400 import UsersUpdateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateErrorResponse400 from a JSON string
users_update_error_response400_instance = UsersUpdateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateErrorResponse400.to_json())

# convert the object into a dict
users_update_error_response400_dict = users_update_error_response400_instance.to_dict()
# create an instance of UsersUpdateErrorResponse400 from a dict
users_update_error_response400_from_dict = UsersUpdateErrorResponse400.from_dict(users_update_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


