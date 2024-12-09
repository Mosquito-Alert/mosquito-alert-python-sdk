# AuthRefreshTokenRefreshErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_refresh_token_refresh_error_component import AuthRefreshTokenRefreshErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRefreshTokenRefreshErrorComponent from a JSON string
auth_refresh_token_refresh_error_component_instance = AuthRefreshTokenRefreshErrorComponent.from_json(json)
# print the JSON string representation of the object
print(AuthRefreshTokenRefreshErrorComponent.to_json())

# convert the object into a dict
auth_refresh_token_refresh_error_component_dict = auth_refresh_token_refresh_error_component_instance.to_dict()
# create an instance of AuthRefreshTokenRefreshErrorComponent from a dict
auth_refresh_token_refresh_error_component_from_dict = AuthRefreshTokenRefreshErrorComponent.from_dict(auth_refresh_token_refresh_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


