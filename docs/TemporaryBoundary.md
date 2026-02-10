# TemporaryBoundary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**expires_in** | **int** | Time in seconds until this cached boundary expires. | [readonly] 

## Example

```python
from mosquito_alert.models.temporary_boundary import TemporaryBoundary

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryBoundary from a JSON string
temporary_boundary_instance = TemporaryBoundary.from_json(json)
# print the JSON string representation of the object
print(TemporaryBoundary.to_json())

# convert the object into a dict
temporary_boundary_dict = temporary_boundary_instance.to_dict()
# create an instance of TemporaryBoundary from a dict
temporary_boundary_from_dict = TemporaryBoundary.from_dict(temporary_boundary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


