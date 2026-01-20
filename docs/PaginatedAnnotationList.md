# PaginatedAnnotationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Annotation]**](Annotation.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_annotation_list import PaginatedAnnotationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAnnotationList from a JSON string
paginated_annotation_list_instance = PaginatedAnnotationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAnnotationList.to_json())

# convert the object into a dict
paginated_annotation_list_dict = paginated_annotation_list_instance.to_dict()
# create an instance of PaginatedAnnotationList from a dict
paginated_annotation_list_from_dict = PaginatedAnnotationList.from_dict(paginated_annotation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


