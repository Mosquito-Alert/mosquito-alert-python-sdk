# ErrorResponse415


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[Error415]**](Error415.md) |  | 

## Example

```python
from mosquito_alert.models.error_response415 import ErrorResponse415

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse415 from a JSON string
error_response415_instance = ErrorResponse415.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse415.to_json())

# convert the object into a dict
error_response415_dict = error_response415_instance.to_dict()
# create an instance of ErrorResponse415 from a dict
error_response415_from_dict = ErrorResponse415.from_dict(error_response415_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


