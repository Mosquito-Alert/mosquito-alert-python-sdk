# AdmBoundaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | 
**source** | **str** |  | 
**level** | **int** |  | 

## Example

```python
from mosquito_alert.models.adm_boundary_request import AdmBoundaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdmBoundaryRequest from a JSON string
adm_boundary_request_instance = AdmBoundaryRequest.from_json(json)
# print the JSON string representation of the object
print(AdmBoundaryRequest.to_json())

# convert the object into a dict
adm_boundary_request_dict = adm_boundary_request_instance.to_dict()
# create an instance of AdmBoundaryRequest from a dict
adm_boundary_request_from_dict = AdmBoundaryRequest.from_dict(adm_boundary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


