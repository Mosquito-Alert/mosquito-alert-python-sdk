# PaginatedBreedingSiteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[BreedingSite]**](BreedingSite.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.paginated_breeding_site_list import PaginatedBreedingSiteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBreedingSiteList from a JSON string
paginated_breeding_site_list_instance = PaginatedBreedingSiteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBreedingSiteList.to_json())

# convert the object into a dict
paginated_breeding_site_list_dict = paginated_breeding_site_list_instance.to_dict()
# create an instance of PaginatedBreedingSiteList from a dict
paginated_breeding_site_list_from_dict = PaginatedBreedingSiteList.from_dict(paginated_breeding_site_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


