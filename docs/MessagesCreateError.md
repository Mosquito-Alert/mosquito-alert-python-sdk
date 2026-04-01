# MessagesCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.messages_create_error import MessagesCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesCreateError from a JSON string
messages_create_error_instance = MessagesCreateError.from_json(json)
# print the JSON string representation of the object
print(MessagesCreateError.to_json())

# convert the object into a dict
messages_create_error_dict = messages_create_error_instance.to_dict()
# create an instance of MessagesCreateError from a dict
messages_create_error_from_dict = MessagesCreateError.from_dict(messages_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


