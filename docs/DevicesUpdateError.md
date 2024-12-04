# DevicesUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.devices_update_error import DevicesUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesUpdateError from a JSON string
devices_update_error_instance = DevicesUpdateError.from_json(json)
# print the JSON string representation of the object
print(DevicesUpdateError.to_json())

# convert the object into a dict
devices_update_error_dict = devices_update_error_instance.to_dict()
# create an instance of DevicesUpdateError from a dict
devices_update_error_from_dict = DevicesUpdateError.from_dict(devices_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


