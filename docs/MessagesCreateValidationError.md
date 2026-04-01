# MessagesCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[MessagesCreateError]**](MessagesCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.messages_create_validation_error import MessagesCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesCreateValidationError from a JSON string
messages_create_validation_error_instance = MessagesCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(MessagesCreateValidationError.to_json())

# convert the object into a dict
messages_create_validation_error_dict = messages_create_validation_error_instance.to_dict()
# create an instance of MessagesCreateValidationError from a dict
messages_create_validation_error_from_dict = MessagesCreateValidationError.from_dict(messages_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


