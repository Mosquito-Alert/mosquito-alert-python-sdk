# DeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Unique device identifier | 
**name** | **str** |  | [optional] 
**fcm_token** | **str** |  | 
**type** | **str** |  | 
**manufacturer** | **str** | The manufacturer of the device. | [optional] 
**model** | **str** | The end-user-visible name for the end product. | 
**os** | [**DeviceOsRequest**](DeviceOsRequest.md) |  | 
**mobile_app** | [**MobileAppRequest**](MobileAppRequest.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.device_request import DeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRequest from a JSON string
device_request_instance = DeviceRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceRequest.to_json())

# convert the object into a dict
device_request_dict = device_request_instance.to_dict()
# create an instance of DeviceRequest from a dict
device_request_from_dict = DeviceRequest.from_dict(device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


