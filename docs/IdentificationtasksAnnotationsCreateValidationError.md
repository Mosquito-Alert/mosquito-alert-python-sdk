# IdentificationtasksAnnotationsCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[IdentificationtasksAnnotationsCreateError]**](IdentificationtasksAnnotationsCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.identificationtasks_annotations_create_validation_error import IdentificationtasksAnnotationsCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationtasksAnnotationsCreateValidationError from a JSON string
identificationtasks_annotations_create_validation_error_instance = IdentificationtasksAnnotationsCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(IdentificationtasksAnnotationsCreateValidationError.to_json())

# convert the object into a dict
identificationtasks_annotations_create_validation_error_dict = identificationtasks_annotations_create_validation_error_instance.to_dict()
# create an instance of IdentificationtasksAnnotationsCreateValidationError from a dict
identificationtasks_annotations_create_validation_error_from_dict = IdentificationtasksAnnotationsCreateValidationError.from_dict(identificationtasks_annotations_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


