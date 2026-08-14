# CreateAudienceMessageContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**LocalizedAudienceMessageTitleRequest**](LocalizedAudienceMessageTitleRequest.md) | Provide the message&#39;s title in all supported languages for this audience | 
**body** | [**LocalizedAudienceMessageBodyRequest**](LocalizedAudienceMessageBodyRequest.md) | Provide the message&#39;s body in all supported languages for this audience | 

## Example

```python
from mosquito_alert.models.create_audience_message_content_request import CreateAudienceMessageContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAudienceMessageContentRequest from a JSON string
create_audience_message_content_request_instance = CreateAudienceMessageContentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAudienceMessageContentRequest.to_json())

# convert the object into a dict
create_audience_message_content_request_dict = create_audience_message_content_request_instance.to_dict()
# create an instance of CreateAudienceMessageContentRequest from a dict
create_audience_message_content_request_from_dict = CreateAudienceMessageContentRequest.from_dict(create_audience_message_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


