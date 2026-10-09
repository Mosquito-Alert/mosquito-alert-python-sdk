# ReportStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ReportStatsMeta**](ReportStatsMeta.md) |  | 
**data** | [**List[ReportStatsRow]**](ReportStatsRow.md) |  | 

## Example

```python
from mosquito_alert.models.report_stats_response import ReportStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStatsResponse from a JSON string
report_stats_response_instance = ReportStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ReportStatsResponse.to_json())

# convert the object into a dict
report_stats_response_dict = report_stats_response_instance.to_dict()
# create an instance of ReportStatsResponse from a dict
report_stats_response_from_dict = ReportStatsResponse.from_dict(report_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


