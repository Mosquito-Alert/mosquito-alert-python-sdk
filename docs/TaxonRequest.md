# TaxonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**common_name** | **str** |  | [optional] 
**rank** | **str** |  | 

## Example

```python
from mosquito_alert.models.taxon_request import TaxonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonRequest from a JSON string
taxon_request_instance = TaxonRequest.from_json(json)
# print the JSON string representation of the object
print(TaxonRequest.to_json())

# convert the object into a dict
taxon_request_dict = taxon_request_instance.to_dict()
# create an instance of TaxonRequest from a dict
taxon_request_from_dict = TaxonRequest.from_dict(taxon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


