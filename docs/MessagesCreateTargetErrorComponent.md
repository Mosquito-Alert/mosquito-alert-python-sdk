# MessagesCreateTargetErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.messages_create_target_error_component import MessagesCreateTargetErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesCreateTargetErrorComponent from a JSON string
messages_create_target_error_component_instance = MessagesCreateTargetErrorComponent.from_json(json)
# print the JSON string representation of the object
print(MessagesCreateTargetErrorComponent.to_json())

# convert the object into a dict
messages_create_target_error_component_dict = messages_create_target_error_component_instance.to_dict()
# create an instance of MessagesCreateTargetErrorComponent from a dict
messages_create_target_error_component_from_dict = MessagesCreateTargetErrorComponent.from_dict(messages_create_target_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


