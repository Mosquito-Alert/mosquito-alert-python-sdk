# MetaCreateMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**CreateAudienceMessageContentRequest**](CreateAudienceMessageContentRequest.md) | The content of the message for the audience | 
**target** | **str** |  | 
**user_uuids** | **List[UUID]** |  | 
**audience** | [**AudienceFilterRequest**](AudienceFilterRequest.md) | The audience filter for the message | 

## Example

```python
from mosquito_alert.models.meta_create_message_request import MetaCreateMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetaCreateMessageRequest from a JSON string
meta_create_message_request_instance = MetaCreateMessageRequest.from_json(json)
# print the JSON string representation of the object
print(MetaCreateMessageRequest.to_json())

# convert the object into a dict
meta_create_message_request_dict = meta_create_message_request_instance.to_dict()
# create an instance of MetaCreateMessageRequest from a dict
meta_create_message_request_from_dict = MetaCreateMessageRequest.from_dict(meta_create_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


