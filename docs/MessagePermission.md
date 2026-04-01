# MessagePermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **bool** |  | 
**change** | **bool** |  | 
**view** | **bool** |  | 
**delete** | **bool** |  | 

## Example

```python
from mosquito_alert.models.message_permission import MessagePermission

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePermission from a JSON string
message_permission_instance = MessagePermission.from_json(json)
# print the JSON string representation of the object
print(MessagePermission.to_json())

# convert the object into a dict
message_permission_dict = message_permission_instance.to_dict()
# create an instance of MessagePermission from a dict
message_permission_from_dict = MessagePermission.from_dict(message_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


