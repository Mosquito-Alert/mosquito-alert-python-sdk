# MinimalUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [readonly] 
**locale** | **str** | The locale code representing the language preference selected by the user for displaying the interface text. Enter the locale following the BCP 47 standard in &#39;language&#39; or &#39;language-region&#39; format (e.g., &#39;en&#39; for English, &#39;en-US&#39; for English (United States), &#39;fr&#39; for French). The language is a two-letter ISO 639-1 code, and the region is an optional two-letter ISO 3166-1 alpha-2 code. | [optional] [default to 'en']

## Example

```python
from mosquito_alert.models.minimal_user import MinimalUser

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalUser from a JSON string
minimal_user_instance = MinimalUser.from_json(json)
# print the JSON string representation of the object
print(MinimalUser.to_json())

# convert the object into a dict
minimal_user_dict = minimal_user_instance.to_dict()
# create an instance of MinimalUser from a dict
minimal_user_from_dict = MinimalUser.from_dict(minimal_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


