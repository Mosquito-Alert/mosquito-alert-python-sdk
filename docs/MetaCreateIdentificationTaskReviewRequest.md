# MetaCreateIdentificationTaskReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] [default to 'overwrite']
**public_photo_uuid** | **UUID** |  | 
**is_safe** | **bool** | Indicates if the content is safe for publication. | 
**public_note** | **str** |  | 
**classification** | [**SpeciesClassificationRequest**](SpeciesClassificationRequest.md) |  | 
**characteristics** | [**SpeciesCharacteristicsRequest**](SpeciesCharacteristicsRequest.md) |  | [optional] 

## Example

```python
from mosquito_alert.models.meta_create_identification_task_review_request import MetaCreateIdentificationTaskReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetaCreateIdentificationTaskReviewRequest from a JSON string
meta_create_identification_task_review_request_instance = MetaCreateIdentificationTaskReviewRequest.from_json(json)
# print the JSON string representation of the object
print(MetaCreateIdentificationTaskReviewRequest.to_json())

# convert the object into a dict
meta_create_identification_task_review_request_dict = meta_create_identification_task_review_request_instance.to_dict()
# create an instance of MetaCreateIdentificationTaskReviewRequest from a dict
meta_create_identification_task_review_request_from_dict = MetaCreateIdentificationTaskReviewRequest.from_dict(meta_create_identification_task_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


