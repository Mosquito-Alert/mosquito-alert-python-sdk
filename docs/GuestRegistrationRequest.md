# GuestRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from mosquito_alert.models.guest_registration_request import GuestRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistrationRequest from a JSON string
guest_registration_request_instance = GuestRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(GuestRegistrationRequest.to_json())

# convert the object into a dict
guest_registration_request_dict = guest_registration_request_instance.to_dict()
# create an instance of GuestRegistrationRequest from a dict
guest_registration_request_from_dict = GuestRegistrationRequest.from_dict(guest_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


