# BitesCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.bites_create_error import BitesCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesCreateError from a JSON string
bites_create_error_instance = BitesCreateError.from_json(json)
# print the JSON string representation of the object
print(BitesCreateError.to_json())

# convert the object into a dict
bites_create_error_dict = bites_create_error_instance.to_dict()
# create an instance of BitesCreateError from a dict
bites_create_error_from_dict = BitesCreateError.from_dict(bites_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


