# UsersAudienceFilterValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[UsersAudienceFilterError]**](UsersAudienceFilterError.md) |  | 

## Example

```python
from mosquito_alert.models.users_audience_filter_validation_error import UsersAudienceFilterValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAudienceFilterValidationError from a JSON string
users_audience_filter_validation_error_instance = UsersAudienceFilterValidationError.from_json(json)
# print the JSON string representation of the object
print(UsersAudienceFilterValidationError.to_json())

# convert the object into a dict
users_audience_filter_validation_error_dict = users_audience_filter_validation_error_instance.to_dict()
# create an instance of UsersAudienceFilterValidationError from a dict
users_audience_filter_validation_error_from_dict = UsersAudienceFilterValidationError.from_dict(users_audience_filter_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


