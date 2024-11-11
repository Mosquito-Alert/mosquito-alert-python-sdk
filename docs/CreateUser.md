# CreateUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**registration_time** | **datetime** | The date and time when user registered and consented to sharing data. Automatically set by server when user uploads registration. | [readonly] 
**score** | **int** | Global XP Score. This field is updated whenever the user asks for the score, and is only stored here. The content must equal score_v2_adult + score_v2_bite + score_v2_site | [readonly] 
**last_score_update** | **datetime** | Last time score was updated | [readonly] 

## Example

```python
from mosquito_alert_api.models.create_user import CreateUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUser from a JSON string
create_user_instance = CreateUser.from_json(json)
# print the JSON string representation of the object
print(CreateUser.to_json())

# convert the object into a dict
create_user_dict = create_user_instance.to_dict()
# create an instance of CreateUser from a dict
create_user_from_dict = CreateUser.from_dict(create_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


