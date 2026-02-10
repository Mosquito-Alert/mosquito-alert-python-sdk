# BreedingSiteGeoJsonModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**geometry** | [**BiteGeoJsonModelGeometry**](BiteGeoJsonModelGeometry.md) |  | [optional] 
**properties** | [**BreedingSiteGeoJsonModelProperties**](BreedingSiteGeoJsonModelProperties.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.breeding_site_geo_json_model import BreedingSiteGeoJsonModel

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSiteGeoJsonModel from a JSON string
breeding_site_geo_json_model_instance = BreedingSiteGeoJsonModel.from_json(json)
# print the JSON string representation of the object
print(BreedingSiteGeoJsonModel.to_json())

# convert the object into a dict
breeding_site_geo_json_model_dict = breeding_site_geo_json_model_instance.to_dict()
# create an instance of BreedingSiteGeoJsonModel from a dict
breeding_site_geo_json_model_from_dict = BreedingSiteGeoJsonModel.from_dict(breeding_site_geo_json_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


