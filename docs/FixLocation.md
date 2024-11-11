# FixLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude rounded down to nearest 0.025 decimal degree. | 
**longitude** | **float** | Longitude rounded down to nearest 0.025 decimal degree. | 

## Example

```python
from mosquito_alert_api.models.fix_location import FixLocation

# TODO update the JSON string below
json = "{}"
# create an instance of FixLocation from a JSON string
fix_location_instance = FixLocation.from_json(json)
# print the JSON string representation of the object
print(FixLocation.to_json())

# convert the object into a dict
fix_location_dict = fix_location_instance.to_dict()
# create an instance of FixLocation from a dict
fix_location_from_dict = FixLocation.from_dict(fix_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


