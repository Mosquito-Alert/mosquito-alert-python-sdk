# ObservationsPredictionCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ObservationsPredictionCreateError]**](ObservationsPredictionCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_prediction_create_validation_error import ObservationsPredictionCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsPredictionCreateValidationError from a JSON string
observations_prediction_create_validation_error_instance = ObservationsPredictionCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(ObservationsPredictionCreateValidationError.to_json())

# convert the object into a dict
observations_prediction_create_validation_error_dict = observations_prediction_create_validation_error_instance.to_dict()
# create an instance of ObservationsPredictionCreateValidationError from a dict
observations_prediction_create_validation_error_from_dict = ObservationsPredictionCreateValidationError.from_dict(observations_prediction_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


