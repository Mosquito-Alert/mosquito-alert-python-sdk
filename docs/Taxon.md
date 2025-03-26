# Taxon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**common_name** | **str** |  | [optional] 
**rank** | **str** |  | 

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


