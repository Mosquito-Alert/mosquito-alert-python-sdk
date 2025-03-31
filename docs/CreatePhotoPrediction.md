# CreatePhotoPrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photo** | [**SimplePhoto**](SimplePhoto.md) |  | [readonly] 
**bbox** | [**BoundingBox**](BoundingBox.md) |  | 
**insect_confidence** | **float** | Insect confidence | 
**predicted_class** | **str** |  | 
**threshold_deviation** | **float** |  | 
**is_decisive** | **bool** | Indicates if this prediction can close the identification task. | [optional] 
**scores** | [**PredictionScore**](PredictionScore.md) |  | 
**classifier_version** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.create_photo_prediction import CreatePhotoPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePhotoPrediction from a JSON string
create_photo_prediction_instance = CreatePhotoPrediction.from_json(json)
# print the JSON string representation of the object
print(CreatePhotoPrediction.to_json())

# convert the object into a dict
create_photo_prediction_dict = create_photo_prediction_instance.to_dict()
# create an instance of CreatePhotoPrediction from a dict
create_photo_prediction_from_dict = CreatePhotoPrediction.from_dict(create_photo_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


