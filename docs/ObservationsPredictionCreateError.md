# ObservationsPredictionCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.observations_prediction_create_error import ObservationsPredictionCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsPredictionCreateError from a JSON string
observations_prediction_create_error_instance = ObservationsPredictionCreateError.from_json(json)
# print the JSON string representation of the object
print(ObservationsPredictionCreateError.to_json())

# convert the object into a dict
observations_prediction_create_error_dict = observations_prediction_create_error_instance.to_dict()
# create an instance of ObservationsPredictionCreateError from a dict
observations_prediction_create_error_from_dict = ObservationsPredictionCreateError.from_dict(observations_prediction_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


