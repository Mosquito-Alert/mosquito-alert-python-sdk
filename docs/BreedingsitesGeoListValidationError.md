# BreedingsitesGeoListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BreedingsitesGeoListError]**](BreedingsitesGeoListError.md) |  | 

## Example

```python
from mosquito_alert.models.breedingsites_geo_list_validation_error import BreedingsitesGeoListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingsitesGeoListValidationError from a JSON string
breedingsites_geo_list_validation_error_instance = BreedingsitesGeoListValidationError.from_json(json)
# print the JSON string representation of the object
print(BreedingsitesGeoListValidationError.to_json())

# convert the object into a dict
breedingsites_geo_list_validation_error_dict = breedingsites_geo_list_validation_error_instance.to_dict()
# create an instance of BreedingsitesGeoListValidationError from a dict
breedingsites_geo_list_validation_error_from_dict = BreedingsitesGeoListValidationError.from_dict(breedingsites_geo_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


