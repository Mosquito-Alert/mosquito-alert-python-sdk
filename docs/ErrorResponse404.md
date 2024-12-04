# ErrorResponse404


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[Error404]**](Error404.md) |  | 

## Example

```python
from mosquito_alert.models.error_response404 import ErrorResponse404

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse404 from a JSON string
error_response404_instance = ErrorResponse404.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse404.to_json())

# convert the object into a dict
error_response404_dict = error_response404_instance.to_dict()
# create an instance of ErrorResponse404 from a dict
error_response404_from_dict = ErrorResponse404.from_dict(error_response404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


