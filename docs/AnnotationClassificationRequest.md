# AnnotationClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon_id** | **int** |  | 
**confidence_label** | **str** |  | 

## Example

```python
from mosquito_alert.models.annotation_classification_request import AnnotationClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationClassificationRequest from a JSON string
annotation_classification_request_instance = AnnotationClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(AnnotationClassificationRequest.to_json())

# convert the object into a dict
annotation_classification_request_dict = annotation_classification_request_instance.to_dict()
# create an instance of AnnotationClassificationRequest from a dict
annotation_classification_request_from_dict = AnnotationClassificationRequest.from_dict(annotation_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


