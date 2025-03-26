# IdentificationtasksListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[IdentificationtasksListError]**](IdentificationtasksListError.md) |  | 

## Example

```python
from mosquito_alert.models.identificationtasks_list_validation_error import IdentificationtasksListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationtasksListValidationError from a JSON string
identificationtasks_list_validation_error_instance = IdentificationtasksListValidationError.from_json(json)
# print the JSON string representation of the object
print(IdentificationtasksListValidationError.to_json())

# convert the object into a dict
identificationtasks_list_validation_error_dict = identificationtasks_list_validation_error_instance.to_dict()
# create an instance of IdentificationtasksListValidationError from a dict
identificationtasks_list_validation_error_from_dict = IdentificationtasksListValidationError.from_dict(identificationtasks_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


