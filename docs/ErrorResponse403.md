# ErrorResponse403


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[Error403]**](Error403.md) |  | 

## Example

```python
from mosquito_alert.models.error_response403 import ErrorResponse403

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse403 from a JSON string
error_response403_instance = ErrorResponse403.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse403.to_json())

# convert the object into a dict
error_response403_dict = error_response403_instance.to_dict()
# create an instance of ErrorResponse403 from a dict
error_response403_from_dict = ErrorResponse403.from_dict(error_response403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


