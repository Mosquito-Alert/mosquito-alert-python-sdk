# PhotoPredictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**BoundingBoxRequest**](BoundingBoxRequest.md) |  | 
**insect_confidence** | **float** | Insect confidence | 
**predicted_class** | **str** |  | [optional] 
**threshold_deviation** | **float** |  | 
**scores** | [**PredictionScoreRequest**](PredictionScoreRequest.md) |  | 
**classifier_version** | **str** |  | 

## Example

```python
from mosquito_alert.models.photo_prediction_request import PhotoPredictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PhotoPredictionRequest from a JSON string
photo_prediction_request_instance = PhotoPredictionRequest.from_json(json)
# print the JSON string representation of the object
print(PhotoPredictionRequest.to_json())

# convert the object into a dict
photo_prediction_request_dict = photo_prediction_request_instance.to_dict()
# create an instance of PhotoPredictionRequest from a dict
photo_prediction_request_from_dict = PhotoPredictionRequest.from_dict(photo_prediction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


