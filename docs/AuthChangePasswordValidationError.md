# AuthChangePasswordValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[AuthChangePasswordError]**](AuthChangePasswordError.md) |  | 

## Example

```python
from mosquito_alert.models.auth_change_password_validation_error import AuthChangePasswordValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthChangePasswordValidationError from a JSON string
auth_change_password_validation_error_instance = AuthChangePasswordValidationError.from_json(json)
# print the JSON string representation of the object
print(AuthChangePasswordValidationError.to_json())

# convert the object into a dict
auth_change_password_validation_error_dict = auth_change_password_validation_error_instance.to_dict()
# create an instance of AuthChangePasswordValidationError from a dict
auth_change_password_validation_error_from_dict = AuthChangePasswordValidationError.from_dict(auth_change_password_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


