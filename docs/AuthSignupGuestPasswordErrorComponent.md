# AuthSignupGuestPasswordErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_signup_guest_password_error_component import AuthSignupGuestPasswordErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSignupGuestPasswordErrorComponent from a JSON string
auth_signup_guest_password_error_component_instance = AuthSignupGuestPasswordErrorComponent.from_json(json)
# print the JSON string representation of the object
print(AuthSignupGuestPasswordErrorComponent.to_json())

# convert the object into a dict
auth_signup_guest_password_error_component_dict = auth_signup_guest_password_error_component_instance.to_dict()
# create an instance of AuthSignupGuestPasswordErrorComponent from a dict
auth_signup_guest_password_error_component_from_dict = AuthSignupGuestPasswordErrorComponent.from_dict(auth_signup_guest_password_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


