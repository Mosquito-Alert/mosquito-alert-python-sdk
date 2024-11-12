# Campaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**country_id** | **int** | Country in which the campaign is taking place | [readonly] 
**posting_address** | **str** | Full posting address of the place where the samples will be sent | 
**start_date** | **datetime** | Date when the campaign starts. No samples should be collected BEFORE this date. | 
**end_date** | **datetime** | Date when the campaign ends. No samples should be collected AFTER this date. | 

## Example

```python
from mosquito_alert.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


