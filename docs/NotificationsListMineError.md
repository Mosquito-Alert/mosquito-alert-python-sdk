# NotificationsListMineError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.notifications_list_mine_error import NotificationsListMineError

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsListMineError from a JSON string
notifications_list_mine_error_instance = NotificationsListMineError.from_json(json)
# print the JSON string representation of the object
print(NotificationsListMineError.to_json())

# convert the object into a dict
notifications_list_mine_error_dict = notifications_list_mine_error_instance.to_dict()
# create an instance of NotificationsListMineError from a dict
notifications_list_mine_error_from_dict = NotificationsListMineError.from_dict(notifications_list_mine_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


