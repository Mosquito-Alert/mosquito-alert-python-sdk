# GuestRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | UUID randomly generated on phone to identify each unique user. Must be exactly 36 characters (32 hex digits plus 4 hyphens). | [readonly] 

## Example

```python
from mosquito_alert.models.guest_registration import GuestRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistration from a JSON string
guest_registration_instance = GuestRegistration.from_json(json)
# print the JSON string representation of the object
print(GuestRegistration.to_json())

# convert the object into a dict
guest_registration_dict = guest_registration_instance.to_dict()
# create an instance of GuestRegistration from a dict
guest_registration_from_dict = GuestRegistration.from_dict(guest_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


