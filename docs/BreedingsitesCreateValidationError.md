# BreedingsitesCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BreedingsitesCreateError]**](BreedingsitesCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.breedingsites_create_validation_error import BreedingsitesCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingsitesCreateValidationError from a JSON string
breedingsites_create_validation_error_instance = BreedingsitesCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(BreedingsitesCreateValidationError.to_json())

# convert the object into a dict
breedingsites_create_validation_error_dict = breedingsites_create_validation_error_instance.to_dict()
# create an instance of BreedingsitesCreateValidationError from a dict
breedingsites_create_validation_error_from_dict = BreedingsitesCreateValidationError.from_dict(breedingsites_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


