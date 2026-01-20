# PaginatedCampaignList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Campaign]**](Campaign.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_campaign_list import PaginatedCampaignList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCampaignList from a JSON string
paginated_campaign_list_instance = PaginatedCampaignList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCampaignList.to_json())

# convert the object into a dict
paginated_campaign_list_dict = paginated_campaign_list_instance.to_dict()
# create an instance of PaginatedCampaignList from a dict
paginated_campaign_list_from_dict = PaginatedCampaignList.from_dict(paginated_campaign_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


