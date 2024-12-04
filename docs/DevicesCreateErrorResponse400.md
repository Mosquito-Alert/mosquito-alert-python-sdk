# DevicesCreateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.devices_create_error_response400 import DevicesCreateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesCreateErrorResponse400 from a JSON string
devices_create_error_response400_instance = DevicesCreateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(DevicesCreateErrorResponse400.to_json())

# convert the object into a dict
devices_create_error_response400_dict = devices_create_error_response400_instance.to_dict()
# create an instance of DevicesCreateErrorResponse400 from a dict
devices_create_error_response400_from_dict = DevicesCreateErrorResponse400.from_dict(devices_create_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


