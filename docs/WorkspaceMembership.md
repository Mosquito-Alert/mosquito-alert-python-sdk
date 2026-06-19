# WorkspaceMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**SimpleUser**](SimpleUser.md) |  | [readonly] 
**role** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.workspace_membership import WorkspaceMembership

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembership from a JSON string
workspace_membership_instance = WorkspaceMembership.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMembership.to_json())

# convert the object into a dict
workspace_membership_dict = workspace_membership_instance.to_dict()
# create an instance of WorkspaceMembership from a dict
workspace_membership_from_dict = WorkspaceMembership.from_dict(workspace_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


