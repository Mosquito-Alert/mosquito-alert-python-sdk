# BreedingSiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**sent_at** | **datetime** |  | 
**location** | [**ReportLocationRequest**](ReportLocationRequest.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**package** | [**PackageRequest**](PackageRequest.md) |  | [optional] 
**device** | [**DeviceRequest**](DeviceRequest.md) |  | [optional] 
**photos** | [**List[ReportPhotoRequest]**](ReportPhotoRequest.md) |  | 
**site_type** | **str** | Breeding site type. | [optional] 
**has_water** | **bool** | Either if the user perceived water in the breeding site. | [optional] 
**in_public_area** | **bool** | Either if the breeding site is found in a public area. | [optional] 
**has_near_mosquitoes** | **bool** | Either if the user perceived mosquitoes near the breeding site (less than 10 meters). | [optional] 
**has_larvae** | **bool** | Either if the user perceived larvaes the breeding site. | [optional] 

## Example

```python
from mosquito_alert_api.models.breeding_site_request import BreedingSiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSiteRequest from a JSON string
breeding_site_request_instance = BreedingSiteRequest.from_json(json)
# print the JSON string representation of the object
print(BreedingSiteRequest.to_json())

# convert the object into a dict
breeding_site_request_dict = breeding_site_request_instance.to_dict()
# create an instance of BreedingSiteRequest from a dict
breeding_site_request_from_dict = BreedingSiteRequest.from_dict(breeding_site_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


