# BreedingSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**short_id** | **str** |  | [readonly] 
**user_uuid** | **str** |  | [readonly] 
**created_at** | **datetime** |  | 
**created_at_local** | **datetime** | The date and time when the record was created, displayed in the local timezone specified for this entry. | [readonly] 
**sent_at** | **datetime** |  | 
**received_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** | Date and time when the report was last modified | [readonly] 
**location** | [**Location**](Location.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**published** | **bool** |  | [readonly] 
**photos** | [**List[SimplePhoto]**](SimplePhoto.md) |  | 
**site_type** | **str** | Breeding site type. | [optional] 
**has_water** | **bool** | Either if the user perceived water in the breeding site. | [optional] 
**in_public_area** | **bool** | Either if the breeding site is found in a public area. | [optional] 
**has_near_mosquitoes** | **bool** | Either if the user perceived mosquitoes near the breeding site (less than 10 meters). | [optional] 
**has_larvae** | **bool** | Either if the user perceived larvaes the breeding site. | [optional] 

## Example

```python
from mosquito_alert.models.breeding_site import BreedingSite

# TODO update the JSON string below
json = "{}"
# create an instance of BreedingSite from a JSON string
breeding_site_instance = BreedingSite.from_json(json)
# print the JSON string representation of the object
print(BreedingSite.to_json())

# convert the object into a dict
breeding_site_dict = breeding_site_instance.to_dict()
# create an instance of BreedingSite from a dict
breeding_site_from_dict = BreedingSite.from_dict(breeding_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


