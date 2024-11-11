# BoundingBoxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_min** | **int** | photo bounding box coordinates top left x | 
**y_min** | **int** | photo bounding box coordinates top left y | 
**x_max** | **int** | photo bounding box coordinates bottom right x | 
**y_max** | **int** | photo bounding box coordinates bottom right y | 

## Example

```python
from mosquito_alert_api.models.bounding_box_request import BoundingBoxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BoundingBoxRequest from a JSON string
bounding_box_request_instance = BoundingBoxRequest.from_json(json)
# print the JSON string representation of the object
print(BoundingBoxRequest.to_json())

# convert the object into a dict
bounding_box_request_dict = bounding_box_request_instance.to_dict()
# create an instance of BoundingBoxRequest from a dict
bounding_box_request_from_dict = BoundingBoxRequest.from_dict(bounding_box_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


