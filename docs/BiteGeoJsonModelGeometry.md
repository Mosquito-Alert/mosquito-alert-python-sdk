# BiteGeoJsonModelGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from mosquito_alert.models.bite_geo_json_model_geometry import BiteGeoJsonModelGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of BiteGeoJsonModelGeometry from a JSON string
bite_geo_json_model_geometry_instance = BiteGeoJsonModelGeometry.from_json(json)
# print the JSON string representation of the object
print(BiteGeoJsonModelGeometry.to_json())

# convert the object into a dict
bite_geo_json_model_geometry_dict = bite_geo_json_model_geometry_instance.to_dict()
# create an instance of BiteGeoJsonModelGeometry from a dict
bite_geo_json_model_geometry_from_dict = BiteGeoJsonModelGeometry.from_dict(bite_geo_json_model_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


