# ParseErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**errors** | [**List[ParseError]**](ParseError.md) |  | 

## Example

```python
from mosquito_alert.models.parse_error_response import ParseErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParseErrorResponse from a JSON string
parse_error_response_instance = ParseErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ParseErrorResponse.to_json())

# convert the object into a dict
parse_error_response_dict = parse_error_response_instance.to_dict()
# create an instance of ParseErrorResponse from a dict
parse_error_response_from_dict = ParseErrorResponse.from_dict(parse_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


