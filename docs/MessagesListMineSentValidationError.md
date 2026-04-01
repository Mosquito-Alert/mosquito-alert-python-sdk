# MessagesListMineSentValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[MessagesListMineSentError]**](MessagesListMineSentError.md) |  | 

## Example

```python
from mosquito_alert.models.messages_list_mine_sent_validation_error import MessagesListMineSentValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesListMineSentValidationError from a JSON string
messages_list_mine_sent_validation_error_instance = MessagesListMineSentValidationError.from_json(json)
# print the JSON string representation of the object
print(MessagesListMineSentValidationError.to_json())

# convert the object into a dict
messages_list_mine_sent_validation_error_dict = messages_list_mine_sent_validation_error_instance.to_dict()
# create an instance of MessagesListMineSentValidationError from a dict
messages_list_mine_sent_validation_error_from_dict = MessagesListMineSentValidationError.from_dict(messages_list_mine_sent_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


