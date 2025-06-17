# AnnotationFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_note** | **str** | Notes to display on public map | [optional] 
**internal_note** | **str** | Internal notes for yourself or other experts | [optional] 
**user_note** | **str** | Message that user will receive when viewing report on phone | [optional] 

## Example

```python
from mosquito_alert.models.annotation_feedback_request import AnnotationFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationFeedbackRequest from a JSON string
annotation_feedback_request_instance = AnnotationFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(AnnotationFeedbackRequest.to_json())

# convert the object into a dict
annotation_feedback_request_dict = annotation_feedback_request_instance.to_dict()
# create an instance of AnnotationFeedbackRequest from a dict
annotation_feedback_request_from_dict = AnnotationFeedbackRequest.from_dict(annotation_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


