# MessagesCreateContentBodyLbErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.messages_create_content_body_lb_error_component import MessagesCreateContentBodyLbErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesCreateContentBodyLbErrorComponent from a JSON string
messages_create_content_body_lb_error_component_instance = MessagesCreateContentBodyLbErrorComponent.from_json(json)
# print the JSON string representation of the object
print(MessagesCreateContentBodyLbErrorComponent.to_json())

# convert the object into a dict
messages_create_content_body_lb_error_component_dict = messages_create_content_body_lb_error_component_instance.to_dict()
# create an instance of MessagesCreateContentBodyLbErrorComponent from a dict
messages_create_content_body_lb_error_component_from_dict = MessagesCreateContentBodyLbErrorComponent.from_dict(messages_create_content_body_lb_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


