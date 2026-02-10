# BreedingSiteGeoJsonModelProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] [readonly] 
**received_at** | **datetime** |  | [optional] [readonly] 
**site_type** | **str** |  | [optional] [readonly] 
**has_water** | **bool** | Either if the user perceived water in the breeding site. | [optional] 

## Example

```python
from mosquito_alert.models.breeding_site_geo_json_model_properties import BreedingSiteGeoJsonModelProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSiteGeoJsonModelProperties from a JSON string
breeding_site_geo_json_model_properties_instance = BreedingSiteGeoJsonModelProperties.from_json(json)
# print the JSON string representation of the object
print(BreedingSiteGeoJsonModelProperties.to_json())

# convert the object into a dict
breeding_site_geo_json_model_properties_dict = breeding_site_geo_json_model_properties_instance.to_dict()
# create an instance of BreedingSiteGeoJsonModelProperties from a dict
breeding_site_geo_json_model_properties_from_dict = BreedingSiteGeoJsonModelProperties.from_dict(breeding_site_geo_json_model_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


