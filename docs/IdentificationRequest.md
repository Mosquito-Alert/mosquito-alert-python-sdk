# IdentificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photo** | [**SimplePhotoRequest**](SimplePhotoRequest.md) |  | 

## Example

```python
from mosquito_alert.models.identification_request import IdentificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationRequest from a JSON string
identification_request_instance = IdentificationRequest.from_json(json)
# print the JSON string representation of the object
print(IdentificationRequest.to_json())

# convert the object into a dict
identification_request_dict = identification_request_instance.to_dict()
# create an instance of IdentificationRequest from a dict
identification_request_from_dict = IdentificationRequest.from_dict(identification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


