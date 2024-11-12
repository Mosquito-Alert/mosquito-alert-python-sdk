# PaginatedPartnerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Partner]**](Partner.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.paginated_partner_list import PaginatedPartnerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPartnerList from a JSON string
paginated_partner_list_instance = PaginatedPartnerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPartnerList.to_json())

# convert the object into a dict
paginated_partner_list_dict = paginated_partner_list_instance.to_dict()
# create an instance of PaginatedPartnerList from a dict
paginated_partner_list_from_dict = PaginatedPartnerList.from_dict(paginated_partner_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


