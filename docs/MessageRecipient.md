# MessageRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**MinimalUser**](MinimalUser.md) |  | [readonly] 
**has_read** | **bool** |  | [readonly] 

## Example

```python
from mosquito_alert.models.message_recipient import MessageRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of MessageRecipient from a JSON string
message_recipient_instance = MessageRecipient.from_json(json)
# print the JSON string representation of the object
print(MessageRecipient.to_json())

# convert the object into a dict
message_recipient_dict = message_recipient_instance.to_dict()
# create an instance of MessageRecipient from a dict
message_recipient_from_dict = MessageRecipient.from_dict(message_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


