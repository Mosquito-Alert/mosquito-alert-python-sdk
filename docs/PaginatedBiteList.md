# PaginatedBiteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Bite]**](Bite.md) |  | [optional] 

## Example

```python
from mosquito_alert_api.models.paginated_bite_list import PaginatedBiteList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBiteList from a JSON string
paginated_bite_list_instance = PaginatedBiteList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBiteList.to_json())

# convert the object into a dict
paginated_bite_list_dict = paginated_bite_list_instance.to_dict()
# create an instance of PaginatedBiteList from a dict
paginated_bite_list_from_dict = PaginatedBiteList.from_dict(paginated_bite_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


