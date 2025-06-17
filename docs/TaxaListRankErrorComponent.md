# TaxaListRankErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.taxa_list_rank_error_component import TaxaListRankErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TaxaListRankErrorComponent from a JSON string
taxa_list_rank_error_component_instance = TaxaListRankErrorComponent.from_json(json)
# print the JSON string representation of the object
print(TaxaListRankErrorComponent.to_json())

# convert the object into a dict
taxa_list_rank_error_component_dict = taxa_list_rank_error_component_instance.to_dict()
# create an instance of TaxaListRankErrorComponent from a dict
taxa_list_rank_error_component_from_dict = TaxaListRankErrorComponent.from_dict(taxa_list_rank_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


