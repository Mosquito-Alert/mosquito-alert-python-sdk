# IdentificationTaskResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 

## Example

```python
from mosquito_alert.models.identification_task_result_request import IdentificationTaskResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationTaskResultRequest from a JSON string
identification_task_result_request_instance = IdentificationTaskResultRequest.from_json(json)
# print the JSON string representation of the object
print(IdentificationTaskResultRequest.to_json())

# convert the object into a dict
identification_task_result_request_dict = identification_task_result_request_instance.to_dict()
# create an instance of IdentificationTaskResultRequest from a dict
identification_task_result_request_from_dict = IdentificationTaskResultRequest.from_dict(identification_task_result_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


