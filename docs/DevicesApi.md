# mosquito_alert.DevicesApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](DevicesApi.md#create) | **POST** /devices/ | 
[**partial_update**](DevicesApi.md#partial_update) | **PATCH** /devices/{device_id}/ | 
[**retrieve**](DevicesApi.md#retrieve) | **GET** /devices/{device_id}/ | 
[**update**](DevicesApi.md#update) | **PUT** /devices/{device_id}/ | 


# **create**
> Device create(device_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

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
        api_response = api_instance.create(device_request)
        print("The response of DevicesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_request** | [**DeviceRequest**](DeviceRequest.md)|  | 

### Return type

[**Device**](Device.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update**
> DeviceUpdate partial_update(device_id, patched_device_update_request=patched_device_update_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

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
        api_response = api_instance.partial_update(device_id, patched_device_update_request=patched_device_update_request)
        print("The response of DevicesApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **patched_device_update_request** | [**PatchedDeviceUpdateRequest**](PatchedDeviceUpdateRequest.md)|  | [optional] 

### Return type

[**DeviceUpdate**](DeviceUpdate.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> Device retrieve(device_id)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

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
        api_response = api_instance.retrieve(device_id)
        print("The response of DevicesApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**Device**](Device.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> DeviceUpdate update(device_id, device_update_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

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
        api_response = api_instance.update(device_id, device_update_request)
        print("The response of DevicesApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **device_update_request** | [**DeviceUpdateRequest**](DeviceUpdateRequest.md)|  | 

### Return type

[**DeviceUpdate**](DeviceUpdate.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

