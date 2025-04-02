# BiteCountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | **int** | Number of bites reported in the head. | [optional] [default to 0]
**left_arm** | **int** | Number of bites reported in the left arm. | [optional] [default to 0]
**right_arm** | **int** | Number of bites reported in the right arm. | [optional] [default to 0]
**chest** | **int** | Number of bites reported in the chest. | [optional] [default to 0]
**left_leg** | **int** | Number of bites reported in the left leg. | [optional] [default to 0]
**right_leg** | **int** | Number of bites reported in the right leg. | [optional] [default to 0]

## Example

```python
from mosquito_alert.models.bite_counts_request import BiteCountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BiteCountsRequest from a JSON string
bite_counts_request_instance = BiteCountsRequest.from_json(json)
# print the JSON string representation of the object
print(BiteCountsRequest.to_json())

# convert the object into a dict
bite_counts_request_dict = bite_counts_request_instance.to_dict()
# create an instance of BiteCountsRequest from a dict
bite_counts_request_from_dict = BiteCountsRequest.from_dict(bite_counts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


