# PaginatedReportStatsResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ReportStatsResponse]**](ReportStatsResponse.md) |  | 

## Example

```python
from mosquito_alert.models.paginated_report_stats_response_list import PaginatedReportStatsResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedReportStatsResponseList from a JSON string
paginated_report_stats_response_list_instance = PaginatedReportStatsResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedReportStatsResponseList.to_json())

# convert the object into a dict
paginated_report_stats_response_list_dict = paginated_report_stats_response_list_instance.to_dict()
# create an instance of PaginatedReportStatsResponseList from a dict
paginated_report_stats_response_list_from_dict = PaginatedReportStatsResponseList.from_dict(paginated_report_stats_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


