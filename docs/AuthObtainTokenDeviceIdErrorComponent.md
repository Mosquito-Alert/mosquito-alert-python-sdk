# AuthObtainTokenDeviceIdErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.auth_obtain_token_device_id_error_component import AuthObtainTokenDeviceIdErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthObtainTokenDeviceIdErrorComponent from a JSON string
auth_obtain_token_device_id_error_component_instance = AuthObtainTokenDeviceIdErrorComponent.from_json(json)
# print the JSON string representation of the object
print(AuthObtainTokenDeviceIdErrorComponent.to_json())

# convert the object into a dict
auth_obtain_token_device_id_error_component_dict = auth_obtain_token_device_id_error_component_instance.to_dict()
# create an instance of AuthObtainTokenDeviceIdErrorComponent from a dict
auth_obtain_token_device_id_error_component_from_dict = AuthObtainTokenDeviceIdErrorComponent.from_dict(auth_obtain_token_device_id_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


