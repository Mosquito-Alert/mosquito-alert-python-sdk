# ObservationsCreateTagsErrorComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.observations_create_tags_error_component import ObservationsCreateTagsErrorComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationsCreateTagsErrorComponent from a JSON string
observations_create_tags_error_component_instance = ObservationsCreateTagsErrorComponent.from_json(json)
# print the JSON string representation of the object
print(ObservationsCreateTagsErrorComponent.to_json())

# convert the object into a dict
observations_create_tags_error_component_dict = observations_create_tags_error_component_instance.to_dict()
# create an instance of ObservationsCreateTagsErrorComponent from a dict
observations_create_tags_error_component_from_dict = ObservationsCreateTagsErrorComponent.from_dict(observations_create_tags_error_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


