# BoundariesCreateTemporaryError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.boundaries_create_temporary_error import BoundariesCreateTemporaryError

# TODO update the JSON string below
json = "{}"
# create an instance of BoundariesCreateTemporaryError from a JSON string
boundaries_create_temporary_error_instance = BoundariesCreateTemporaryError.from_json(json)
# print the JSON string representation of the object
print(BoundariesCreateTemporaryError.to_json())

# convert the object into a dict
boundaries_create_temporary_error_dict = boundaries_create_temporary_error_instance.to_dict()
# create an instance of BoundariesCreateTemporaryError from a dict
boundaries_create_temporary_error_from_dict = BoundariesCreateTemporaryError.from_dict(boundaries_create_temporary_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


