# PaginatedMessageTopicList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MessageTopic]**](MessageTopic.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_message_topic_list import PaginatedMessageTopicList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMessageTopicList from a JSON string
paginated_message_topic_list_instance = PaginatedMessageTopicList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMessageTopicList.to_json())

# convert the object into a dict
paginated_message_topic_list_dict = paginated_message_topic_list_instance.to_dict()
# create an instance of PaginatedMessageTopicList from a dict
paginated_message_topic_list_from_dict = PaginatedMessageTopicList.from_dict(paginated_message_topic_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


