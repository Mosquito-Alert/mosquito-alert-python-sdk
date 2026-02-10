# ObservationsGeoListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ObservationsGeoListError]**](ObservationsGeoListError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_geo_list_validation_error import ObservationsGeoListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsGeoListValidationError from a JSON string
observations_geo_list_validation_error_instance = ObservationsGeoListValidationError.from_json(json)
# print the JSON string representation of the object
print(ObservationsGeoListValidationError.to_json())

# convert the object into a dict
observations_geo_list_validation_error_dict = observations_geo_list_validation_error_instance.to_dict()
# create an instance of ObservationsGeoListValidationError from a dict
observations_geo_list_validation_error_from_dict = ObservationsGeoListValidationError.from_dict(observations_geo_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


