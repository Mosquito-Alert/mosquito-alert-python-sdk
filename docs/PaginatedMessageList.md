# PaginatedMessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Message]**](Message.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_message_list import PaginatedMessageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMessageList from a JSON string
paginated_message_list_instance = PaginatedMessageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMessageList.to_json())

# convert the object into a dict
paginated_message_list_dict = paginated_message_list_instance.to_dict()
# create an instance of PaginatedMessageList from a dict
paginated_message_list_from_dict = PaginatedMessageList.from_dict(paginated_message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


