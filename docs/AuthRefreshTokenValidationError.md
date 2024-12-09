# AuthRefreshTokenValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[AuthRefreshTokenError]**](AuthRefreshTokenError.md) |  | 

## Example

```python
from mosquito_alert.models.auth_refresh_token_validation_error import AuthRefreshTokenValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRefreshTokenValidationError from a JSON string
auth_refresh_token_validation_error_instance = AuthRefreshTokenValidationError.from_json(json)
# print the JSON string representation of the object
print(AuthRefreshTokenValidationError.to_json())

# convert the object into a dict
auth_refresh_token_validation_error_dict = auth_refresh_token_validation_error_instance.to_dict()
# create an instance of AuthRefreshTokenValidationError from a dict
auth_refresh_token_validation_error_from_dict = AuthRefreshTokenValidationError.from_dict(auth_refresh_token_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


