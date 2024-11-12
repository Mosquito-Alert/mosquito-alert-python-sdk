# BiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**sent_at** | **datetime** |  | 
**location** | [**ReportLocationRequest**](ReportLocationRequest.md) |  | 
**note** | **str** | Note user attached to report. | [optional] 
**tags** | **List[str]** |  | [optional] 
**package** | [**PackageRequest**](PackageRequest.md) |  | [optional] 
**device** | [**DeviceRequest**](DeviceRequest.md) |  | [optional] 
**event_environment** | **str** | The environment where the event took place. | [optional] 
**event_moment** | **str** | The moment of the day when the event took place. | [optional] 
**head_bite_count** | **int** | Number of bites reported in the head. | [optional] [default to 0]
**left_arm_bite_count** | **int** | Number of bites reported in the left arm. | [optional] [default to 0]
**right_arm_bite_count** | **int** | Number of bites reported in the right arm. | [optional] [default to 0]
**chest_bite_count** | **int** | Number of bites reported in the chest. | [optional] [default to 0]
**left_leg_bite_count** | **int** | Number of bites reported in the left leg. | [optional] [default to 0]
**right_leg_bite_count** | **int** | Number of bites reported in the right leg. | [optional] [default to 0]

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


