# NutsAdmBoundaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nuts2** | **str** | Basic regions for economic applications (e.g., Spanish autonomous communities). | 
**nuts3** | **str** | Small regions for specific analyses (e.g., French départements). | 

## Example

```python
from mosquito_alert.models.nuts_adm_boundaries import NutsAdmBoundaries

# TODO update the JSON string below
json = "{}"
# create an instance of NutsAdmBoundaries from a JSON string
nuts_adm_boundaries_instance = NutsAdmBoundaries.from_json(json)
# print the JSON string representation of the object
print(NutsAdmBoundaries.to_json())

# convert the object into a dict
nuts_adm_boundaries_dict = nuts_adm_boundaries_instance.to_dict()
# create an instance of NutsAdmBoundaries from a dict
nuts_adm_boundaries_from_dict = NutsAdmBoundaries.from_dict(nuts_adm_boundaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


