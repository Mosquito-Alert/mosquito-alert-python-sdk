# PaginatedTaxonList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Taxon]**](Taxon.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.paginated_taxon_list import PaginatedTaxonList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTaxonList from a JSON string
paginated_taxon_list_instance = PaginatedTaxonList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTaxonList.to_json())

# convert the object into a dict
paginated_taxon_list_dict = paginated_taxon_list_instance.to_dict()
# create an instance of PaginatedTaxonList from a dict
paginated_taxon_list_from_dict = PaginatedTaxonList.from_dict(paginated_taxon_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


