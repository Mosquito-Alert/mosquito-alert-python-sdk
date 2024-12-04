# BitesCreateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.bites_create_error_response400 import BitesCreateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of BitesCreateErrorResponse400 from a JSON string
bites_create_error_response400_instance = BitesCreateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(BitesCreateErrorResponse400.to_json())

# convert the object into a dict
bites_create_error_response400_dict = bites_create_error_response400_instance.to_dict()
# create an instance of BitesCreateErrorResponse400 from a dict
bites_create_error_response400_from_dict = BitesCreateErrorResponse400.from_dict(bites_create_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


