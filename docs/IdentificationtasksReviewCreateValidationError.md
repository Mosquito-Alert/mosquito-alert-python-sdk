# IdentificationtasksReviewCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[IdentificationtasksReviewCreateError]**](IdentificationtasksReviewCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.identificationtasks_review_create_validation_error import IdentificationtasksReviewCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationtasksReviewCreateValidationError from a JSON string
identificationtasks_review_create_validation_error_instance = IdentificationtasksReviewCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(IdentificationtasksReviewCreateValidationError.to_json())

# convert the object into a dict
identificationtasks_review_create_validation_error_dict = identificationtasks_review_create_validation_error_instance.to_dict()
# create an instance of IdentificationtasksReviewCreateValidationError from a dict
identificationtasks_review_create_validation_error_from_dict = IdentificationtasksReviewCreateValidationError.from_dict(identificationtasks_review_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


