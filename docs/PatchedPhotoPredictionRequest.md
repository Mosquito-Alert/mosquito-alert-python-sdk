# PatchedPhotoPredictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**BoundingBoxRequest**](BoundingBoxRequest.md) |  | [optional] 
**insect_confidence** | **float** | Insect confidence | [optional] 
**predicted_class** | **str** |  | [optional] 
**threshold_deviation** | **float** |  | [optional] 
**is_decisive** | **bool** | Indicates if this prediction can close the identification task. | [optional] 
**scores** | [**PredictionScoreRequest**](PredictionScoreRequest.md) |  | [optional] 
**classifier_version** | **str** |  | [optional] 

## Example

```python
from mosquito_alert.models.patched_photo_prediction_request import PatchedPhotoPredictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPhotoPredictionRequest from a JSON string
patched_photo_prediction_request_instance = PatchedPhotoPredictionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPhotoPredictionRequest.to_json())

# convert the object into a dict
patched_photo_prediction_request_dict = patched_photo_prediction_request_instance.to_dict()
# create an instance of PatchedPhotoPredictionRequest from a dict
patched_photo_prediction_request_from_dict = PatchedPhotoPredictionRequest.from_dict(patched_photo_prediction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


