# ObservationGeoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**point** | [**Point**](Point.md) |  | 
**received_at** | **datetime** |  | [readonly] 
**identification_taxon_id** | **int** |  | [readonly] 

## Example

```python
from mosquito_alert.models.observation_geo_model import ObservationGeoModel

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationGeoModel from a JSON string
observation_geo_model_instance = ObservationGeoModel.from_json(json)
# print the JSON string representation of the object
print(ObservationGeoModel.to_json())

# convert the object into a dict
observation_geo_model_dict = observation_geo_model_instance.to_dict()
# create an instance of ObservationGeoModel from a dict
observation_geo_model_from_dict = ObservationGeoModel.from_dict(observation_geo_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


