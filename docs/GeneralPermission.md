# GeneralPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [readonly] 
**permissions** | [**Permissions**](Permissions.md) |  | [readonly] 
**is_staff** | **bool** |  | 

## Example

```python
from mosquito_alert.models.general_permission import GeneralPermission

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralPermission from a JSON string
general_permission_instance = GeneralPermission.from_json(json)
# print the JSON string representation of the object
print(GeneralPermission.to_json())

# convert the object into a dict
general_permission_dict = general_permission_instance.to_dict()
# create an instance of GeneralPermission from a dict
general_permission_from_dict = GeneralPermission.from_dict(general_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


