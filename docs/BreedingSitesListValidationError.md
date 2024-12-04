# BreedingSitesListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BreedingSitesListError]**](BreedingSitesListError.md) |  | 

## Example

```python
from mosquito_alert.models.breeding_sites_list_validation_error import BreedingSitesListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSitesListValidationError from a JSON string
breeding_sites_list_validation_error_instance = BreedingSitesListValidationError.from_json(json)
# print the JSON string representation of the object
print(BreedingSitesListValidationError.to_json())

# convert the object into a dict
breeding_sites_list_validation_error_dict = breeding_sites_list_validation_error_instance.to_dict()
# create an instance of BreedingSitesListValidationError from a dict
breeding_sites_list_validation_error_from_dict = BreedingSitesListValidationError.from_dict(breeding_sites_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


