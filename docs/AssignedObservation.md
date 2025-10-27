# AssignedObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**short_id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | 
**created_at_local** | **datetime** | The date and time when the record was created, displayed without timezone field. | [readonly] 
**received_at** | **datetime** |  | [readonly] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**photos** | [**List[SimplePhoto]**](SimplePhoto.md) |  | [readonly] 
**user** | [**MinimalUser**](MinimalUser.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.assigned_observation import AssignedObservation

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedObservation from a JSON string
assigned_observation_instance = AssignedObservation.from_json(json)
# print the JSON string representation of the object
print(AssignedObservation.to_json())

# convert the object into a dict
assigned_observation_dict = assigned_observation_instance.to_dict()
# create an instance of AssignedObservation from a dict
assigned_observation_from_dict = AssignedObservation.from_dict(assigned_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


