# CreateNotificationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedField**](LocalizedField.md) | Provide the message&#39;s title in all supported languages | 
**body** | [**LocalizedField**](LocalizedField.md) | Provide the message&#39;s body in all supported languages | 

## Example

```python
from mosquito_alert.models.create_notification_message import CreateNotificationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationMessage from a JSON string
create_notification_message_instance = CreateNotificationMessage.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationMessage.to_json())

# convert the object into a dict
create_notification_message_dict = create_notification_message_instance.to_dict()
# create an instance of CreateNotificationMessage from a dict
create_notification_message_from_dict = CreateNotificationMessage.from_dict(create_notification_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


