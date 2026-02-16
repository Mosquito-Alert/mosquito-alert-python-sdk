# CreateOverwriteReviewRequest


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
from mosquito_alert.models.create_overwrite_review_request import CreateOverwriteReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOverwriteReviewRequest from a JSON string
create_overwrite_review_request_instance = CreateOverwriteReviewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOverwriteReviewRequest.to_json())

# convert the object into a dict
create_overwrite_review_request_dict = create_overwrite_review_request_instance.to_dict()
# create an instance of CreateOverwriteReviewRequest from a dict
create_overwrite_review_request_from_dict = CreateOverwriteReviewRequest.from_dict(create_overwrite_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


