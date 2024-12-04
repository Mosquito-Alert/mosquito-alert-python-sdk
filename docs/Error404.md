# Error404


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | 
**attr** | **str** |  | 

## Example

```python
from mosquito_alert.models.error404 import Error404

# TODO update the JSON string below
json = "{}"
# create an instance of Error404 from a JSON string
error404_instance = Error404.from_json(json)
# print the JSON string representation of the object
print(Error404.to_json())

# convert the object into a dict
error404_dict = error404_instance.to_dict()
# create an instance of Error404 from a dict
error404_from_dict = Error404.from_dict(error404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

