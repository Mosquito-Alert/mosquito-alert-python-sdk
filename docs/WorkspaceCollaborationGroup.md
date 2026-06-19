# WorkspaceCollaborationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**workspaces** | [**List[SimpleWorkspace]**](SimpleWorkspace.md) |  | [readonly] 
**reviewers** | [**List[SimpleUser]**](SimpleUser.md) |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.workspace_collaboration_group import WorkspaceCollaborationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCollaborationGroup from a JSON string
workspace_collaboration_group_instance = WorkspaceCollaborationGroup.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCollaborationGroup.to_json())

# convert the object into a dict
workspace_collaboration_group_dict = workspace_collaboration_group_instance.to_dict()
# create an instance of WorkspaceCollaborationGroup from a dict
workspace_collaboration_group_from_dict = WorkspaceCollaborationGroup.from_dict(workspace_collaboration_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


