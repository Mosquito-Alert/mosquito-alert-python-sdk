# ErrorResponse406


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[Error406]**](Error406.md) |  | 

## Example

```python
from mosquito_alert.models.error_response406 import ErrorResponse406

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse406 from a JSON string
error_response406_instance = ErrorResponse406.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse406.to_json())

# convert the object into a dict
error_response406_dict = error_response406_instance.to_dict()
# create an instance of ErrorResponse406 from a dict
error_response406_from_dict = ErrorResponse406.from_dict(error_response406_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


