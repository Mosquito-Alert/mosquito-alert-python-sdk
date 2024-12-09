# AuthObtainTokenValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[AuthObtainTokenError]**](AuthObtainTokenError.md) |  | 

## Example

```python
from mosquito_alert.models.auth_obtain_token_validation_error import AuthObtainTokenValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthObtainTokenValidationError from a JSON string
auth_obtain_token_validation_error_instance = AuthObtainTokenValidationError.from_json(json)
# print the JSON string representation of the object
print(AuthObtainTokenValidationError.to_json())

# convert the object into a dict
auth_obtain_token_validation_error_dict = auth_obtain_token_validation_error_instance.to_dict()
# create an instance of AuthObtainTokenValidationError from a dict
auth_obtain_token_validation_error_from_dict = AuthObtainTokenValidationError.from_dict(auth_obtain_token_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


