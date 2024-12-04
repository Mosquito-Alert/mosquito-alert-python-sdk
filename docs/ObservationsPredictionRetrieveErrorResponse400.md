# ObservationsPredictionRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_prediction_retrieve_error_response400 import ObservationsPredictionRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsPredictionRetrieveErrorResponse400 from a JSON string
observations_prediction_retrieve_error_response400_instance = ObservationsPredictionRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(ObservationsPredictionRetrieveErrorResponse400.to_json())

# convert the object into a dict
observations_prediction_retrieve_error_response400_dict = observations_prediction_retrieve_error_response400_instance.to_dict()
# create an instance of ObservationsPredictionRetrieveErrorResponse400 from a dict
observations_prediction_retrieve_error_response400_from_dict = ObservationsPredictionRetrieveErrorResponse400.from_dict(observations_prediction_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


