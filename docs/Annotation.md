# Annotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**observation_uuid** | **str** | UUID randomly generated on phone to identify each unique report version. Must be exactly 36 characters (32 hex digits plus 4 hyphens). | [readonly] 
**user** | [**SimpleAnnotatorUser**](SimpleAnnotatorUser.md) |  | [readonly] 
**best_photo** | [**SimplePhoto**](SimplePhoto.md) |  | [readonly] 
**classification** | [**AnnotationClassification**](AnnotationClassification.md) |  | 
**feedback** | [**AnnotationFeedback**](AnnotationFeedback.md) |  | [optional] 
**type** | **str** |  | [readonly] 
**is_flagged** | **bool** |  | [readonly] [default to False]
**is_decisive** | **bool** |  | [readonly] [default to False]
**observation_flags** | [**ObservationFlags**](ObservationFlags.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.annotation import Annotation

# TODO update the JSON string below
json = "{}"
# create an instance of Annotation from a JSON string
annotation_instance = Annotation.from_json(json)
# print the JSON string representation of the object
print(Annotation.to_json())

# convert the object into a dict
annotation_dict = annotation_instance.to_dict()
# create an instance of Annotation from a dict
annotation_from_dict = Annotation.from_dict(annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


