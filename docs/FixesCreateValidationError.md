# FixesCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[FixesCreateError]**](FixesCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.fixes_create_validation_error import FixesCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of FixesCreateValidationError from a JSON string
fixes_create_validation_error_instance = FixesCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(FixesCreateValidationError.to_json())

# convert the object into a dict
fixes_create_validation_error_dict = fixes_create_validation_error_instance.to_dict()
# create an instance of FixesCreateValidationError from a dict
fixes_create_validation_error_from_dict = FixesCreateValidationError.from_dict(fixes_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


