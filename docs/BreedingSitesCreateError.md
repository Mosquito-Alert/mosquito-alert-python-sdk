# BreedingSitesCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.breeding_sites_create_error import BreedingSitesCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSitesCreateError from a JSON string
breeding_sites_create_error_instance = BreedingSitesCreateError.from_json(json)
# print the JSON string representation of the object
print(BreedingSitesCreateError.to_json())

# convert the object into a dict
breeding_sites_create_error_dict = breeding_sites_create_error_instance.to_dict()
# create an instance of BreedingSitesCreateError from a dict
breeding_sites_create_error_from_dict = BreedingSitesCreateError.from_dict(breeding_sites_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


