# BiteGeoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**point** | [**Point**](Point.md) |  | 
**received_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.bite_geo_model import BiteGeoModel

# TODO update the JSON string below
json = "{}"
# create an instance of BiteGeoModel from a JSON string
bite_geo_model_instance = BiteGeoModel.from_json(json)
# print the JSON string representation of the object
print(BiteGeoModel.to_json())

# convert the object into a dict
bite_geo_model_dict = bite_geo_model_instance.to_dict()
# create an instance of BiteGeoModel from a dict
bite_geo_model_from_dict = BiteGeoModel.from_dict(bite_geo_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


