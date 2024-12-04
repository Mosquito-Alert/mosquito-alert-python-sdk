# DevicesRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.devices_retrieve_error_response400 import DevicesRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesRetrieveErrorResponse400 from a JSON string
devices_retrieve_error_response400_instance = DevicesRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(DevicesRetrieveErrorResponse400.to_json())

# convert the object into a dict
devices_retrieve_error_response400_dict = devices_retrieve_error_response400_instance.to_dict()
# create an instance of DevicesRetrieveErrorResponse400 from a dict
devices_retrieve_error_response400_from_dict = DevicesRetrieveErrorResponse400.from_dict(devices_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

