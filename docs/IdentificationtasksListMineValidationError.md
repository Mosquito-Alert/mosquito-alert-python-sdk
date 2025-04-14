# IdentificationtasksListMineValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[IdentificationtasksListMineError]**](IdentificationtasksListMineError.md) |  | 

## Example

```python
from mosquito_alert.models.identificationtasks_list_mine_validation_error import IdentificationtasksListMineValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationtasksListMineValidationError from a JSON string
identificationtasks_list_mine_validation_error_instance = IdentificationtasksListMineValidationError.from_json(json)
# print the JSON string representation of the object
print(IdentificationtasksListMineValidationError.to_json())

# convert the object into a dict
identificationtasks_list_mine_validation_error_dict = identificationtasks_list_mine_validation_error_instance.to_dict()
# create an instance of IdentificationtasksListMineValidationError from a dict
identificationtasks_list_mine_validation_error_from_dict = IdentificationtasksListMineValidationError.from_dict(identificationtasks_list_mine_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


