# SimplifiedObservationWithPhotos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**short_id** | **str** |  | [readonly] 
**user_uuid** | **str** |  | [readonly] 
**created_at** | **datetime** |  | 
**created_at_local** | **datetime** | The date and time when the record was created, displayed in the local timezone specified for this entry. | [readonly] 
**received_at** | **datetime** |  | [readonly] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**photos** | [**List[SimplePhoto]**](SimplePhoto.md) |  | 

## Example

```python
from mosquito_alert.models.simplified_observation_with_photos import SimplifiedObservationWithPhotos

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedObservationWithPhotos from a JSON string
simplified_observation_with_photos_instance = SimplifiedObservationWithPhotos.from_json(json)
# print the JSON string representation of the object
print(SimplifiedObservationWithPhotos.to_json())

# convert the object into a dict
simplified_observation_with_photos_dict = simplified_observation_with_photos_instance.to_dict()
# create an instance of SimplifiedObservationWithPhotos from a dict
simplified_observation_with_photos_from_dict = SimplifiedObservationWithPhotos.from_dict(simplified_observation_with_photos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


