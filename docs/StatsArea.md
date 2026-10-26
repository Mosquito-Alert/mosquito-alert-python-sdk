# StatsArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Value to send as &#x60;?area&#x3D;&#x60;, e.g. \&quot;nuts2:34\&quot;. | 
**level** | **str** |  | 
**id** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 
**is_member** | **bool** | True if the user is a direct member of a workspace anchored on this area. | 
**children** | [**List[StatsArea]**](StatsArea.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.stats_area import StatsArea

# TODO update the JSON string below
json = "{}"
# create an instance of StatsArea from a JSON string
stats_area_instance = StatsArea.from_json(json)
# print the JSON string representation of the object
print(StatsArea.to_json())

# convert the object into a dict
stats_area_dict = stats_area_instance.to_dict()
# create an instance of StatsArea from a dict
stats_area_from_dict = StatsArea.from_dict(stats_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


