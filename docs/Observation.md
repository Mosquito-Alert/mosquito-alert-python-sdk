# Observation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**short_id** | **str** |  | [readonly] 
**user_uuid** | **str** |  | [readonly] 
**created_at** | **datetime** |  | 
**created_at_local** | **datetime** | The date and time when the record was created, displayed in the local timezone specified for this entry. | [readonly] 
**sent_at** | **datetime** |  | 
**received_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** | Date and time when the report was last modified | [readonly] 
**location** | [**ReportLocation**](ReportLocation.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**published** | **bool** |  | [readonly] 
**photos** | [**List[ReportPhoto]**](ReportPhoto.md) |  | 
**event_environment** | **str** | The environment where the event took place. | [optional] 
**event_moment** | **str** | The moment of the day when the event took place. | [optional] 
**user_perceived_mosquito_specie** | **str** | The mosquito specie perceived by the user. | [optional] 
**user_perceived_mosquito_thorax** | **str** | The species of mosquito that the thorax resembles, according to the user. | [optional] 
**user_perceived_mosquito_abdomen** | **str** | The species of mosquito that the abdomen resembles, according to the user. | [optional] 
**user_perceived_mosquito_legs** | **str** | The species of mosquito that the leg resembles, according to the user. | [optional] 

## Example

```python
from mosquito_alert.models.observation import Observation

# TODO update the JSON string below
json = "{}"
# create an instance of Observation from a JSON string
observation_instance = Observation.from_json(json)
# print the JSON string representation of the object
print(Observation.to_json())

# convert the object into a dict
observation_dict = observation_instance.to_dict()
# create an instance of Observation from a dict
observation_from_dict = Observation.from_dict(observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


