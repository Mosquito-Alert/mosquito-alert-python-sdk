# SimpleWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [optional] 
**country** | [**Country**](Country.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.simple_workspace import SimpleWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleWorkspace from a JSON string
simple_workspace_instance = SimpleWorkspace.from_json(json)
# print the JSON string representation of the object
print(SimpleWorkspace.to_json())

# convert the object into a dict
simple_workspace_dict = simple_workspace_instance.to_dict()
# create an instance of SimpleWorkspace from a dict
simple_workspace_from_dict = SimpleWorkspace.from_dict(simple_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


