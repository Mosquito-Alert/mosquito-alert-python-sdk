# Error500


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | 
**attr** | **str** |  | 

## Example

```python
from mosquito_alert.models.error500 import Error500

# TODO update the JSON string below
json = "{}"
# create an instance of Error500 from a JSON string
error500_instance = Error500.from_json(json)
# print the JSON string representation of the object
print(Error500.to_json())

# convert the object into a dict
error500_dict = error500_instance.to_dict()
# create an instance of Error500 from a dict
error500_from_dict = Error500.from_dict(error500_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


