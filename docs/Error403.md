# Error403


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | 
**attr** | **str** |  | 

## Example

```python
from mosquito_alert.models.error403 import Error403

# TODO update the JSON string below
json = "{}"
# create an instance of Error403 from a JSON string
error403_instance = Error403.from_json(json)
# print the JSON string representation of the object
print(Error403.to_json())

# convert the object into a dict
error403_dict = error403_instance.to_dict()
# create an instance of Error403 from a dict
error403_from_dict = Error403.from_dict(error403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


