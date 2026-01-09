# Observation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**short_id** | **str** |  | [readonly] 
**user_uuid** | **UUID** |  | [readonly] 
**created_at** | **datetime** |  | 
**created_at_local** | **datetime** | The date and time when the record was created, displayed without timezone field. | [readonly] 
**sent_at** | **datetime** |  | 
**received_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** | Date and time when the report was last modified | [readonly] 
**location** | [**Location**](Location.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**published** | **bool** |  | [readonly] 
**photos** | [**List[SimplePhoto]**](SimplePhoto.md) |  | [readonly] 
**identification** | [**Identification**](Identification.md) |  | [readonly] 
**event_environment** | **str** | The environment where the event took place. | [optional] 
**event_moment** | **str** | The moment of the day when the event took place. | [optional] 
**mosquito_appearance** | [**MosquitoAppearance**](MosquitoAppearance.md) | User-provided description of the mosquito&#39;s appearance | [optional] 

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


