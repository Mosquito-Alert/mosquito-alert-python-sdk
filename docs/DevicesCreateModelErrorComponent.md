# DevicesCreateModelErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.devices_create_model_error_component import DevicesCreateModelErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesCreateModelErrorComponent from a JSON string
devices_create_model_error_component_instance = DevicesCreateModelErrorComponent.from_json(json)
# print the JSON string representation of the object
print(DevicesCreateModelErrorComponent.to_json())

# convert the object into a dict
devices_create_model_error_component_dict = devices_create_model_error_component_instance.to_dict()
# create an instance of DevicesCreateModelErrorComponent from a dict
devices_create_model_error_component_from_dict = DevicesCreateModelErrorComponent.from_dict(devices_create_model_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


