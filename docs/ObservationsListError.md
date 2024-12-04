# ObservationsListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.observations_list_error import ObservationsListError

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsListError from a JSON string
observations_list_error_instance = ObservationsListError.from_json(json)
# print the JSON string representation of the object
print(ObservationsListError.to_json())

# convert the object into a dict
observations_list_error_dict = observations_list_error_instance.to_dict()
# create an instance of ObservationsListError from a dict
observations_list_error_from_dict = ObservationsListError.from_dict(observations_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


