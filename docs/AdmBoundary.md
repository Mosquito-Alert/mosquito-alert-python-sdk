# AdmBoundary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | 
**source** | **str** |  | 
**level** | **int** |  | 

## Example

```python
from mosquito_alert.models.adm_boundary import AdmBoundary

# TODO update the JSON string below
json = "{}"
# create an instance of AdmBoundary from a JSON string
adm_boundary_instance = AdmBoundary.from_json(json)
# print the JSON string representation of the object
print(AdmBoundary.to_json())

# convert the object into a dict
adm_boundary_dict = adm_boundary_instance.to_dict()
# create an instance of AdmBoundary from a dict
adm_boundary_from_dict = AdmBoundary.from_dict(adm_boundary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


