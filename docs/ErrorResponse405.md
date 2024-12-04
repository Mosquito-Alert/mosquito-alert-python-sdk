# ErrorResponse405


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[Error405]**](Error405.md) |  | 

## Example

```python
from mosquito_alert.models.error_response405 import ErrorResponse405

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse405 from a JSON string
error_response405_instance = ErrorResponse405.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse405.to_json())

# convert the object into a dict
error_response405_dict = error_response405_instance.to_dict()
# create an instance of ErrorResponse405 from a dict
error_response405_from_dict = ErrorResponse405.from_dict(error_response405_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


