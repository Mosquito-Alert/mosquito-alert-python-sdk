# ObservationPredictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_photo_uuid** | **str** | The selected photo whose prediction represents the observation as the best classification result. | 
**is_executive_validation** | **bool** | Whether if the photo prediction will be used as an executive validation for the report. | [optional] [default to False]

## Example

```python
from mosquito_alert_api.models.observation_prediction_request import ObservationPredictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationPredictionRequest from a JSON string
observation_prediction_request_instance = ObservationPredictionRequest.from_json(json)
# print the JSON string representation of the object
print(ObservationPredictionRequest.to_json())

# convert the object into a dict
observation_prediction_request_dict = observation_prediction_request_instance.to_dict()
# create an instance of ObservationPredictionRequest from a dict
observation_prediction_request_from_dict = ObservationPredictionRequest.from_dict(observation_prediction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


