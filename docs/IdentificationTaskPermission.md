# IdentificationTaskPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **bool** |  | 
**change** | **bool** |  | 
**view** | **bool** |  | 
**delete** | **bool** |  | 

## Example

```python
from mosquito_alert.models.identification_task_permission import IdentificationTaskPermission

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTaskPermission from a JSON string
identification_task_permission_instance = IdentificationTaskPermission.from_json(json)
# print the JSON string representation of the object
print(IdentificationTaskPermission.to_json())

# convert the object into a dict
identification_task_permission_dict = identification_task_permission_instance.to_dict()
# create an instance of IdentificationTaskPermission from a dict
identification_task_permission_from_dict = IdentificationTaskPermission.from_dict(identification_task_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


