# Error406


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | 
**attr** | **str** |  | 

## Example

```python
from mosquito_alert.models.error406 import Error406

# TODO update the JSON string below
json = "{}"
# create an instance of Error406 from a JSON string
error406_instance = Error406.from_json(json)
# print the JSON string representation of the object
print(Error406.to_json())

# convert the object into a dict
error406_dict = error406_instance.to_dict()
# create an instance of Error406 from a dict
error406_from_dict = Error406.from_dict(error406_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


