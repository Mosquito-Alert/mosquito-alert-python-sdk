# SimplifiedObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**user_uuid** | **str** |  | [readonly] 
**created_at** | **datetime** |  | 
**created_at_local** | **datetime** | The date and time when the record was created, displayed in the local timezone specified for this entry. | [readonly] 
**received_at** | **datetime** |  | [readonly] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 

## Example

```python
from mosquito_alert.models.simplified_observation import SimplifiedObservation

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedObservation from a JSON string
simplified_observation_instance = SimplifiedObservation.from_json(json)
# print the JSON string representation of the object
print(SimplifiedObservation.to_json())

# convert the object into a dict
simplified_observation_dict = simplified_observation_instance.to_dict()
# create an instance of SimplifiedObservation from a dict
simplified_observation_from_dict = SimplifiedObservation.from_dict(simplified_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


