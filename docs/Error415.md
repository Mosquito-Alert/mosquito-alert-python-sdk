# Error415


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | 
**attr** | **str** |  | 

## Example

```python
from mosquito_alert.models.error415 import Error415

# TODO update the JSON string below
json = "{}"
# create an instance of Error415 from a JSON string
error415_instance = Error415.from_json(json)
# print the JSON string representation of the object
print(Error415.to_json())

# convert the object into a dict
error415_dict = error415_instance.to_dict()
# create an instance of Error415 from a dict
error415_from_dict = Error415.from_dict(error415_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


