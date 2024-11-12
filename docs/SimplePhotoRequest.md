# SimplePhotoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | 

## Example

```python
from mosquito_alert.models.simple_photo_request import SimplePhotoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePhotoRequest from a JSON string
simple_photo_request_instance = SimplePhotoRequest.from_json(json)
# print the JSON string representation of the object
print(SimplePhotoRequest.to_json())

# convert the object into a dict
simple_photo_request_dict = simple_photo_request_instance.to_dict()
# create an instance of SimplePhotoRequest from a dict
simple_photo_request_from_dict = SimplePhotoRequest.from_dict(simple_photo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


