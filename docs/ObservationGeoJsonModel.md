# ObservationGeoJsonModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **UUID** |  | [optional] [readonly] 
**geometry** | [**BiteGeoJsonModelGeometry**](BiteGeoJsonModelGeometry.md) |  | [optional] 
**properties** | [**ObservationGeoJsonModelProperties**](ObservationGeoJsonModelProperties.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.observation_geo_json_model import ObservationGeoJsonModel

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationGeoJsonModel from a JSON string
observation_geo_json_model_instance = ObservationGeoJsonModel.from_json(json)
# print the JSON string representation of the object
print(ObservationGeoJsonModel.to_json())

# convert the object into a dict
observation_geo_json_model_dict = observation_geo_json_model_instance.to_dict()
# create an instance of ObservationGeoJsonModel from a dict
observation_geo_json_model_from_dict = ObservationGeoJsonModel.from_dict(observation_geo_json_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


