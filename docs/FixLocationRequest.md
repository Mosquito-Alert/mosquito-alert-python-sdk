# FixLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude rounded down to nearest 0.025 decimal degree. | 
**longitude** | **float** | Longitude rounded down to nearest 0.025 decimal degree. | 

## Example

```python
from mosquito_alert_api.models.fix_location_request import FixLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FixLocationRequest from a JSON string
fix_location_request_instance = FixLocationRequest.from_json(json)
# print the JSON string representation of the object
print(FixLocationRequest.to_json())

# convert the object into a dict
fix_location_request_dict = fix_location_request_instance.to_dict()
# create an instance of FixLocationRequest from a dict
fix_location_request_from_dict = FixLocationRequest.from_dict(fix_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


