# BreedingsitesCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.breedingsites_create_error import BreedingsitesCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingsitesCreateError from a JSON string
breedingsites_create_error_instance = BreedingsitesCreateError.from_json(json)
# print the JSON string representation of the object
print(BreedingsitesCreateError.to_json())

# convert the object into a dict
breedingsites_create_error_dict = breedingsites_create_error_instance.to_dict()
# create an instance of BreedingsitesCreateError from a dict
breedingsites_create_error_from_dict = BreedingsitesCreateError.from_dict(breedingsites_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


