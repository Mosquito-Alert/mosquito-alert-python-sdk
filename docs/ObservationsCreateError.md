# ObservationsCreateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.observations_create_error import ObservationsCreateError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsCreateError from a JSON string
observations_create_error_instance = ObservationsCreateError.from_json(json)
# print the JSON string representation of the object
print(ObservationsCreateError.to_json())

# convert the object into a dict
observations_create_error_dict = observations_create_error_instance.to_dict()
# create an instance of ObservationsCreateError from a dict
observations_create_error_from_dict = ObservationsCreateError.from_dict(observations_create_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


