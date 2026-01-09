# SimplePhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**url** | **str** | URL of the photo associated with the item. Note: This URL may change over time. Do not rely on it for permanent storage. | [readonly] 

## Example

```python
from mosquito_alert.models.simple_photo import SimplePhoto

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePhoto from a JSON string
simple_photo_instance = SimplePhoto.from_json(json)
# print the JSON string representation of the object
print(SimplePhoto.to_json())

# convert the object into a dict
simple_photo_dict = simple_photo_instance.to_dict()
# create an instance of SimplePhoto from a dict
simple_photo_from_dict = SimplePhoto.from_dict(simple_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


