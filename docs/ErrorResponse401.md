# ErrorResponse401


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[Error401]**](Error401.md) |  | 

## Example

```python
from mosquito_alert.models.error_response401 import ErrorResponse401

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse401 from a JSON string
error_response401_instance = ErrorResponse401.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse401.to_json())

# convert the object into a dict
error_response401_dict = error_response401_instance.to_dict()
# create an instance of ErrorResponse401 from a dict
error_response401_from_dict = ErrorResponse401.from_dict(error_response401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


