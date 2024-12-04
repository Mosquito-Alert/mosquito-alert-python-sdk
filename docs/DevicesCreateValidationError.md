# DevicesCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[DevicesCreateError]**](DevicesCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.devices_create_validation_error import DevicesCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesCreateValidationError from a JSON string
devices_create_validation_error_instance = DevicesCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(DevicesCreateValidationError.to_json())

# convert the object into a dict
devices_create_validation_error_dict = devices_create_validation_error_instance.to_dict()
# create an instance of DevicesCreateValidationError from a dict
devices_create_validation_error_from_dict = DevicesCreateValidationError.from_dict(devices_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


