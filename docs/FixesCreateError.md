# FixesCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.fixes_create_error import FixesCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of FixesCreateError from a JSON string
fixes_create_error_instance = FixesCreateError.from_json(json)
# print the JSON string representation of the object
print(FixesCreateError.to_json())

# convert the object into a dict
fixes_create_error_dict = fixes_create_error_instance.to_dict()
# create an instance of FixesCreateError from a dict
fixes_create_error_from_dict = FixesCreateError.from_dict(fixes_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


