# DeviceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Unique device identifier | [readonly] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [readonly] 
**manufacturer** | **str** | The manufacturer of the device. | [readonly] 
**model** | **str** | The end-user-visible name for the end product. | [readonly] 
**os** | [**DeviceOs**](DeviceOs.md) |  | 
**mobile_app** | [**MobileApp**](MobileApp.md) |  | [optional] 
**user_uuid** | **UUID** |  | [readonly] 
**last_login** | **datetime** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.device_update import DeviceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUpdate from a JSON string
device_update_instance = DeviceUpdate.from_json(json)
# print the JSON string representation of the object
print(DeviceUpdate.to_json())

# convert the object into a dict
device_update_dict = device_update_instance.to_dict()
# create an instance of DeviceUpdate from a dict
device_update_from_dict = DeviceUpdate.from_dict(device_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


