# UsersCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.users_create_error import UsersCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateError from a JSON string
users_create_error_instance = UsersCreateError.from_json(json)
# print the JSON string representation of the object
print(UsersCreateError.to_json())

# convert the object into a dict
users_create_error_dict = users_create_error_instance.to_dict()
# create an instance of UsersCreateError from a dict
users_create_error_from_dict = UsersCreateError.from_dict(users_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


