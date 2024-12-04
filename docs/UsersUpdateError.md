# UsersUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.users_update_error import UsersUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateError from a JSON string
users_update_error_instance = UsersUpdateError.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateError.to_json())

# convert the object into a dict
users_update_error_dict = users_update_error_instance.to_dict()
# create an instance of UsersUpdateError from a dict
users_update_error_from_dict = UsersUpdateError.from_dict(users_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


