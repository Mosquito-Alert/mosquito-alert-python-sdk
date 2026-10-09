# AreaMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | 
**id** | **str** |  | 
**code** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from mosquito_alert.models.area_meta import AreaMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AreaMeta from a JSON string
area_meta_instance = AreaMeta.from_json(json)
# print the JSON string representation of the object
print(AreaMeta.to_json())

# convert the object into a dict
area_meta_dict = area_meta_instance.to_dict()
# create an instance of AreaMeta from a dict
area_meta_from_dict = AreaMeta.from_dict(area_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


