# mosquito_alert.DevicesApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_create**](DevicesApi.md#devices_create) | **POST** /devices/ | 
[**devices_partial_update**](DevicesApi.md#devices_partial_update) | **PATCH** /devices/{device_id}/ | 
[**devices_retrieve**](DevicesApi.md#devices_retrieve) | **GET** /devices/{device_id}/ | 
[**devices_update**](DevicesApi.md#devices_update) | **PUT** /devices/{device_id}/ | 


# **devices_create**
> Device devices_create(device_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.device import Device
from mosquito_alert.models.device_request import DeviceRequest
from mosquito_alert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert.Configuration(
    host = "https://api.mosquitoalert.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.DevicesApi(api_client)
    device_request = mosquito_alert.DeviceRequest() # DeviceRequest | 

    try:
        api_response = api_instance.devices_create(device_request)
        print("The response of DevicesApi->devices_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->devices_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_request** | [**DeviceRequest**](DeviceRequest.md)|  | 

### Return type

[**Device**](Device.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_partial_update**
> DeviceUpdate devices_partial_update(device_id, patched_device_update_request=patched_device_update_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.device_update import DeviceUpdate
from mosquito_alert.models.patched_device_update_request import PatchedDeviceUpdateRequest
from mosquito_alert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert.Configuration(
    host = "https://api.mosquitoalert.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    patched_device_update_request = mosquito_alert.PatchedDeviceUpdateRequest() # PatchedDeviceUpdateRequest |  (optional)

    try:
        api_response = api_instance.devices_partial_update(device_id, patched_device_update_request=patched_device_update_request)
        print("The response of DevicesApi->devices_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->devices_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **patched_device_update_request** | [**PatchedDeviceUpdateRequest**](PatchedDeviceUpdateRequest.md)|  | [optional] 

### Return type

[**DeviceUpdate**](DeviceUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_retrieve**
> Device devices_retrieve(device_id)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.device import Device
from mosquito_alert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert.Configuration(
    host = "https://api.mosquitoalert.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        api_response = api_instance.devices_retrieve(device_id)
        print("The response of DevicesApi->devices_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->devices_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**Device**](Device.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_update**
> DeviceUpdate devices_update(device_id, device_update_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.device_update import DeviceUpdate
from mosquito_alert.models.device_update_request import DeviceUpdateRequest
from mosquito_alert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert.Configuration(
    host = "https://api.mosquitoalert.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    device_update_request = mosquito_alert.DeviceUpdateRequest() # DeviceUpdateRequest | 

    try:
        api_response = api_instance.devices_update(device_id, device_update_request)
        print("The response of DevicesApi->devices_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->devices_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **device_update_request** | [**DeviceUpdateRequest**](DeviceUpdateRequest.md)|  | 

### Return type

[**DeviceUpdate**](DeviceUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
