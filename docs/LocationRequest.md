# LocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Indicates how the location was obtained. Use &#39;Auto (GPS)&#39; if the location was automatically retrieved from the device&#39;s GPS, or &#39;Manual (User-selected)&#39; if the location was selected by the user on a map. | 
**point** | [**LocationPoint**](LocationPoint.md) |  | 

## Example

```python
from mosquito_alert.models.location_request import LocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LocationRequest from a JSON string
location_request_instance = LocationRequest.from_json(json)
# print the JSON string representation of the object
print(LocationRequest.to_json())

# convert the object into a dict
location_request_dict = location_request_instance.to_dict()
# create an instance of LocationRequest from a dict
location_request_from_dict = LocationRequest.from_dict(location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


