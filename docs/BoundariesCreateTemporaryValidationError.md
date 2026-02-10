# BoundariesCreateTemporaryValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BoundariesCreateTemporaryError]**](BoundariesCreateTemporaryError.md) |  | 

## Example

```python
from mosquito_alert.models.boundaries_create_temporary_validation_error import BoundariesCreateTemporaryValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BoundariesCreateTemporaryValidationError from a JSON string
boundaries_create_temporary_validation_error_instance = BoundariesCreateTemporaryValidationError.from_json(json)
# print the JSON string representation of the object
print(BoundariesCreateTemporaryValidationError.to_json())

# convert the object into a dict
boundaries_create_temporary_validation_error_dict = boundaries_create_temporary_validation_error_instance.to_dict()
# create an instance of BoundariesCreateTemporaryValidationError from a dict
boundaries_create_temporary_validation_error_from_dict = BoundariesCreateTemporaryValidationError.from_dict(boundaries_create_temporary_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


