# PartnerPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 

## Example

```python
from mosquito_alert_api.models.partner_point import PartnerPoint

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerPoint from a JSON string
partner_point_instance = PartnerPoint.from_json(json)
# print the JSON string representation of the object
print(PartnerPoint.to_json())

# convert the object into a dict
partner_point_dict = partner_point_instance.to_dict()
# create an instance of PartnerPoint from a dict
partner_point_from_dict = PartnerPoint.from_dict(partner_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


