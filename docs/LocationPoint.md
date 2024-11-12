# LocationPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 

## Example

```python
from mosquito_alert.models.location_point import LocationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of LocationPoint from a JSON string
location_point_instance = LocationPoint.from_json(json)
# print the JSON string representation of the object
print(LocationPoint.to_json())

# convert the object into a dict
location_point_dict = location_point_instance.to_dict()
# create an instance of LocationPoint from a dict
location_point_from_dict = LocationPoint.from_dict(location_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


