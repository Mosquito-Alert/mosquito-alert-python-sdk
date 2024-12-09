# AuthRefreshTokenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_refresh_token_error import AuthRefreshTokenError

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRefreshTokenError from a JSON string
auth_refresh_token_error_instance = AuthRefreshTokenError.from_json(json)
# print the JSON string representation of the object
print(AuthRefreshTokenError.to_json())

# convert the object into a dict
auth_refresh_token_error_dict = auth_refresh_token_error_instance.to_dict()
# create an instance of AuthRefreshTokenError from a dict
auth_refresh_token_error_from_dict = AuthRefreshTokenError.from_dict(auth_refresh_token_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


