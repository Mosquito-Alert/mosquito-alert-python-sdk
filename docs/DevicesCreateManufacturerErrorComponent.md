# DevicesCreateManufacturerErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.devices_create_manufacturer_error_component import DevicesCreateManufacturerErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesCreateManufacturerErrorComponent from a JSON string
devices_create_manufacturer_error_component_instance = DevicesCreateManufacturerErrorComponent.from_json(json)
# print the JSON string representation of the object
print(DevicesCreateManufacturerErrorComponent.to_json())

# convert the object into a dict
devices_create_manufacturer_error_component_dict = devices_create_manufacturer_error_component_instance.to_dict()
# create an instance of DevicesCreateManufacturerErrorComponent from a dict
devices_create_manufacturer_error_component_from_dict = DevicesCreateManufacturerErrorComponent.from_dict(devices_create_manufacturer_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


