# AnnotationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**best_photo_uuid** | **str** |  | [optional] 
**classification** | [**AnnotationClassificationRequest**](AnnotationClassificationRequest.md) |  | 
**characteristics** | [**AnnotationCharacteristicsRequest**](AnnotationCharacteristicsRequest.md) |  | [optional] 
**feedback** | [**AnnotationFeedbackRequest**](AnnotationFeedbackRequest.md) |  | [optional] 
**is_flagged** | **bool** |  | [optional] [default to False]
**is_decisive** | **bool** |  | [optional] [default to False]
**observation_flags** | [**ObservationFlagsRequest**](ObservationFlagsRequest.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from mosquito_alert.models.annotation_request import AnnotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRequest from a JSON string
annotation_request_instance = AnnotationRequest.from_json(json)
# print the JSON string representation of the object
print(AnnotationRequest.to_json())

# convert the object into a dict
annotation_request_dict = annotation_request_instance.to_dict()
# create an instance of AnnotationRequest from a dict
annotation_request_from_dict = AnnotationRequest.from_dict(annotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


