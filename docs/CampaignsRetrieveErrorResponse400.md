# CampaignsRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.campaigns_retrieve_error_response400 import CampaignsRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignsRetrieveErrorResponse400 from a JSON string
campaigns_retrieve_error_response400_instance = CampaignsRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(CampaignsRetrieveErrorResponse400.to_json())

# convert the object into a dict
campaigns_retrieve_error_response400_dict = campaigns_retrieve_error_response400_instance.to_dict()
# create an instance of CampaignsRetrieveErrorResponse400 from a dict
campaigns_retrieve_error_response400_from_dict = CampaignsRetrieveErrorResponse400.from_dict(campaigns_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


