# ObservationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**sent_at** | **datetime** |  | 
**location** | [**LocationRequest**](LocationRequest.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**package** | [**PackageRequest**](PackageRequest.md) |  | [optional] 
**device** | [**DeviceRequest**](DeviceRequest.md) |  | [optional] 
**photos** | [**List[SimplePhotoRequest]**](SimplePhotoRequest.md) |  | 
**event_environment** | **str** | The environment where the event took place. | [optional] 
**event_moment** | **str** | The moment of the day when the event took place. | [optional] 
**user_perceived_mosquito_specie** | **str** | The mosquito specie perceived by the user. | [optional] 
**user_perceived_mosquito_thorax** | **str** | The species of mosquito that the thorax resembles, according to the user. | [optional] 
**user_perceived_mosquito_abdomen** | **str** | The species of mosquito that the abdomen resembles, according to the user. | [optional] 
**user_perceived_mosquito_legs** | **str** | The species of mosquito that the leg resembles, according to the user. | [optional] 

## Example

```python
from mosquito_alert.models.observation_request import ObservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationRequest from a JSON string
observation_request_instance = ObservationRequest.from_json(json)
# print the JSON string representation of the object
print(ObservationRequest.to_json())

# convert the object into a dict
observation_request_dict = observation_request_instance.to_dict()
# create an instance of ObservationRequest from a dict
observation_request_from_dict = ObservationRequest.from_dict(observation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


