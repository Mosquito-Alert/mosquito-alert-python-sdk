# SimplifiedLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | [**LocationPoint**](LocationPoint.md) |  | 
**timezone** | **str** |  | [readonly] 
**display_name** | **str** |  | [readonly] 
**country** | [**Country**](Country.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.simplified_location import SimplifiedLocation

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedLocation from a JSON string
simplified_location_instance = SimplifiedLocation.from_json(json)
# print the JSON string representation of the object
print(SimplifiedLocation.to_json())

# convert the object into a dict
simplified_location_dict = simplified_location_instance.to_dict()
# create an instance of SimplifiedLocation from a dict
simplified_location_from_dict = SimplifiedLocation.from_dict(simplified_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


