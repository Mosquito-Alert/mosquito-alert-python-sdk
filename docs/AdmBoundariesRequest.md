# AdmBoundariesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nuts** | [**NutsAdmBoundariesRequest**](NutsAdmBoundariesRequest.md) | NUTS (Nomenclature of Territorial Units for Statistics). A hierarchical system used by the European Union to divide its territory into comparable regions for statistical purposes. | [optional] 

## Example

```python
from mosquito_alert.models.adm_boundaries_request import AdmBoundariesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdmBoundariesRequest from a JSON string
adm_boundaries_request_instance = AdmBoundariesRequest.from_json(json)
# print the JSON string representation of the object
print(AdmBoundariesRequest.to_json())

# convert the object into a dict
adm_boundaries_request_dict = adm_boundaries_request_instance.to_dict()
# create an instance of AdmBoundariesRequest from a dict
adm_boundaries_request_from_dict = AdmBoundariesRequest.from_dict(adm_boundaries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


