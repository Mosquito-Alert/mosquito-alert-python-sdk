# TokenVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from mosquito_alert.models.token_verify_request import TokenVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenVerifyRequest from a JSON string
token_verify_request_instance = TokenVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(TokenVerifyRequest.to_json())

# convert the object into a dict
token_verify_request_dict = token_verify_request_instance.to_dict()
# create an instance of TokenVerifyRequest from a dict
token_verify_request_from_dict = TokenVerifyRequest.from_dict(token_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


