# MessagesListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.messages_list_error import MessagesListError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesListError from a JSON string
messages_list_error_instance = MessagesListError.from_json(json)
# print the JSON string representation of the object
print(MessagesListError.to_json())

# convert the object into a dict
messages_list_error_dict = messages_list_error_instance.to_dict()
# create an instance of MessagesListError from a dict
messages_list_error_from_dict = MessagesListError.from_dict(messages_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


