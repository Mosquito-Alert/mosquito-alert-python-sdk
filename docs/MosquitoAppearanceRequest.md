# MosquitoAppearanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specie** | **str** | The mosquito specie perceived by the user. | [optional] 
**thorax** | **str** | The species of mosquito that the thorax resembles, according to the user. | [optional] 
**abdomen** | **str** | The species of mosquito that the abdomen resembles, according to the user. | [optional] 
**legs** | **str** | The species of mosquito that the leg resembles, according to the user. | [optional] 

## Example

```python
from mosquito_alert.models.mosquito_appearance_request import MosquitoAppearanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MosquitoAppearanceRequest from a JSON string
mosquito_appearance_request_instance = MosquitoAppearanceRequest.from_json(json)
# print the JSON string representation of the object
print(MosquitoAppearanceRequest.to_json())

# convert the object into a dict
mosquito_appearance_request_dict = mosquito_appearance_request_instance.to_dict()
# create an instance of MosquitoAppearanceRequest from a dict
mosquito_appearance_request_from_dict = MosquitoAppearanceRequest.from_dict(mosquito_appearance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


