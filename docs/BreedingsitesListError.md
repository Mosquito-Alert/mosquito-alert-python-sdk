# BreedingsitesListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.breedingsites_list_error import BreedingsitesListError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingsitesListError from a JSON string
breedingsites_list_error_instance = BreedingsitesListError.from_json(json)
# print the JSON string representation of the object
print(BreedingsitesListError.to_json())

# convert the object into a dict
breedingsites_list_error_dict = breedingsites_list_error_instance.to_dict()
# create an instance of BreedingsitesListError from a dict
breedingsites_list_error_from_dict = BreedingsitesListError.from_dict(breedingsites_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


