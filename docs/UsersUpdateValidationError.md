# UsersUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[UsersUpdateError]**](UsersUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.users_update_validation_error import UsersUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateValidationError from a JSON string
users_update_validation_error_instance = UsersUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateValidationError.to_json())

# convert the object into a dict
users_update_validation_error_dict = users_update_validation_error_instance.to_dict()
# create an instance of UsersUpdateValidationError from a dict
users_update_validation_error_from_dict = UsersUpdateValidationError.from_dict(users_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


