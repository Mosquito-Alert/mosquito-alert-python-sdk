# DevicesCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.devices_create_error import DevicesCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesCreateError from a JSON string
devices_create_error_instance = DevicesCreateError.from_json(json)
# print the JSON string representation of the object
print(DevicesCreateError.to_json())

# convert the object into a dict
devices_create_error_dict = devices_create_error_instance.to_dict()
# create an instance of DevicesCreateError from a dict
devices_create_error_from_dict = DevicesCreateError.from_dict(devices_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


