# Permissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | [**AnnotationPermission**](AnnotationPermission.md) |  | 
**identification_task** | [**IdentificationTaskPermission**](IdentificationTaskPermission.md) |  | 
**review** | [**ReviewPermission**](ReviewPermission.md) |  | 

## Example

```python
from mosquito_alert.models.permissions import Permissions

# TODO update the JSON string below
json = "{}"
# create an instance of Permissions from a JSON string
permissions_instance = Permissions.from_json(json)
# print the JSON string representation of the object
print(Permissions.to_json())

# convert the object into a dict
permissions_dict = permissions_instance.to_dict()
# create an instance of Permissions from a dict
permissions_from_dict = Permissions.from_dict(permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


