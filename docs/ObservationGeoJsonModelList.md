# ObservationGeoJsonModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**features** | [**List[ObservationGeoJsonModel]**](ObservationGeoJsonModel.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.observation_geo_json_model_list import ObservationGeoJsonModelList

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationGeoJsonModelList from a JSON string
observation_geo_json_model_list_instance = ObservationGeoJsonModelList.from_json(json)
# print the JSON string representation of the object
print(ObservationGeoJsonModelList.to_json())

# convert the object into a dict
observation_geo_json_model_list_dict = observation_geo_json_model_list_instance.to_dict()
# create an instance of ObservationGeoJsonModelList from a dict
observation_geo_json_model_list_from_dict = ObservationGeoJsonModelList.from_dict(observation_geo_json_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


