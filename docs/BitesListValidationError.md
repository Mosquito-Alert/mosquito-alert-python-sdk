# BitesListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BitesListError]**](BitesListError.md) |  | 

## Example

```python
from mosquito_alert.models.bites_list_validation_error import BitesListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesListValidationError from a JSON string
bites_list_validation_error_instance = BitesListValidationError.from_json(json)
# print the JSON string representation of the object
print(BitesListValidationError.to_json())

# convert the object into a dict
bites_list_validation_error_dict = bites_list_validation_error_instance.to_dict()
# create an instance of BitesListValidationError from a dict
bites_list_validation_error_from_dict = BitesListValidationError.from_dict(bites_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


