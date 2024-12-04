# DevicesCreateDeviceIdErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.devices_create_device_id_error_component import DevicesCreateDeviceIdErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesCreateDeviceIdErrorComponent from a JSON string
devices_create_device_id_error_component_instance = DevicesCreateDeviceIdErrorComponent.from_json(json)
# print the JSON string representation of the object
print(DevicesCreateDeviceIdErrorComponent.to_json())

# convert the object into a dict
devices_create_device_id_error_component_dict = devices_create_device_id_error_component_instance.to_dict()
# create an instance of DevicesCreateDeviceIdErrorComponent from a dict
devices_create_device_id_error_component_from_dict = DevicesCreateDeviceIdErrorComponent.from_dict(devices_create_device_id_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


