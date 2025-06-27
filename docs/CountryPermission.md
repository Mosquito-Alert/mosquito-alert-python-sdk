# CountryPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [readonly] 
**permissions** | [**Permissions**](Permissions.md) |  | [readonly] 
**country** | [**Country**](Country.md) |  | [readonly] 

## Example

```python
from mosquito_alert.models.country_permission import CountryPermission

# TODO update the JSON string below
json = "{}"
# create an instance of CountryPermission from a JSON string
country_permission_instance = CountryPermission.from_json(json)
# print the JSON string representation of the object
print(CountryPermission.to_json())

# convert the object into a dict
country_permission_dict = country_permission_instance.to_dict()
# create an instance of CountryPermission from a dict
country_permission_from_dict = CountryPermission.from_dict(country_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


