# BreedingSiteGeoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**point** | [**Point**](Point.md) |  | 
**received_at** | **datetime** |  | [readonly] 
**site_type** | **str** |  | [readonly] 
**has_water** | **bool** | Either if the user perceived water in the breeding site. | [optional] 

## Example

```python
from mosquito_alert.models.breeding_site_geo_model import BreedingSiteGeoModel

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSiteGeoModel from a JSON string
breeding_site_geo_model_instance = BreedingSiteGeoModel.from_json(json)
# print the JSON string representation of the object
print(BreedingSiteGeoModel.to_json())

# convert the object into a dict
breeding_site_geo_model_dict = breeding_site_geo_model_instance.to_dict()
# create an instance of BreedingSiteGeoModel from a dict
breeding_site_geo_model_from_dict = BreedingSiteGeoModel.from_dict(breeding_site_geo_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


