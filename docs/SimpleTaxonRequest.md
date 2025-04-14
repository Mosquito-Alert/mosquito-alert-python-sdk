# SimpleTaxonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**common_name** | **str** |  | [optional] 
**rank** | **str** |  | 

## Example

```python
from mosquito_alert.models.simple_taxon_request import SimpleTaxonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTaxonRequest from a JSON string
simple_taxon_request_instance = SimpleTaxonRequest.from_json(json)
# print the JSON string representation of the object
print(SimpleTaxonRequest.to_json())

# convert the object into a dict
simple_taxon_request_dict = simple_taxon_request_instance.to_dict()
# create an instance of SimpleTaxonRequest from a dict
simple_taxon_request_from_dict = SimpleTaxonRequest.from_dict(simple_taxon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


