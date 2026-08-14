# MessageRecipientStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**read** | **int** |  | 
**unread** | **int** |  | 

## Example

```python
from mosquito_alert.models.message_recipient_stats import MessageRecipientStats

# TODO update the JSON string below
json = "{}"
# create an instance of MessageRecipientStats from a JSON string
message_recipient_stats_instance = MessageRecipientStats.from_json(json)
# print the JSON string representation of the object
print(MessageRecipientStats.to_json())

# convert the object into a dict
message_recipient_stats_dict = message_recipient_stats_instance.to_dict()
# create an instance of MessageRecipientStats from a dict
message_recipient_stats_from_dict = MessageRecipientStats.from_dict(message_recipient_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


