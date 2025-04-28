# PaginatedCountryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Country]**](Country.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.paginated_country_list import PaginatedCountryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCountryList from a JSON string
paginated_country_list_instance = PaginatedCountryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCountryList.to_json())

# convert the object into a dict
paginated_country_list_dict = paginated_country_list_instance.to_dict()
# create an instance of PaginatedCountryList from a dict
paginated_country_list_from_dict = PaginatedCountryList.from_dict(paginated_country_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


