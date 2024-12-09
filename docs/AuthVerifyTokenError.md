# AuthVerifyTokenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_verify_token_error import AuthVerifyTokenError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthVerifyTokenError from a JSON string
auth_verify_token_error_instance = AuthVerifyTokenError.from_json(json)
# print the JSON string representation of the object
print(AuthVerifyTokenError.to_json())

# convert the object into a dict
auth_verify_token_error_dict = auth_verify_token_error_instance.to_dict()
# create an instance of AuthVerifyTokenError from a dict
auth_verify_token_error_from_dict = AuthVerifyTokenError.from_dict(auth_verify_token_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


