# IdentificationTaskReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert.models.identification_task_review import IdentificationTaskReview

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTaskReview from a JSON string
identification_task_review_instance = IdentificationTaskReview.from_json(json)
# print the JSON string representation of the object
print(IdentificationTaskReview.to_json())

# convert the object into a dict
identification_task_review_dict = identification_task_review_instance.to_dict()
# create an instance of IdentificationTaskReview from a dict
identification_task_review_from_dict = IdentificationTaskReview.from_dict(identification_task_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


