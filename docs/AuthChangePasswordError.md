# AuthChangePasswordError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_change_password_error import AuthChangePasswordError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthChangePasswordError from a JSON string
auth_change_password_error_instance = AuthChangePasswordError.from_json(json)
# print the JSON string representation of the object
print(AuthChangePasswordError.to_json())

# convert the object into a dict
auth_change_password_error_dict = auth_change_password_error_instance.to_dict()
# create an instance of AuthChangePasswordError from a dict
auth_change_password_error_from_dict = AuthChangePasswordError.from_dict(auth_change_password_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


