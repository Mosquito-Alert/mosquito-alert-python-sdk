# IdentificationTaskCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review** | **bool** |  | [readonly] 
**annotate** | **bool** |  | [readonly] 
**annotate_executive** | **bool** |  | [readonly] 

## Example

```python
from mosquito_alert.models.identification_task_capabilities import IdentificationTaskCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTaskCapabilities from a JSON string
identification_task_capabilities_instance = IdentificationTaskCapabilities.from_json(json)
# print the JSON string representation of the object
print(IdentificationTaskCapabilities.to_json())

# convert the object into a dict
identification_task_capabilities_dict = identification_task_capabilities_instance.to_dict()
# create an instance of IdentificationTaskCapabilities from a dict
identification_task_capabilities_from_dict = IdentificationTaskCapabilities.from_dict(identification_task_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


