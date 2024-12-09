# BitesListMineError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.bites_list_mine_error import BitesListMineError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesListMineError from a JSON string
bites_list_mine_error_instance = BitesListMineError.from_json(json)
# print the JSON string representation of the object
print(BitesListMineError.to_json())

# convert the object into a dict
bites_list_mine_error_dict = bites_list_mine_error_instance.to_dict()
# create an instance of BitesListMineError from a dict
bites_list_mine_error_from_dict = BitesListMineError.from_dict(bites_list_mine_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


