# AnnotationClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | [**SimpleTaxon**](SimpleTaxon.md) |  | [readonly] 
**confidence** | **float** |  | [readonly] 
**confidence_label** | **str** |  | 
**is_high_confidence** | **bool** |  | [readonly] 

## Example

```python
from mosquito_alert.models.annotation_classification import AnnotationClassification

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationClassification from a JSON string
annotation_classification_instance = AnnotationClassification.from_json(json)
# print the JSON string representation of the object
print(AnnotationClassification.to_json())

# convert the object into a dict
annotation_classification_dict = annotation_classification_instance.to_dict()
# create an instance of AnnotationClassification from a dict
annotation_classification_from_dict = AnnotationClassification.from_dict(annotation_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


