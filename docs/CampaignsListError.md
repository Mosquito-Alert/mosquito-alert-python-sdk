# CampaignsListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.campaigns_list_error import CampaignsListError

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignsListError from a JSON string
campaigns_list_error_instance = CampaignsListError.from_json(json)
# print the JSON string representation of the object
print(CampaignsListError.to_json())

# convert the object into a dict
campaigns_list_error_dict = campaigns_list_error_instance.to_dict()
# create an instance of CampaignsListError from a dict
campaigns_list_error_from_dict = CampaignsListError.from_dict(campaigns_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


