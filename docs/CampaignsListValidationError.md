# CampaignsListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[CampaignsListError]**](CampaignsListError.md) |  | 

## Example

```python
from mosquito_alert.models.campaigns_list_validation_error import CampaignsListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignsListValidationError from a JSON string
campaigns_list_validation_error_instance = CampaignsListValidationError.from_json(json)
# print the JSON string representation of the object
print(CampaignsListValidationError.to_json())

# convert the object into a dict
campaigns_list_validation_error_dict = campaigns_list_validation_error_instance.to_dict()
# create an instance of CampaignsListValidationError from a dict
campaigns_list_validation_error_from_dict = CampaignsListValidationError.from_dict(campaigns_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


