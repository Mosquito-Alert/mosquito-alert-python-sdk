# AnnotationCharacteristics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sex** | **str** |  | [optional] 
**is_blood_fed** | **bool** |  | [optional] [default to False]
**is_gravid** | **bool** |  | [optional] [default to False]

## Example

```python
from mosquito_alert.models.annotation_characteristics import AnnotationCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationCharacteristics from a JSON string
annotation_characteristics_instance = AnnotationCharacteristics.from_json(json)
# print the JSON string representation of the object
print(AnnotationCharacteristics.to_json())

# convert the object into a dict
annotation_characteristics_dict = annotation_characteristics_instance.to_dict()
# create an instance of AnnotationCharacteristics from a dict
annotation_characteristics_from_dict = AnnotationCharacteristics.from_dict(annotation_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


