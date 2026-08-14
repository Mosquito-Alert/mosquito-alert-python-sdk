# CreateAudienceMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**CreateAudienceMessageContentRequest**](CreateAudienceMessageContentRequest.md) | The content of the message for the audience | 
**target** | **str** |  | 
**audience** | [**AudienceFilterRequest**](AudienceFilterRequest.md) | The audience filter for the message | 

## Example

```python
from mosquito_alert.models.create_audience_message_request import CreateAudienceMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAudienceMessageRequest from a JSON string
create_audience_message_request_instance = CreateAudienceMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAudienceMessageRequest.to_json())

# convert the object into a dict
create_audience_message_request_dict = create_audience_message_request_instance.to_dict()
# create an instance of CreateAudienceMessageRequest from a dict
create_audience_message_request_from_dict = CreateAudienceMessageRequest.from_dict(create_audience_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


