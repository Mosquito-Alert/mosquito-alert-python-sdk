# Bite


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
**event_environment** | **str** | The environment where the event took place. | [optional] 
**event_moment** | **str** | The moment of the day when the event took place. | [optional] 
**counts** | [**BiteCounts**](BiteCounts.md) |  | 

## Example

```python
from mosquito_alert.models.bite import Bite

# TODO update the JSON string below
json = "{}"
# create an instance of Bite from a JSON string
bite_instance = Bite.from_json(json)
# print the JSON string representation of the object
print(Bite.to_json())

# convert the object into a dict
bite_dict = bite_instance.to_dict()
# create an instance of Bite from a dict
bite_from_dict = Bite.from_dict(bite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


