# PaginatedSimplePhotoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SimplePhoto]**](SimplePhoto.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.paginated_simple_photo_list import PaginatedSimplePhotoList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSimplePhotoList from a JSON string
paginated_simple_photo_list_instance = PaginatedSimplePhotoList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSimplePhotoList.to_json())

# convert the object into a dict
paginated_simple_photo_list_dict = paginated_simple_photo_list_instance.to_dict()
# create an instance of PaginatedSimplePhotoList from a dict
paginated_simple_photo_list_from_dict = PaginatedSimplePhotoList.from_dict(paginated_simple_photo_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


