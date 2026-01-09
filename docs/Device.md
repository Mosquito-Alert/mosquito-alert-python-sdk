# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Unique device identifier | 
**name** | **str** |  | [optional] 
**type** | **str** |  | 
**manufacturer** | **str** | The manufacturer of the device. | [optional] 
**model** | **str** | The end-user-visible name for the end product. | 
**os** | [**DeviceOs**](DeviceOs.md) |  | 
**mobile_app** | [**MobileApp**](MobileApp.md) |  | [optional] 
**user_uuid** | **UUID** |  | [readonly] 
**last_login** | **datetime** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


