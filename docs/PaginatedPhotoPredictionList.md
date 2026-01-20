# PaginatedPhotoPredictionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PhotoPrediction]**](PhotoPrediction.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_photo_prediction_list import PaginatedPhotoPredictionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPhotoPredictionList from a JSON string
paginated_photo_prediction_list_instance = PaginatedPhotoPredictionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPhotoPredictionList.to_json())

# convert the object into a dict
paginated_photo_prediction_list_dict = paginated_photo_prediction_list_instance.to_dict()
# create an instance of PaginatedPhotoPredictionList from a dict
paginated_photo_prediction_list_from_dict = PaginatedPhotoPredictionList.from_dict(paginated_photo_prediction_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


