# PatchedDeviceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**fcm_token** | **str** |  | [optional] 
**os** | [**DeviceOsRequest**](DeviceOsRequest.md) |  | [optional] 
**mobile_app** | [**MobileAppRequest**](MobileAppRequest.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.patched_device_update_request import PatchedDeviceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDeviceUpdateRequest from a JSON string
patched_device_update_request_instance = PatchedDeviceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDeviceUpdateRequest.to_json())

# convert the object into a dict
patched_device_update_request_dict = patched_device_update_request_instance.to_dict()
# create an instance of PatchedDeviceUpdateRequest from a dict
patched_device_update_request_from_dict = PatchedDeviceUpdateRequest.from_dict(patched_device_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


