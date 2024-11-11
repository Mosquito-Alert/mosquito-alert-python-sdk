# ReportPhotoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**file** | **bytearray** |  | 

## Example

```python
from mosquito_alert_api.models.report_photo_request import ReportPhotoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPhotoRequest from a JSON string
report_photo_request_instance = ReportPhotoRequest.from_json(json)
# print the JSON string representation of the object
print(ReportPhotoRequest.to_json())

# convert the object into a dict
report_photo_request_dict = report_photo_request_instance.to_dict()
# create an instance of ReportPhotoRequest from a dict
report_photo_request_from_dict = ReportPhotoRequest.from_dict(report_photo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


