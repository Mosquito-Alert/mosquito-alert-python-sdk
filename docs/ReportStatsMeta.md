# ReportStatsMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **List[str]** |  | 
**interval** | **str** |  | [optional] 
**cumulative** | **bool** |  | [optional] 
**level** | **int** |  | [optional] 
**area** | [**AreaMeta**](AreaMeta.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.report_stats_meta import ReportStatsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStatsMeta from a JSON string
report_stats_meta_instance = ReportStatsMeta.from_json(json)
# print the JSON string representation of the object
print(ReportStatsMeta.to_json())

# convert the object into a dict
report_stats_meta_dict = report_stats_meta_instance.to_dict()
# create an instance of ReportStatsMeta from a dict
report_stats_meta_from_dict = ReportStatsMeta.from_dict(report_stats_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


