# BitesListMineValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[BitesListMineError]**](BitesListMineError.md) |  | 

## Example

```python
from mosquito_alert.models.bites_list_mine_validation_error import BitesListMineValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of BitesListMineValidationError from a JSON string
bites_list_mine_validation_error_instance = BitesListMineValidationError.from_json(json)
# print the JSON string representation of the object
print(BitesListMineValidationError.to_json())

# convert the object into a dict
bites_list_mine_validation_error_dict = bites_list_mine_validation_error_instance.to_dict()
# create an instance of BitesListMineValidationError from a dict
bites_list_mine_validation_error_from_dict = BitesListMineValidationError.from_dict(bites_list_mine_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


