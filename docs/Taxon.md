# Taxon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**common_name** | **str** |  | [optional] 
**rank** | **str** |  | 
**italicize** | **bool** | Display the name in italics when rendering. | [readonly] 
**is_relevant** | **bool** | Indicates if this taxon is relevant for the application. Will be shown first and will set task to conflict if final taxon is not this. | 

## Example

```python
from mosquito_alert.models.taxon import Taxon

# TODO update the JSON string below
json = "{}"
# create an instance of Taxon from a JSON string
taxon_instance = Taxon.from_json(json)
# print the JSON string representation of the object
print(Taxon.to_json())

# convert the object into a dict
taxon_dict = taxon_instance.to_dict()
# create an instance of Taxon from a dict
taxon_from_dict = Taxon.from_dict(taxon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


