# SimpleTaxon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**common_name** | **str** |  | [optional] 
**rank** | **str** |  | 
**italicize** | **bool** | Display the name in italics when rendering. | [readonly] 

## Example

```python
from mosquito_alert.models.simple_taxon import SimpleTaxon

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTaxon from a JSON string
simple_taxon_instance = SimpleTaxon.from_json(json)
# print the JSON string representation of the object
print(SimpleTaxon.to_json())

# convert the object into a dict
simple_taxon_dict = simple_taxon_instance.to_dict()
# create an instance of SimpleTaxon from a dict
simple_taxon_from_dict = SimpleTaxon.from_dict(simple_taxon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


