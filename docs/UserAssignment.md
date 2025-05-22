# UserAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**SimpleAnnotatorUser**](SimpleAnnotatorUser.md) |  | 
**annotation_id** | **int** |  | [readonly] 
**annotation_type** | **str** |  | [readonly] 

## Example

```python
from mosquito_alert.models.user_assignment import UserAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssignment from a JSON string
user_assignment_instance = UserAssignment.from_json(json)
# print the JSON string representation of the object
print(UserAssignment.to_json())

# convert the object into a dict
user_assignment_dict = user_assignment_instance.to_dict()
# create an instance of UserAssignment from a dict
user_assignment_from_dict = UserAssignment.from_dict(user_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


