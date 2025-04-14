# TaxaListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[TaxaListError]**](TaxaListError.md) |  | 

## Example

```python
from mosquito_alert.models.taxa_list_validation_error import TaxaListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of TaxaListValidationError from a JSON string
taxa_list_validation_error_instance = TaxaListValidationError.from_json(json)
# print the JSON string representation of the object
print(TaxaListValidationError.to_json())

# convert the object into a dict
taxa_list_validation_error_dict = taxa_list_validation_error_instance.to_dict()
# create an instance of TaxaListValidationError from a dict
taxa_list_validation_error_from_dict = TaxaListValidationError.from_dict(taxa_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


