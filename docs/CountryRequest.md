# CountryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_en** | **str** | Full name of the country in English (e.g., Spain). | 
**iso3_code** | **str** | ISO 3166-1 alpha-3 country code (3-letter code, e.g., ESP). | 

## Example

```python
from mosquito_alert.models.country_request import CountryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CountryRequest from a JSON string
country_request_instance = CountryRequest.from_json(json)
# print the JSON string representation of the object
print(CountryRequest.to_json())

# convert the object into a dict
country_request_dict = country_request_instance.to_dict()
# create an instance of CountryRequest from a dict
country_request_from_dict = CountryRequest.from_dict(country_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


