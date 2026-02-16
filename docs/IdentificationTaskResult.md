# IdentificationTaskResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [readonly] 
**taxon** | [**SimpleTaxon**](SimpleTaxon.md) |  | [readonly] 
**is_high_confidence** | **bool** |  | [readonly] 
**confidence** | **float** |  | [readonly] 
**confidence_label** | **str** |  | [readonly] 
**uncertainty** | **float** |  | [readonly] 
**agreement** | **float** |  | [readonly] 
**characteristics** | [**SpeciesCharacteristics**](SpeciesCharacteristics.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.identification_task_result import IdentificationTaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTaskResult from a JSON string
identification_task_result_instance = IdentificationTaskResult.from_json(json)
# print the JSON string representation of the object
print(IdentificationTaskResult.to_json())

# convert the object into a dict
identification_task_result_dict = identification_task_result_instance.to_dict()
# create an instance of IdentificationTaskResult from a dict
identification_task_result_from_dict = IdentificationTaskResult.from_dict(identification_task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


