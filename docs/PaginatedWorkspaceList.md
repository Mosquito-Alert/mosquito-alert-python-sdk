# PaginatedWorkspaceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Workspace]**](Workspace.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_workspace_list import PaginatedWorkspaceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkspaceList from a JSON string
paginated_workspace_list_instance = PaginatedWorkspaceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWorkspaceList.to_json())

# convert the object into a dict
paginated_workspace_list_dict = paginated_workspace_list_instance.to_dict()
# create an instance of PaginatedWorkspaceList from a dict
paginated_workspace_list_from_dict = PaginatedWorkspaceList.from_dict(paginated_workspace_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


