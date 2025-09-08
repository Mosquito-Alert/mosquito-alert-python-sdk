# CreateAgreeReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] [default to 'agree']

## Example

```python
from mosquito_alert.models.create_agree_review_request import CreateAgreeReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgreeReviewRequest from a JSON string
create_agree_review_request_instance = CreateAgreeReviewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAgreeReviewRequest.to_json())

# convert the object into a dict
create_agree_review_request_dict = create_agree_review_request_instance.to_dict()
# create an instance of CreateAgreeReviewRequest from a dict
create_agree_review_request_from_dict = CreateAgreeReviewRequest.from_dict(create_agree_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


