# BiteCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of bites reported. | [readonly] [default to 0]
**head** | **int** | Number of bites reported in the head. | [optional] [default to 0]
**left_arm** | **int** | Number of bites reported in the left arm. | [optional] [default to 0]
**right_arm** | **int** | Number of bites reported in the right arm. | [optional] [default to 0]
**chest** | **int** | Number of bites reported in the chest. | [optional] [default to 0]
**left_leg** | **int** | Number of bites reported in the left leg. | [optional] [default to 0]
**right_leg** | **int** | Number of bites reported in the right leg. | [optional] [default to 0]

## Example

```python
from mosquito_alert.models.bite_counts import BiteCounts

# TODO update the JSON string below
json = "{}"
# create an instance of BiteCounts from a JSON string
bite_counts_instance = BiteCounts.from_json(json)
# print the JSON string representation of the object
print(BiteCounts.to_json())

# convert the object into a dict
bite_counts_dict = bite_counts_instance.to_dict()
# create an instance of BiteCounts from a dict
bite_counts_from_dict = BiteCounts.from_dict(bite_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


