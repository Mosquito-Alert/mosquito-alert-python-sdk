# PhotosRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.photos_retrieve_error_response400 import PhotosRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of PhotosRetrieveErrorResponse400 from a JSON string
photos_retrieve_error_response400_instance = PhotosRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(PhotosRetrieveErrorResponse400.to_json())

# convert the object into a dict
photos_retrieve_error_response400_dict = photos_retrieve_error_response400_instance.to_dict()
# create an instance of PhotosRetrieveErrorResponse400 from a dict
photos_retrieve_error_response400_from_dict = PhotosRetrieveErrorResponse400.from_dict(photos_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


