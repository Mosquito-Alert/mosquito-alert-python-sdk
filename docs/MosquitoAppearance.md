# MosquitoAppearance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specie** | **str** | The mosquito specie perceived by the user. | [optional] 
**thorax** | **str** | The species of mosquito that the thorax resembles, according to the user. | [optional] 
**abdomen** | **str** | The species of mosquito that the abdomen resembles, according to the user. | [optional] 
**legs** | **str** | The species of mosquito that the leg resembles, according to the user. | [optional] 

## Example

```python
from mosquito_alert.models.mosquito_appearance import MosquitoAppearance

# TODO update the JSON string below
json = "{}"
# create an instance of MosquitoAppearance from a JSON string
mosquito_appearance_instance = MosquitoAppearance.from_json(json)
# print the JSON string representation of the object
print(MosquitoAppearance.to_json())

# convert the object into a dict
mosquito_appearance_dict = mosquito_appearance_instance.to_dict()
# create an instance of MosquitoAppearance from a dict
mosquito_appearance_from_dict = MosquitoAppearance.from_dict(mosquito_appearance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


