# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **str** | Manufacturer of device from which this report was submitted. | [optional] 
**model** | **str** | Model of device from which this report was submitted. | [optional] 
**os** | **str** | Operating system of device from which this report was submitted. | [optional] 
**os_version** | **str** | Operating system version of device from which this report was submitted. | [optional] 
**os_language** | **str** | Language setting of operating system on device from which this report was submitted. 2-digit ISO-639-1 language code. | [optional] 

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


