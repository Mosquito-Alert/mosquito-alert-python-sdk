# LocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Did user indicate that report relates to current location of phone (&#39;current&#39;) or to a location selected manually on the map (&#39;selected&#39;)? Or is the choice missing (&#39;missing&#39;) | 
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


