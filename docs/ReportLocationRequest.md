# ReportLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Did user indicate that report relates to current location of phone (&#39;current&#39;) or to a location selected manually on the map (&#39;selected&#39;)? Or is the choice missing (&#39;missing&#39;) | 
**point** | [**ReportLocationPoint**](ReportLocationPoint.md) |  | 

## Example

```python
from mosquito_alert.models.report_location_request import ReportLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportLocationRequest from a JSON string
report_location_request_instance = ReportLocationRequest.from_json(json)
# print the JSON string representation of the object
print(ReportLocationRequest.to_json())

# convert the object into a dict
report_location_request_dict = report_location_request_instance.to_dict()
# create an instance of ReportLocationRequest from a dict
report_location_request_from_dict = ReportLocationRequest.from_dict(report_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


