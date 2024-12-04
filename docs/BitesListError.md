# BitesListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.bites_list_error import BitesListError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesListError from a JSON string
bites_list_error_instance = BitesListError.from_json(json)
# print the JSON string representation of the object
print(BitesListError.to_json())

# convert the object into a dict
bites_list_error_dict = bites_list_error_instance.to_dict()
# create an instance of BitesListError from a dict
bites_list_error_from_dict = BitesListError.from_dict(bites_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


