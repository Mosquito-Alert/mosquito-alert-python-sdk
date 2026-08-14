# MessageTargeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | [readonly] 
**audience** | [**AudienceFilter**](AudienceFilter.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.message_targeting import MessageTargeting

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTargeting from a JSON string
message_targeting_instance = MessageTargeting.from_json(json)
# print the JSON string representation of the object
print(MessageTargeting.to_json())

# convert the object into a dict
message_targeting_dict = message_targeting_instance.to_dict()
# create an instance of MessageTargeting from a dict
message_targeting_from_dict = MessageTargeting.from_dict(message_targeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


