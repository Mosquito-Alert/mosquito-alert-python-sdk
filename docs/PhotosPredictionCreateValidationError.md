# PhotosPredictionCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[PhotosPredictionCreateError]**](PhotosPredictionCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.photos_prediction_create_validation_error import PhotosPredictionCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosPredictionCreateValidationError from a JSON string
photos_prediction_create_validation_error_instance = PhotosPredictionCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(PhotosPredictionCreateValidationError.to_json())

# convert the object into a dict
photos_prediction_create_validation_error_dict = photos_prediction_create_validation_error_instance.to_dict()
# create an instance of PhotosPredictionCreateValidationError from a dict
photos_prediction_create_validation_error_from_dict = PhotosPredictionCreateValidationError.from_dict(photos_prediction_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


