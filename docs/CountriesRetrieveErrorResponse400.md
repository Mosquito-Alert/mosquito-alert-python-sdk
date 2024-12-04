# CountriesRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.countries_retrieve_error_response400 import CountriesRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of CountriesRetrieveErrorResponse400 from a JSON string
countries_retrieve_error_response400_instance = CountriesRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(CountriesRetrieveErrorResponse400.to_json())

# convert the object into a dict
countries_retrieve_error_response400_dict = countries_retrieve_error_response400_instance.to_dict()
# create an instance of CountriesRetrieveErrorResponse400 from a dict
countries_retrieve_error_response400_from_dict = CountriesRetrieveErrorResponse400.from_dict(countries_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


