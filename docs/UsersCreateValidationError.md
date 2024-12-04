# UsersCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[UsersCreateError]**](UsersCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.users_create_validation_error import UsersCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateValidationError from a JSON string
users_create_validation_error_instance = UsersCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(UsersCreateValidationError.to_json())

# convert the object into a dict
users_create_validation_error_dict = users_create_validation_error_instance.to_dict()
# create an instance of UsersCreateValidationError from a dict
users_create_validation_error_from_dict = UsersCreateValidationError.from_dict(users_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


