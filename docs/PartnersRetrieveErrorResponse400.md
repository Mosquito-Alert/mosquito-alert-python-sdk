# PartnersRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.partners_retrieve_error_response400 import PartnersRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of PartnersRetrieveErrorResponse400 from a JSON string
partners_retrieve_error_response400_instance = PartnersRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(PartnersRetrieveErrorResponse400.to_json())

# convert the object into a dict
partners_retrieve_error_response400_dict = partners_retrieve_error_response400_instance.to_dict()
# create an instance of PartnersRetrieveErrorResponse400 from a dict
partners_retrieve_error_response400_from_dict = PartnersRetrieveErrorResponse400.from_dict(partners_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


