# FixesCreateErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.fixes_create_error_response400 import FixesCreateErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of FixesCreateErrorResponse400 from a JSON string
fixes_create_error_response400_instance = FixesCreateErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(FixesCreateErrorResponse400.to_json())

# convert the object into a dict
fixes_create_error_response400_dict = fixes_create_error_response400_instance.to_dict()
# create an instance of FixesCreateErrorResponse400 from a dict
fixes_create_error_response400_from_dict = FixesCreateErrorResponse400.from_dict(fixes_create_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


