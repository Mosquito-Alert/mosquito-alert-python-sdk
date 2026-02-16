# SpeciesClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon_id** | **int** |  | 
**confidence_label** | **str** |  | 

## Example

```python
from mosquito_alert.models.species_classification_request import SpeciesClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpeciesClassificationRequest from a JSON string
species_classification_request_instance = SpeciesClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(SpeciesClassificationRequest.to_json())

# convert the object into a dict
species_classification_request_dict = species_classification_request_instance.to_dict()
# create an instance of SpeciesClassificationRequest from a dict
species_classification_request_from_dict = SpeciesClassificationRequest.from_dict(species_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


