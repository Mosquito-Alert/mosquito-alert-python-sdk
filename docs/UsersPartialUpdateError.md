# UsersPartialUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.users_partial_update_error import UsersPartialUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPartialUpdateError from a JSON string
users_partial_update_error_instance = UsersPartialUpdateError.from_json(json)
# print the JSON string representation of the object
print(UsersPartialUpdateError.to_json())

# convert the object into a dict
users_partial_update_error_dict = users_partial_update_error_instance.to_dict()
# create an instance of UsersPartialUpdateError from a dict
users_partial_update_error_from_dict = UsersPartialUpdateError.from_dict(users_partial_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


