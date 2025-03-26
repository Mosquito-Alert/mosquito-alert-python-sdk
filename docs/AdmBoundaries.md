# AdmBoundaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nuts** | [**NutsAdmBoundaries**](NutsAdmBoundaries.md) | NUTS (Nomenclature of Territorial Units for Statistics). A hierarchical system used by the European Union to divide its territory into comparable regions for statistical purposes. | [optional] 

## Example

```python
from mosquito_alert.models.adm_boundaries import AdmBoundaries

# TODO update the JSON string below
json = "{}"
# create an instance of AdmBoundaries from a JSON string
adm_boundaries_instance = AdmBoundaries.from_json(json)
# print the JSON string representation of the object
print(AdmBoundaries.to_json())

# convert the object into a dict
adm_boundaries_dict = adm_boundaries_instance.to_dict()
# create an instance of AdmBoundaries from a dict
adm_boundaries_from_dict = AdmBoundaries.from_dict(adm_boundaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


