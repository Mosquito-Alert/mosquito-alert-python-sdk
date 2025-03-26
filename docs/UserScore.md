# UserScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.user_score import UserScore

# TODO update the JSON string below
json = "{}"
# create an instance of UserScore from a JSON string
user_score_instance = UserScore.from_json(json)
# print the JSON string representation of the object
print(UserScore.to_json())

# convert the object into a dict
user_score_dict = user_score_instance.to_dict()
# create an instance of UserScore from a dict
user_score_from_dict = UserScore.from_dict(user_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


