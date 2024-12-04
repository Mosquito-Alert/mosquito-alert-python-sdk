# BreedingSitesListErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.breeding_sites_list_error_response400 import BreedingSitesListErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSitesListErrorResponse400 from a JSON string
breeding_sites_list_error_response400_instance = BreedingSitesListErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(BreedingSitesListErrorResponse400.to_json())

# convert the object into a dict
breeding_sites_list_error_response400_dict = breeding_sites_list_error_response400_instance.to_dict()
# create an instance of BreedingSitesListErrorResponse400 from a dict
breeding_sites_list_error_response400_from_dict = BreedingSitesListErrorResponse400.from_dict(breeding_sites_list_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


