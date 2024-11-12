# PaginatedDetailNotificationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DetailNotification]**](DetailNotification.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.paginated_detail_notification_list import PaginatedDetailNotificationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDetailNotificationList from a JSON string
paginated_detail_notification_list_instance = PaginatedDetailNotificationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDetailNotificationList.to_json())

# convert the object into a dict
paginated_detail_notification_list_dict = paginated_detail_notification_list_instance.to_dict()
# create an instance of PaginatedDetailNotificationList from a dict
paginated_detail_notification_list_from_dict = PaginatedDetailNotificationList.from_dict(paginated_detail_notification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


