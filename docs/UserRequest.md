# UserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_token** | **str** | Device token, used in messaging. Must be supplied by the client | [optional] 

## Example

```python
from mosquito_alert.models.user_request import UserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequest from a JSON string
user_request_instance = UserRequest.from_json(json)
# print the JSON string representation of the object
print(UserRequest.to_json())

# convert the object into a dict
user_request_dict = user_request_instance.to_dict()
# create an instance of UserRequest from a dict
user_request_from_dict = UserRequest.from_dict(user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


