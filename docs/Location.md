# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Indicates how the location was obtained. Use &#39;Auto (GPS)&#39; if the location was automatically retrieved from the device&#39;s GPS, or &#39;Manual (User-selected)&#39; if the location was selected by the user on a map. | 
**point** | [**LocationPoint**](LocationPoint.md) |  | 
**timezone** | **str** |  | [readonly] 
**country_id** | **int** |  | [readonly] 
**adm_boundaries** | [**AdmBoundaries**](AdmBoundaries.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


