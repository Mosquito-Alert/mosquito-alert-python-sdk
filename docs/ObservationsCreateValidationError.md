# ObservationsCreateValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ObservationsCreateError]**](ObservationsCreateError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_create_validation_error import ObservationsCreateValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsCreateValidationError from a JSON string
observations_create_validation_error_instance = ObservationsCreateValidationError.from_json(json)
# print the JSON string representation of the object
print(ObservationsCreateValidationError.to_json())

# convert the object into a dict
observations_create_validation_error_dict = observations_create_validation_error_instance.to_dict()
# create an instance of ObservationsCreateValidationError from a dict
observations_create_validation_error_from_dict = ObservationsCreateValidationError.from_dict(observations_create_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


