# BitesListErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.bites_list_error_response400 import BitesListErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of BitesListErrorResponse400 from a JSON string
bites_list_error_response400_instance = BitesListErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(BitesListErrorResponse400.to_json())

# convert the object into a dict
bites_list_error_response400_dict = bites_list_error_response400_instance.to_dict()
# create an instance of BitesListErrorResponse400 from a dict
bites_list_error_response400_from_dict = BitesListErrorResponse400.from_dict(bites_list_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


