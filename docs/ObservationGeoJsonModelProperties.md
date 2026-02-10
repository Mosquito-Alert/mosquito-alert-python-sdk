# ObservationGeoJsonModelProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**received_at** | **datetime** |  | [optional] [readonly] 
**identification_taxon_id** | **int** |  | [optional] [readonly] 

## Example

```python
from mosquito_alert.models.observation_geo_json_model_properties import ObservationGeoJsonModelProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationGeoJsonModelProperties from a JSON string
observation_geo_json_model_properties_instance = ObservationGeoJsonModelProperties.from_json(json)
# print the JSON string representation of the object
print(ObservationGeoJsonModelProperties.to_json())

# convert the object into a dict
observation_geo_json_model_properties_dict = observation_geo_json_model_properties_instance.to_dict()
# create an instance of ObservationGeoJsonModelProperties from a dict
observation_geo_json_model_properties_from_dict = ObservationGeoJsonModelProperties.from_dict(observation_geo_json_model_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


