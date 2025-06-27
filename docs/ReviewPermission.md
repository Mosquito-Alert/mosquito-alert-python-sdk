# ReviewPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **bool** |  | 
**change** | **bool** |  | 
**view** | **bool** |  | 
**delete** | **bool** |  | 

## Example

```python
from mosquito_alert.models.review_permission import ReviewPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewPermission from a JSON string
review_permission_instance = ReviewPermission.from_json(json)
# print the JSON string representation of the object
print(ReviewPermission.to_json())

# convert the object into a dict
review_permission_dict = review_permission_instance.to_dict()
# create an instance of ReviewPermission from a dict
review_permission_from_dict = ReviewPermission.from_dict(review_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


