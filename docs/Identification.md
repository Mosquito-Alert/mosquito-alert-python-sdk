# Identification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photo** | [**SimplePhoto**](SimplePhoto.md) |  | 
**num_annotations** | **int** |  | [readonly] 
**result** | [**IdentificationTaskResult**](IdentificationTaskResult.md) |  | [readonly] 
**public_note** | **str** |  | [readonly] 

## Example

```python
from mosquito_alert.models.identification import Identification

# TODO update the JSON string below
json = "{}"
# create an instance of Identification from a JSON string
identification_instance = Identification.from_json(json)
# print the JSON string representation of the object
print(Identification.to_json())

# convert the object into a dict
identification_dict = identification_instance.to_dict()
# create an instance of Identification from a dict
identification_from_dict = Identification.from_dict(identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


