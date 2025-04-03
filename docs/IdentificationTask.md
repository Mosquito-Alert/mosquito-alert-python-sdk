# IdentificationTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observation** | [**SimplifiedObservation**](SimplifiedObservation.md) |  | [readonly] 
**public_photo** | [**SimplePhoto**](SimplePhoto.md) |  | 
**assignees_ids** | **List[int]** |  | [readonly] 
**status** | **str** |  | [optional] [default to 'open']
**is_flagged** | **bool** |  | [readonly] 
**is_safe** | **bool** | Indicates if the content is safe for publication. | [readonly] 
**public_note** | **str** |  | [readonly] 
**num_assignations** | **int** |  | [readonly] 
**num_annotations** | **int** |  | [readonly] 
**revision** | [**IdentificationTaskRevision**](IdentificationTaskRevision.md) |  | [readonly] 
**result** | [**IdentificationTaskResult**](IdentificationTaskResult.md) |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.identification_task import IdentificationTask

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTask from a JSON string
identification_task_instance = IdentificationTask.from_json(json)
# print the JSON string representation of the object
print(IdentificationTask.to_json())

# convert the object into a dict
identification_task_dict = identification_task_instance.to_dict()
# create an instance of IdentificationTask from a dict
identification_task_from_dict = IdentificationTask.from_dict(identification_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


