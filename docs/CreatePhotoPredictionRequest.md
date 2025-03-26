# CreatePhotoPredictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photo_uuid** | **str** |  | 
**bbox** | [**BoundingBoxRequest**](BoundingBoxRequest.md) |  | 
**insect_confidence** | **float** | Insect confidence | 
**predicted_class** | **str** |  | 
**threshold_deviation** | **float** |  | 
**is_final_prediction** | **bool** | Indicates if this prediction can close the identification task. | [optional] 
**scores** | [**PredictionScoreRequest**](PredictionScoreRequest.md) |  | 
**classifier_version** | **str** |  | 

## Example

```python
from mosquito_alert.models.create_photo_prediction_request import CreatePhotoPredictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePhotoPredictionRequest from a JSON string
create_photo_prediction_request_instance = CreatePhotoPredictionRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePhotoPredictionRequest.to_json())

# convert the object into a dict
create_photo_prediction_request_dict = create_photo_prediction_request_instance.to_dict()
# create an instance of CreatePhotoPredictionRequest from a dict
create_photo_prediction_request_from_dict = CreatePhotoPredictionRequest.from_dict(create_photo_prediction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


