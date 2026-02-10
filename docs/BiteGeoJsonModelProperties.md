# BiteGeoJsonModelProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] [readonly] 
**received_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from mosquito_alert.models.bite_geo_json_model_properties import BiteGeoJsonModelProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BiteGeoJsonModelProperties from a JSON string
bite_geo_json_model_properties_instance = BiteGeoJsonModelProperties.from_json(json)
# print the JSON string representation of the object
print(BiteGeoJsonModelProperties.to_json())

# convert the object into a dict
bite_geo_json_model_properties_dict = bite_geo_json_model_properties_instance.to_dict()
# create an instance of BiteGeoJsonModelProperties from a dict
bite_geo_json_model_properties_from_dict = BiteGeoJsonModelProperties.from_dict(bite_geo_json_model_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


