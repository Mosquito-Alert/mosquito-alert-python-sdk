# TemporaryBoundaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geojson** | **object** |  | 

## Example

```python
from mosquito_alert.models.temporary_boundary_request import TemporaryBoundaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryBoundaryRequest from a JSON string
temporary_boundary_request_instance = TemporaryBoundaryRequest.from_json(json)
# print the JSON string representation of the object
print(TemporaryBoundaryRequest.to_json())

# convert the object into a dict
temporary_boundary_request_dict = temporary_boundary_request_instance.to_dict()
# create an instance of TemporaryBoundaryRequest from a dict
temporary_boundary_request_from_dict = TemporaryBoundaryRequest.from_dict(temporary_boundary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


