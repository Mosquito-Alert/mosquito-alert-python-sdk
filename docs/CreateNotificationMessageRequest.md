# CreateNotificationMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedMessageTitleRequest**](LocalizedMessageTitleRequest.md) | Provide the message&#39;s title in all supported languages | 
**body** | [**LocalizedMessageBodyRequest**](LocalizedMessageBodyRequest.md) | Provide the message&#39;s body in all supported languages | 

## Example

```python
from mosquito_alert.models.create_notification_message_request import CreateNotificationMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationMessageRequest from a JSON string
create_notification_message_request_instance = CreateNotificationMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationMessageRequest.to_json())

# convert the object into a dict
create_notification_message_request_dict = create_notification_message_request_instance.to_dict()
# create an instance of CreateNotificationMessageRequest from a dict
create_notification_message_request_from_dict = CreateNotificationMessageRequest.from_dict(create_notification_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


