# ObservationsListMineValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ObservationsListMineError]**](ObservationsListMineError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_list_mine_validation_error import ObservationsListMineValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsListMineValidationError from a JSON string
observations_list_mine_validation_error_instance = ObservationsListMineValidationError.from_json(json)
# print the JSON string representation of the object
print(ObservationsListMineValidationError.to_json())

# convert the object into a dict
observations_list_mine_validation_error_dict = observations_list_mine_validation_error_instance.to_dict()
# create an instance of ObservationsListMineValidationError from a dict
observations_list_mine_validation_error_from_dict = ObservationsListMineValidationError.from_dict(observations_list_mine_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

