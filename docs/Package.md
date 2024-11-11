# Package


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of tigatrapp package from which this report was submitted. | [optional] 
**version** | **int** | Version number of tigatrapp package from which this report was submitted. | [optional] 
**language** | **str** | Language setting, within tigatrapp, of device from which this report was submitted. 2-digit ISO-639-1 language code. | [optional] 

## Example

```python
from mosquito_alert_api.models.package import Package

# TODO update the JSON string below
json = "{}"
# create an instance of Package from a JSON string
package_instance = Package.from_json(json)
# print the JSON string representation of the object
print(Package.to_json())

# convert the object into a dict
package_dict = package_instance.to_dict()
# create an instance of Package from a dict
package_from_dict = Package.from_dict(package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


