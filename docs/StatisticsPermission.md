# StatisticsPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **bool** |  | 
**change** | **bool** |  | 
**view** | **bool** |  | 
**delete** | **bool** |  | 

## Example

```python
from mosquito_alert.models.statistics_permission import StatisticsPermission

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsPermission from a JSON string
statistics_permission_instance = StatisticsPermission.from_json(json)
# print the JSON string representation of the object
print(StatisticsPermission.to_json())

# convert the object into a dict
statistics_permission_dict = statistics_permission_instance.to_dict()
# create an instance of StatisticsPermission from a dict
statistics_permission_from_dict = StatisticsPermission.from_dict(statistics_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


