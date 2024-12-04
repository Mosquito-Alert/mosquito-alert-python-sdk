# LocalizedField

A custom serializer field that supports localization for a dynamic field name. Allows calling with arguments such as 'title', 'message', max_length, help_text, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bg** | **str** | Български | [optional] 
**bn** | **str** | বাংলা | [optional] 
**ca** | **str** | Català | [optional] 
**de** | **str** | Deutsch | [optional] 
**el** | **str** | Ελληνικά | [optional] 
**en** | **str** | English | 
**es** | **str** | Español | [optional] 
**eu** | **str** | Euskara | [optional] 
**fr** | **str** | Français | [optional] 
**gl** | **str** | Galego | [optional] 
**hr** | **str** | Hrvatski | [optional] 
**hu** | **str** | Magyar | [optional] 
**it** | **str** | Italiano | [optional] 
**lb** | **str** | Lëtzebuergesch | [optional] 
**mk** | **str** | Македонски | [optional] 
**nl** | **str** | Nederlands | [optional] 
**pt** | **str** | Português | [optional] 
**ro** | **str** | Română | [optional] 
**sl** | **str** | Slovenščina | [optional] 
**sq** | **str** | Shqip | [optional] 
**sr** | **str** | Српски | [optional] 
**sv** | **str** | Svenska | [optional] 
**tr** | **str** | Türkçe | [optional] 
**zh_cn** | **str** | 中文（中国） | [optional] 

## Example

```python
from mosquito_alert.models.localized_field import LocalizedField

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedField from a JSON string
localized_field_instance = LocalizedField.from_json(json)
# print the JSON string representation of the object
print(LocalizedField.to_json())

# convert the object into a dict
localized_field_dict = localized_field_instance.to_dict()
# create an instance of LocalizedField from a dict
localized_field_from_dict = LocalizedField.from_dict(localized_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

