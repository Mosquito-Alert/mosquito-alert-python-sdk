# BreedingSiteGeoJsonModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**features** | [**List[BreedingSiteGeoJsonModel]**](BreedingSiteGeoJsonModel.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.breeding_site_geo_json_model_list import BreedingSiteGeoJsonModelList

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSiteGeoJsonModelList from a JSON string
breeding_site_geo_json_model_list_instance = BreedingSiteGeoJsonModelList.from_json(json)
# print the JSON string representation of the object
print(BreedingSiteGeoJsonModelList.to_json())

# convert the object into a dict
breeding_site_geo_json_model_list_dict = breeding_site_geo_json_model_list_instance.to_dict()
# create an instance of BreedingSiteGeoJsonModelList from a dict
breeding_site_geo_json_model_list_from_dict = BreedingSiteGeoJsonModelList.from_dict(breeding_site_geo_json_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


