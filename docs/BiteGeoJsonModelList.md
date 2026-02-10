# BiteGeoJsonModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**features** | [**List[BiteGeoJsonModel]**](BiteGeoJsonModel.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.bite_geo_json_model_list import BiteGeoJsonModelList

# TODO update the JSON string below
json = "{}"
# create an instance of BiteGeoJsonModelList from a JSON string
bite_geo_json_model_list_instance = BiteGeoJsonModelList.from_json(json)
# print the JSON string representation of the object
print(BiteGeoJsonModelList.to_json())

# convert the object into a dict
bite_geo_json_model_list_dict = bite_geo_json_model_list_instance.to_dict()
# create an instance of BiteGeoJsonModelList from a dict
bite_geo_json_model_list_from_dict = BiteGeoJsonModelList.from_dict(bite_geo_json_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


