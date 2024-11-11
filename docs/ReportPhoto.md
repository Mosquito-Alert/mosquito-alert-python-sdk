# ReportPhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**url** | **str** | URL of the photo associated with the item. Note: This URL may change over time. Do not rely on it for permanent storage. | [readonly] 

## Example

```python
from mosquito_alert_api.models.report_photo import ReportPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPhoto from a JSON string
report_photo_instance = ReportPhoto.from_json(json)
# print the JSON string representation of the object
print(ReportPhoto.to_json())

# convert the object into a dict
report_photo_dict = report_photo_instance.to_dict()
# create an instance of ReportPhoto from a dict
report_photo_from_dict = ReportPhoto.from_dict(report_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


