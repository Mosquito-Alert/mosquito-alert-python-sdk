# MessagesListTargetErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.messages_list_target_error_component import MessagesListTargetErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesListTargetErrorComponent from a JSON string
messages_list_target_error_component_instance = MessagesListTargetErrorComponent.from_json(json)
# print the JSON string representation of the object
print(MessagesListTargetErrorComponent.to_json())

# convert the object into a dict
messages_list_target_error_component_dict = messages_list_target_error_component_instance.to_dict()
# create an instance of MessagesListTargetErrorComponent from a dict
messages_list_target_error_component_from_dict = MessagesListTargetErrorComponent.from_dict(messages_list_target_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


