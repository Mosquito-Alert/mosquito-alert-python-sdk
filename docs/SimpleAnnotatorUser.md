# SimpleAnnotatorUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**username** | **str** |  | [readonly] 
**first_name** | **str** |  | [readonly] 
**last_name** | **str** |  | [readonly] 
**full_name** | **str** |  | [readonly] 

## Example

```python
from mosquito_alert.models.simple_annotator_user import SimpleAnnotatorUser

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAnnotatorUser from a JSON string
simple_annotator_user_instance = SimpleAnnotatorUser.from_json(json)
# print the JSON string representation of the object
print(SimpleAnnotatorUser.to_json())

# convert the object into a dict
simple_annotator_user_dict = simple_annotator_user_instance.to_dict()
# create an instance of SimpleAnnotatorUser from a dict
simple_annotator_user_from_dict = SimpleAnnotatorUser.from_dict(simple_annotator_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


