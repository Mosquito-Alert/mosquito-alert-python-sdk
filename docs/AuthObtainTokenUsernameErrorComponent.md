# AuthObtainTokenUsernameErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_obtain_token_username_error_component import AuthObtainTokenUsernameErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthObtainTokenUsernameErrorComponent from a JSON string
auth_obtain_token_username_error_component_instance = AuthObtainTokenUsernameErrorComponent.from_json(json)
# print the JSON string representation of the object
print(AuthObtainTokenUsernameErrorComponent.to_json())

# convert the object into a dict
auth_obtain_token_username_error_component_dict = auth_obtain_token_username_error_component_instance.to_dict()
# create an instance of AuthObtainTokenUsernameErrorComponent from a dict
auth_obtain_token_username_error_component_from_dict = AuthObtainTokenUsernameErrorComponent.from_dict(auth_obtain_token_username_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


