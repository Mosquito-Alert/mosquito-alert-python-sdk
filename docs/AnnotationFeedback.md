# AnnotationFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_note** | **str** | Notes to display on public map | [optional] 
**user_note** | **str** | Message that user will receive when viewing report on phone | [optional] 

## Example

```python
from mosquito_alert.models.annotation_feedback import AnnotationFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationFeedback from a JSON string
annotation_feedback_instance = AnnotationFeedback.from_json(json)
# print the JSON string representation of the object
print(AnnotationFeedback.to_json())

# convert the object into a dict
annotation_feedback_dict = annotation_feedback_instance.to_dict()
# create an instance of AnnotationFeedback from a dict
annotation_feedback_from_dict = AnnotationFeedback.from_dict(annotation_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


