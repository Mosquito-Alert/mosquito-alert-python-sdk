# DevicesUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[DevicesUpdateError]**](DevicesUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.devices_update_validation_error import DevicesUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesUpdateValidationError from a JSON string
devices_update_validation_error_instance = DevicesUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(DevicesUpdateValidationError.to_json())

# convert the object into a dict
devices_update_validation_error_dict = devices_update_validation_error_instance.to_dict()
# create an instance of DevicesUpdateValidationError from a dict
devices_update_validation_error_from_dict = DevicesUpdateValidationError.from_dict(devices_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


