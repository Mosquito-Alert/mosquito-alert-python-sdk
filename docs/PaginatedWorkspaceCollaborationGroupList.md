# PaginatedWorkspaceCollaborationGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[WorkspaceCollaborationGroup]**](WorkspaceCollaborationGroup.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_workspace_collaboration_group_list import PaginatedWorkspaceCollaborationGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkspaceCollaborationGroupList from a JSON string
paginated_workspace_collaboration_group_list_instance = PaginatedWorkspaceCollaborationGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWorkspaceCollaborationGroupList.to_json())

# convert the object into a dict
paginated_workspace_collaboration_group_list_dict = paginated_workspace_collaboration_group_list_instance.to_dict()
# create an instance of PaginatedWorkspaceCollaborationGroupList from a dict
paginated_workspace_collaboration_group_list_from_dict = PaginatedWorkspaceCollaborationGroupList.from_dict(paginated_workspace_collaboration_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


