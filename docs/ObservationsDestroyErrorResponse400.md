# ObservationsDestroyErrorResponse400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.observations_destroy_error_response400 import ObservationsDestroyErrorResponse400

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsDestroyErrorResponse400 from a JSON string
observations_destroy_error_response400_instance = ObservationsDestroyErrorResponse400.from_json(json)
# print the JSON string representation of the object
print(ObservationsDestroyErrorResponse400.to_json())

# convert the object into a dict
observations_destroy_error_response400_dict = observations_destroy_error_response400_instance.to_dict()
# create an instance of ObservationsDestroyErrorResponse400 from a dict
observations_destroy_error_response400_from_dict = ObservationsDestroyErrorResponse400.from_dict(observations_destroy_error_response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


