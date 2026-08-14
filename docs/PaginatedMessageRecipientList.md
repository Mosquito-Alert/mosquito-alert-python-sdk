# PaginatedMessageRecipientList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MessageRecipient]**](MessageRecipient.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_message_recipient_list import PaginatedMessageRecipientList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMessageRecipientList from a JSON string
paginated_message_recipient_list_instance = PaginatedMessageRecipientList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMessageRecipientList.to_json())

# convert the object into a dict
paginated_message_recipient_list_dict = paginated_message_recipient_list_instance.to_dict()
# create an instance of PaginatedMessageRecipientList from a dict
paginated_message_recipient_list_from_dict = PaginatedMessageRecipientList.from_dict(paginated_message_recipient_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


