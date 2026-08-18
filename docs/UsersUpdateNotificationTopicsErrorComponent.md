# UsersUpdateNotificationTopicsErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.users_update_notification_topics_error_component import UsersUpdateNotificationTopicsErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateNotificationTopicsErrorComponent from a JSON string
users_update_notification_topics_error_component_instance = UsersUpdateNotificationTopicsErrorComponent.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateNotificationTopicsErrorComponent.to_json())

# convert the object into a dict
users_update_notification_topics_error_component_dict = users_update_notification_topics_error_component_instance.to_dict()
# create an instance of UsersUpdateNotificationTopicsErrorComponent from a dict
users_update_notification_topics_error_component_from_dict = UsersUpdateNotificationTopicsErrorComponent.from_dict(users_update_notification_topics_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


