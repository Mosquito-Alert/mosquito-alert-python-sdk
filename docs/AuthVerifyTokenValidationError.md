# AuthVerifyTokenValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[AuthVerifyTokenError]**](AuthVerifyTokenError.md) |  | 

## Example

```python
from mosquito_alert.models.auth_verify_token_validation_error import AuthVerifyTokenValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthVerifyTokenValidationError from a JSON string
auth_verify_token_validation_error_instance = AuthVerifyTokenValidationError.from_json(json)
# print the JSON string representation of the object
print(AuthVerifyTokenValidationError.to_json())

# convert the object into a dict
auth_verify_token_validation_error_dict = auth_verify_token_validation_error_instance.to_dict()
# create an instance of AuthVerifyTokenValidationError from a dict
auth_verify_token_validation_error_from_dict = AuthVerifyTokenValidationError.from_dict(auth_verify_token_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


