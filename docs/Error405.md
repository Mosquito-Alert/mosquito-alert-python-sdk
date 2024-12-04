# Error405


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | 
**attr** | **str** |  | 

## Example

```python
from mosquito_alert.models.error405 import Error405

# TODO update the JSON string below
json = "{}"
# create an instance of Error405 from a JSON string
error405_instance = Error405.from_json(json)
# print the JSON string representation of the object
print(Error405.to_json())

# convert the object into a dict
error405_dict = error405_instance.to_dict()
# create an instance of Error405 from a dict
error405_from_dict = Error405.from_dict(error405_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


