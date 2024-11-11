# ObservationPrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_photo_uuid** | **str** | The selected photo whose prediction represents the observation as the best classification result. | 
**insect_confidence** | **float** |  | [readonly] 
**predicted_class** | **str** |  | [readonly] 
**predicted_class_display** | **str** |  | [readonly] 
**is_executive_validation** | **bool** | Whether if the photo prediction will be used as an executive validation for the report. | [readonly] [default to False]
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert_api.models.observation_prediction import ObservationPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationPrediction from a JSON string
observation_prediction_instance = ObservationPrediction.from_json(json)
# print the JSON string representation of the object
print(ObservationPrediction.to_json())

# convert the object into a dict
observation_prediction_dict = observation_prediction_instance.to_dict()
# create an instance of ObservationPrediction from a dict
observation_prediction_from_dict = ObservationPrediction.from_dict(observation_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


