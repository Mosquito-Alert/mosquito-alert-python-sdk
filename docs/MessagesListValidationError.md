# MessagesListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[MessagesListError]**](MessagesListError.md) |  | 

## Example

```python
from mosquito_alert.models.messages_list_validation_error import MessagesListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesListValidationError from a JSON string
messages_list_validation_error_instance = MessagesListValidationError.from_json(json)
# print the JSON string representation of the object
print(MessagesListValidationError.to_json())

# convert the object into a dict
messages_list_validation_error_dict = messages_list_validation_error_instance.to_dict()
# create an instance of MessagesListValidationError from a dict
messages_list_validation_error_from_dict = MessagesListValidationError.from_dict(messages_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


