# BitesGeoListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.bites_geo_list_error import BitesGeoListError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesGeoListError from a JSON string
bites_geo_list_error_instance = BitesGeoListError.from_json(json)
# print the JSON string representation of the object
print(BitesGeoListError.to_json())

# convert the object into a dict
bites_geo_list_error_dict = bites_geo_list_error_instance.to_dict()
# create an instance of BitesGeoListError from a dict
bites_geo_list_error_from_dict = BitesGeoListError.from_dict(bites_geo_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


