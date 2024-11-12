# ReportLocationPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 

## Example

```python
from mosquito_alert.models.report_location_point import ReportLocationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ReportLocationPoint from a JSON string
report_location_point_instance = ReportLocationPoint.from_json(json)
# print the JSON string representation of the object
print(ReportLocationPoint.to_json())

# convert the object into a dict
report_location_point_dict = report_location_point_instance.to_dict()
# create an instance of ReportLocationPoint from a dict
report_location_point_from_dict = ReportLocationPoint.from_dict(report_location_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


