# BiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**sent_at** | **datetime** |  | 
**location** | [**LocationRequest**](LocationRequest.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**event_environment** | **str** | The environment where the event took place. | [optional] 
**event_moment** | **str** | The moment of the day when the event took place. | [optional] 
**counts** | [**BiteCountsRequest**](BiteCountsRequest.md) |  | 

## Example

```python
from mosquito_alert.models.bite_request import BiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BiteRequest from a JSON string
bite_request_instance = BiteRequest.from_json(json)
# print the JSON string representation of the object
print(BiteRequest.to_json())

# convert the object into a dict
bite_request_dict = bite_request_instance.to_dict()
# create an instance of BiteRequest from a dict
bite_request_from_dict = BiteRequest.from_dict(bite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


