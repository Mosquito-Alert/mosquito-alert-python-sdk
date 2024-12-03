# MobileAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** |  | 
**package_version** | **str** |  | 

## Example

```python
from mosquito_alert.models.mobile_app_request import MobileAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppRequest from a JSON string
mobile_app_request_instance = MobileAppRequest.from_json(json)
# print the JSON string representation of the object
print(MobileAppRequest.to_json())

# convert the object into a dict
mobile_app_request_dict = mobile_app_request_instance.to_dict()
# create an instance of MobileAppRequest from a dict
mobile_app_request_from_dict = MobileAppRequest.from_dict(mobile_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


