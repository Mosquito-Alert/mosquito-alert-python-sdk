# UsersPartialUpdateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[UsersPartialUpdateError]**](UsersPartialUpdateError.md) |  | 

## Example

```python
from mosquito_alert.models.users_partial_update_validation_error import UsersPartialUpdateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPartialUpdateValidationError from a JSON string
users_partial_update_validation_error_instance = UsersPartialUpdateValidationError.from_json(json)
# print the JSON string representation of the object
print(UsersPartialUpdateValidationError.to_json())

# convert the object into a dict
users_partial_update_validation_error_dict = users_partial_update_validation_error_instance.to_dict()
# create an instance of UsersPartialUpdateValidationError from a dict
users_partial_update_validation_error_from_dict = UsersPartialUpdateValidationError.from_dict(users_partial_update_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


