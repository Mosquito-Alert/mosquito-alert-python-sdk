# AuthObtainTokenPasswordErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_obtain_token_password_error_component import AuthObtainTokenPasswordErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthObtainTokenPasswordErrorComponent from a JSON string
auth_obtain_token_password_error_component_instance = AuthObtainTokenPasswordErrorComponent.from_json(json)
# print the JSON string representation of the object
print(AuthObtainTokenPasswordErrorComponent.to_json())

# convert the object into a dict
auth_obtain_token_password_error_component_dict = auth_obtain_token_password_error_component_instance.to_dict()
# create an instance of AuthObtainTokenPasswordErrorComponent from a dict
auth_obtain_token_password_error_component_from_dict = AuthObtainTokenPasswordErrorComponent.from_dict(auth_obtain_token_password_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


