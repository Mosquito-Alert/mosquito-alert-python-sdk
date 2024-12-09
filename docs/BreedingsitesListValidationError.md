# BreedingsitesListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BreedingsitesListError]**](BreedingsitesListError.md) |  | 

## Example

```python
from mosquito_alert.models.breedingsites_list_validation_error import BreedingsitesListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingsitesListValidationError from a JSON string
breedingsites_list_validation_error_instance = BreedingsitesListValidationError.from_json(json)
# print the JSON string representation of the object
print(BreedingsitesListValidationError.to_json())

# convert the object into a dict
breedingsites_list_validation_error_dict = breedingsites_list_validation_error_instance.to_dict()
# create an instance of BreedingsitesListValidationError from a dict
breedingsites_list_validation_error_from_dict = BreedingsitesListValidationError.from_dict(breedingsites_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


