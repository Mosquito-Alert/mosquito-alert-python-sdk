# TaxonTreeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**common_name** | **str** |  | [optional] 
**rank** | **str** |  | 
**italicize** | **bool** | Display the name in italics when rendering. | [readonly] 
**is_relevant** | **bool** | Indicates if this taxon is relevant for the application. Will be shown first and will set task to conflict if final taxon is not this. | 
**children** | [**List[TaxonTreeNode]**](TaxonTreeNode.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.taxon_tree_node import TaxonTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonTreeNode from a JSON string
taxon_tree_node_instance = TaxonTreeNode.from_json(json)
# print the JSON string representation of the object
print(TaxonTreeNode.to_json())

# convert the object into a dict
taxon_tree_node_dict = taxon_tree_node_instance.to_dict()
# create an instance of TaxonTreeNode from a dict
taxon_tree_node_from_dict = TaxonTreeNode.from_dict(taxon_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


