# BitesCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BitesCreateError]**](BitesCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.bites_create_validation_error import BitesCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesCreateValidationError from a JSON string
bites_create_validation_error_instance = BitesCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(BitesCreateValidationError.to_json())

# convert the object into a dict
bites_create_validation_error_dict = bites_create_validation_error_instance.to_dict()
# create an instance of BitesCreateValidationError from a dict
bites_create_validation_error_from_dict = BitesCreateValidationError.from_dict(bites_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


