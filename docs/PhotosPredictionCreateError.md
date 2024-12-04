# PhotosPredictionCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.photos_prediction_create_error import PhotosPredictionCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosPredictionCreateError from a JSON string
photos_prediction_create_error_instance = PhotosPredictionCreateError.from_json(json)
# print the JSON string representation of the object
print(PhotosPredictionCreateError.to_json())

# convert the object into a dict
photos_prediction_create_error_dict = photos_prediction_create_error_instance.to_dict()
# create an instance of PhotosPredictionCreateError from a dict
photos_prediction_create_error_from_dict = PhotosPredictionCreateError.from_dict(photos_prediction_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


