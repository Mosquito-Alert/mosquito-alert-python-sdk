# DevicesPartialUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.devices_partial_update_error import DevicesPartialUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesPartialUpdateError from a JSON string
devices_partial_update_error_instance = DevicesPartialUpdateError.from_json(json)
# print the JSON string representation of the object
print(DevicesPartialUpdateError.to_json())

# convert the object into a dict
devices_partial_update_error_dict = devices_partial_update_error_instance.to_dict()
# create an instance of DevicesPartialUpdateError from a dict
devices_partial_update_error_from_dict = DevicesPartialUpdateError.from_dict(devices_partial_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


