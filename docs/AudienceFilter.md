# AudienceFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_login_before** | **datetime** |  | [optional] 
**last_login_after** | **datetime** |  | [optional] 
**in_area** | **object** | Filter users whose last known location is within the specified area. The area should be provided as a GeoJSON geometry object. | [optional] 
**locale** | **str** |  | [optional] 
**notification_topics** | **List[str]** | Filter users subscribed to any of the provided notification topics. | [optional] 

## Example

```python
from mosquito_alert.models.audience_filter import AudienceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceFilter from a JSON string
audience_filter_instance = AudienceFilter.from_json(json)
# print the JSON string representation of the object
print(AudienceFilter.to_json())

# convert the object into a dict
audience_filter_dict = audience_filter_instance.to_dict()
# create an instance of AudienceFilter from a dict
audience_filter_from_dict = AudienceFilter.from_dict(audience_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


