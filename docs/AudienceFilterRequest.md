# AudienceFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_login_before** | **datetime** |  | [optional] 
**last_login_after** | **datetime** |  | [optional] 
**in_area** | **object** | Filter users whose last known location is within the specified area. The area should be provided as a GeoJSON geometry object. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from mosquito_alert.models.audience_filter_request import AudienceFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceFilterRequest from a JSON string
audience_filter_request_instance = AudienceFilterRequest.from_json(json)
# print the JSON string representation of the object
print(AudienceFilterRequest.to_json())

# convert the object into a dict
audience_filter_request_dict = audience_filter_request_instance.to_dict()
# create an instance of AudienceFilterRequest from a dict
audience_filter_request_from_dict = AudienceFilterRequest.from_dict(audience_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


