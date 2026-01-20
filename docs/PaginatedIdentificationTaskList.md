# PaginatedIdentificationTaskList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[IdentificationTask]**](IdentificationTask.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_identification_task_list import PaginatedIdentificationTaskList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedIdentificationTaskList from a JSON string
paginated_identification_task_list_instance = PaginatedIdentificationTaskList.from_json(json)
# print the JSON string representation of the object
print(PaginatedIdentificationTaskList.to_json())

# convert the object into a dict
paginated_identification_task_list_dict = paginated_identification_task_list_instance.to_dict()
# create an instance of PaginatedIdentificationTaskList from a dict
paginated_identification_task_list_from_dict = PaginatedIdentificationTaskList.from_dict(paginated_identification_task_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


