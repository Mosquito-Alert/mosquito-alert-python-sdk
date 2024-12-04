# ObservationsRetrieveErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_retrieve_error_response400 import ObservationsRetrieveErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsRetrieveErrorResponse400 from a JSON string
observations_retrieve_error_response400_instance = ObservationsRetrieveErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(ObservationsRetrieveErrorResponse400.to_json())

# convert the object into a dict
observations_retrieve_error_response400_dict = observations_retrieve_error_response400_instance.to_dict()
# create an instance of ObservationsRetrieveErrorResponse400 from a dict
observations_retrieve_error_response400_from_dict = ObservationsRetrieveErrorResponse400.from_dict(observations_retrieve_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


