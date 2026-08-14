# UsersAudienceFilterError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.users_audience_filter_error import UsersAudienceFilterError

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAudienceFilterError from a JSON string
users_audience_filter_error_instance = UsersAudienceFilterError.from_json(json)
# print the JSON string representation of the object
print(UsersAudienceFilterError.to_json())

# convert the object into a dict
users_audience_filter_error_dict = users_audience_filter_error_instance.to_dict()
# create an instance of UsersAudienceFilterError from a dict
users_audience_filter_error_from_dict = UsersAudienceFilterError.from_dict(users_audience_filter_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


