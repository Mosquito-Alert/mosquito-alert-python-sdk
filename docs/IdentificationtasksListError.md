# IdentificationtasksListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attr** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from mosquito_alert.models.identificationtasks_list_error import IdentificationtasksListError

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationtasksListError from a JSON string
identificationtasks_list_error_instance = IdentificationtasksListError.from_json(json)
# print the JSON string representation of the object
print(IdentificationtasksListError.to_json())

# convert the object into a dict
identificationtasks_list_error_dict = identificationtasks_list_error_instance.to_dict()
# create an instance of IdentificationtasksListError from a dict
identificationtasks_list_error_from_dict = IdentificationtasksListError.from_dict(identificationtasks_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


