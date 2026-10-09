# ReportStatsRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**region_id** | **int** |  | [optional] 
**region_code** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**count** | **int** |  | 

## Example

```python
from mosquito_alert.models.report_stats_row import ReportStatsRow

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStatsRow from a JSON string
report_stats_row_instance = ReportStatsRow.from_json(json)
# print the JSON string representation of the object
print(ReportStatsRow.to_json())

# convert the object into a dict
report_stats_row_dict = report_stats_row_instance.to_dict()
# create an instance of ReportStatsRow from a dict
report_stats_row_from_dict = ReportStatsRow.from_dict(report_stats_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


