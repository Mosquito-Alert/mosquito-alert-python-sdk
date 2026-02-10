# BiteGeoJsonModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **UUID** |  | [optional] [readonly] 
**geometry** | [**BiteGeoJsonModelGeometry**](BiteGeoJsonModelGeometry.md) |  | [optional] 
**properties** | [**BiteGeoJsonModelProperties**](BiteGeoJsonModelProperties.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.bite_geo_json_model import BiteGeoJsonModel

# TODO update the JSON string below
json = "{}"
# create an instance of BiteGeoJsonModel from a JSON string
bite_geo_json_model_instance = BiteGeoJsonModel.from_json(json)
# print the JSON string representation of the object
print(BiteGeoJsonModel.to_json())

# convert the object into a dict
bite_geo_json_model_dict = bite_geo_json_model_instance.to_dict()
# create an instance of BiteGeoJsonModel from a dict
bite_geo_json_model_from_dict = BiteGeoJsonModel.from_dict(bite_geo_json_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


