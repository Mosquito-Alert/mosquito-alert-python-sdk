# NutsAdmBoundariesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nuts2** | **str** | Basic regions for economic applications (e.g., Spanish autonomous communities). | 
**nuts3** | **str** | Small regions for specific analyses (e.g., French départements). | 

## Example

```python
from mosquito_alert.models.nuts_adm_boundaries_request import NutsAdmBoundariesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NutsAdmBoundariesRequest from a JSON string
nuts_adm_boundaries_request_instance = NutsAdmBoundariesRequest.from_json(json)
# print the JSON string representation of the object
print(NutsAdmBoundariesRequest.to_json())

# convert the object into a dict
nuts_adm_boundaries_request_dict = nuts_adm_boundaries_request_instance.to_dict()
# create an instance of NutsAdmBoundariesRequest from a dict
nuts_adm_boundaries_request_from_dict = NutsAdmBoundariesRequest.from_dict(nuts_adm_boundaries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


