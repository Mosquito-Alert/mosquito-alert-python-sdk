# DevicesPartialUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[DevicesPartialUpdateError]**](DevicesPartialUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.devices_partial_update_validation_error import DevicesPartialUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesPartialUpdateValidationError from a JSON string
devices_partial_update_validation_error_instance = DevicesPartialUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(DevicesPartialUpdateValidationError.to_json())

# convert the object into a dict
devices_partial_update_validation_error_dict = devices_partial_update_validation_error_instance.to_dict()
# create an instance of DevicesPartialUpdateValidationError from a dict
devices_partial_update_validation_error_from_dict = DevicesPartialUpdateValidationError.from_dict(devices_partial_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


