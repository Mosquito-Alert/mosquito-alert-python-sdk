# SpeciesClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | [**SimpleTaxon**](SimpleTaxon.md) |  | [readonly] 
**confidence** | **float** |  | [readonly] 
**confidence_label** | **str** |  | 
**is_high_confidence** | **bool** |  | [readonly] 

## Example

```python
from mosquito_alert.models.species_classification import SpeciesClassification

# TODO update the JSON string below
json = "{}"
# create an instance of SpeciesClassification from a JSON string
species_classification_instance = SpeciesClassification.from_json(json)
# print the JSON string representation of the object
print(SpeciesClassification.to_json())

# convert the object into a dict
species_classification_dict = species_classification_instance.to_dict()
# create an instance of SpeciesClassification from a dict
species_classification_from_dict = SpeciesClassification.from_dict(species_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


