# ObservationFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_favourite** | **bool** |  | [readonly] [default to False]
**is_visible** | **bool** |  | [readonly] [default to True]

## Example

```python
from mosquito_alert.models.observation_flags import ObservationFlags

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationFlags from a JSON string
observation_flags_instance = ObservationFlags.from_json(json)
# print the JSON string representation of the object
print(ObservationFlags.to_json())

# convert the object into a dict
observation_flags_dict = observation_flags_instance.to_dict()
# create an instance of ObservationFlags from a dict
observation_flags_from_dict = ObservationFlags.from_dict(observation_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


