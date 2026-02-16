# SpeciesCharacteristicsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sex** | **str** |  | 
**is_blood_fed** | **bool** |  | [optional] 
**is_gravid** | **bool** |  | [optional] 

## Example

```python
from mosquito_alert.models.species_characteristics_request import SpeciesCharacteristicsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpeciesCharacteristicsRequest from a JSON string
species_characteristics_request_instance = SpeciesCharacteristicsRequest.from_json(json)
# print the JSON string representation of the object
print(SpeciesCharacteristicsRequest.to_json())

# convert the object into a dict
species_characteristics_request_dict = species_characteristics_request_instance.to_dict()
# create an instance of SpeciesCharacteristicsRequest from a dict
species_characteristics_request_from_dict = SpeciesCharacteristicsRequest.from_dict(species_characteristics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


