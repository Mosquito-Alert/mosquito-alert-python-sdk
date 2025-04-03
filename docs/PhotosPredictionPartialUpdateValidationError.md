# PhotosPredictionPartialUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[PhotosPredictionPartialUpdateError]**](PhotosPredictionPartialUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.photos_prediction_partial_update_validation_error import PhotosPredictionPartialUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosPredictionPartialUpdateValidationError from a JSON string
photos_prediction_partial_update_validation_error_instance = PhotosPredictionPartialUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(PhotosPredictionPartialUpdateValidationError.to_json())

# convert the object into a dict
photos_prediction_partial_update_validation_error_dict = photos_prediction_partial_update_validation_error_instance.to_dict()
# create an instance of PhotosPredictionPartialUpdateValidationError from a dict
photos_prediction_partial_update_validation_error_from_dict = PhotosPredictionPartialUpdateValidationError.from_dict(photos_prediction_partial_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


