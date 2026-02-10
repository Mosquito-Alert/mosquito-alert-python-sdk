# BitesGeoListValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BitesGeoListError]**](BitesGeoListError.md) |  | 

## Example

```python
from mosquito_alert.models.bites_geo_list_validation_error import BitesGeoListValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesGeoListValidationError from a JSON string
bites_geo_list_validation_error_instance = BitesGeoListValidationError.from_json(json)
# print the JSON string representation of the object
print(BitesGeoListValidationError.to_json())

# convert the object into a dict
bites_geo_list_validation_error_dict = bites_geo_list_validation_error_instance.to_dict()
# create an instance of BitesGeoListValidationError from a dict
bites_geo_list_validation_error_from_dict = BitesGeoListValidationError.from_dict(bites_geo_list_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


