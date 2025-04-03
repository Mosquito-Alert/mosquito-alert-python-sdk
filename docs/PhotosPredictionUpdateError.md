# PhotosPredictionUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.photos_prediction_update_error import PhotosPredictionUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosPredictionUpdateError from a JSON string
photos_prediction_update_error_instance = PhotosPredictionUpdateError.from_json(json)
# print the JSON string representation of the object
print(PhotosPredictionUpdateError.to_json())

# convert the object into a dict
photos_prediction_update_error_dict = photos_prediction_update_error_instance.to_dict()
# create an instance of PhotosPredictionUpdateError from a dict
photos_prediction_update_error_from_dict = PhotosPredictionUpdateError.from_dict(photos_prediction_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


