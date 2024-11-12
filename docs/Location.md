# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Did user indicate that report relates to current location of phone (&#39;current&#39;) or to a location selected manually on the map (&#39;selected&#39;)? Or is the choice missing (&#39;missing&#39;) | 
**point** | [**LocationPoint**](LocationPoint.md) |  | 
**timezone** | **str** |  | [readonly] 
**country_id** | **int** |  | [readonly] 
**nuts_2** | **str** |  | [readonly] 
**nuts_3** | **str** |  | [readonly] 

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


