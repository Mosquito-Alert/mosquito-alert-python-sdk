# AppUserTokenObtainPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** |  | [readonly] 
**refresh** | **str** |  | [readonly] 

## Example

```python
from mosquito_alert.models.app_user_token_obtain_pair import AppUserTokenObtainPair

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserTokenObtainPair from a JSON string
app_user_token_obtain_pair_instance = AppUserTokenObtainPair.from_json(json)
# print the JSON string representation of the object
print(AppUserTokenObtainPair.to_json())

# convert the object into a dict
app_user_token_obtain_pair_dict = app_user_token_obtain_pair_instance.to_dict()
# create an instance of AppUserTokenObtainPair from a dict
app_user_token_obtain_pair_from_dict = AppUserTokenObtainPair.from_dict(app_user_token_obtain_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


