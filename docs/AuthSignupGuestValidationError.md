# AuthSignupGuestValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[AuthSignupGuestError]**](AuthSignupGuestError.md) |  | 

## Example

```python
from mosquito_alert.models.auth_signup_guest_validation_error import AuthSignupGuestValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSignupGuestValidationError from a JSON string
auth_signup_guest_validation_error_instance = AuthSignupGuestValidationError.from_json(json)
# print the JSON string representation of the object
print(AuthSignupGuestValidationError.to_json())

# convert the object into a dict
auth_signup_guest_validation_error_dict = auth_signup_guest_validation_error_instance.to_dict()
# create an instance of AuthSignupGuestValidationError from a dict
auth_signup_guest_validation_error_from_dict = AuthSignupGuestValidationError.from_dict(auth_signup_guest_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


