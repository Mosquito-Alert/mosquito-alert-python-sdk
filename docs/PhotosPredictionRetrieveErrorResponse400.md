# PhotosPredictionRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.photos_prediction_retrieve_error_response400 import PhotosPredictionRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosPredictionRetrieveErrorResponse400 from a JSON string
photos_prediction_retrieve_error_response400_instance = PhotosPredictionRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(PhotosPredictionRetrieveErrorResponse400.to_json())

# convert the object into a dict
photos_prediction_retrieve_error_response400_dict = photos_prediction_retrieve_error_response400_instance.to_dict()
# create an instance of PhotosPredictionRetrieveErrorResponse400 from a dict
photos_prediction_retrieve_error_response400_from_dict = PhotosPredictionRetrieveErrorResponse400.from_dict(photos_prediction_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


