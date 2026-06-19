# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [optional] 
**country** | [**Country**](Country.md) |  | [readonly] 
**memberships** | [**List[WorkspaceMembership]**](WorkspaceMembership.md) |  | [readonly] 
**is_public** | **bool** | Whether the results of the workspace are visible to the public. | [optional] 
**supervisor_exclusivity_days** | **int** | Number of days that a identification tasks in the queue is exclusively available to the supervisors. | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


