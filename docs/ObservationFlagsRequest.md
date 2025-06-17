# ObservationFlagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_favourite** | **bool** |  | [optional] [default to False]
**is_visible** | **bool** |  | [optional] [default to True]

## Example

```python
from mosquito_alert.models.observation_flags_request import ObservationFlagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationFlagsRequest from a JSON string
observation_flags_request_instance = ObservationFlagsRequest.from_json(json)
# print the JSON string representation of the object
print(ObservationFlagsRequest.to_json())

# convert the object into a dict
observation_flags_request_dict = observation_flags_request_instance.to_dict()
# create an instance of ObservationFlagsRequest from a dict
observation_flags_request_from_dict = ObservationFlagsRequest.from_dict(observation_flags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


