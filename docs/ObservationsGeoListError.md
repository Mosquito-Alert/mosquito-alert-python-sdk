# ObservationsGeoListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.observations_geo_list_error import ObservationsGeoListError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsGeoListError from a JSON string
observations_geo_list_error_instance = ObservationsGeoListError.from_json(json)
# print the JSON string representation of the object
print(ObservationsGeoListError.to_json())

# convert the object into a dict
observations_geo_list_error_dict = observations_geo_list_error_instance.to_dict()
# create an instance of ObservationsGeoListError from a dict
observations_geo_list_error_from_dict = ObservationsGeoListError.from_dict(observations_geo_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


