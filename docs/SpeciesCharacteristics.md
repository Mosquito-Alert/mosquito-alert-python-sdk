# SpeciesCharacteristics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sex** | **str** |  | 
**is_blood_fed** | **bool** |  | [optional] 
**is_gravid** | **bool** |  | [optional] 

## Example

```python
from mosquito_alert.models.species_characteristics import SpeciesCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of SpeciesCharacteristics from a JSON string
species_characteristics_instance = SpeciesCharacteristics.from_json(json)
# print the JSON string representation of the object
print(SpeciesCharacteristics.to_json())

# convert the object into a dict
species_characteristics_dict = species_characteristics_instance.to_dict()
# create an instance of SpeciesCharacteristics from a dict
species_characteristics_from_dict = SpeciesCharacteristics.from_dict(species_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


