# IdentificationTaskRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.identification_task_revision import IdentificationTaskRevision

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTaskRevision from a JSON string
identification_task_revision_instance = IdentificationTaskRevision.from_json(json)
# print the JSON string representation of the object
print(IdentificationTaskRevision.to_json())

# convert the object into a dict
identification_task_revision_dict = identification_task_revision_instance.to_dict()
# create an instance of IdentificationTaskRevision from a dict
identification_task_revision_from_dict = IdentificationTaskRevision.from_dict(identification_task_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


