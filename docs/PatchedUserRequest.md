# PatchedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_token** | **str** | Device token, used in messaging. Must be supplied by the client | [optional] 
**language_iso** | **str** | Language setting of app. 2-digit ISO-639-1 language code. | [optional] 

## Example

```python
from mosquito_alert.models.patched_user_request import PatchedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserRequest from a JSON string
patched_user_request_instance = PatchedUserRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserRequest.to_json())

# convert the object into a dict
patched_user_request_dict = patched_user_request_instance.to_dict()
# create an instance of PatchedUserRequest from a dict
patched_user_request_from_dict = PatchedUserRequest.from_dict(patched_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


