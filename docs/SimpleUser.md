# SimpleUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**username** | **str** |  | [readonly] 
**first_name** | **str** |  | [readonly] 
**last_name** | **str** |  | [readonly] 
**full_name** | **str** |  | [readonly] 

## Example

```python
from mosquito_alert.models.simple_user import SimpleUser

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleUser from a JSON string
simple_user_instance = SimpleUser.from_json(json)
# print the JSON string representation of the object
print(SimpleUser.to_json())

# convert the object into a dict
simple_user_dict = simple_user_instance.to_dict()
# create an instance of SimpleUser from a dict
simple_user_from_dict = SimpleUser.from_dict(simple_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


