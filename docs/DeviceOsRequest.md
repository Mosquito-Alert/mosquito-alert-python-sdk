# DeviceOsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Operating system of device from which this report was submitted. | 
**version** | **str** | Operating system version of device from which this report was submitted. | 
**locale** | **str** | The locale configured in the device following the BCP 47 standard in &#39;language&#39; or &#39;language-region&#39; format (e.g., &#39;en&#39; for English, &#39;en-US&#39; for English (United States), &#39;fr&#39; for French). The language is a two-letter ISO 639-1 code, and the region is an optional two-letter ISO 3166-1 alpha-2 code. | [optional] 

## Example

```python
from mosquito_alert.models.device_os_request import DeviceOsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOsRequest from a JSON string
device_os_request_instance = DeviceOsRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceOsRequest.to_json())

# convert the object into a dict
device_os_request_dict = device_os_request_instance.to_dict()
# create an instance of DeviceOsRequest from a dict
device_os_request_from_dict = DeviceOsRequest.from_dict(device_os_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


