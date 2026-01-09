# mosquito_alert.PingApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve**](PingApi.md#retrieve) | **GET** /ping/ | 


# **retrieve**
> retrieve()

Simple ping endpoint to check API connectivity

### Example


```python
import mosquito_alert
from mosquito_alert.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert.Configuration(
    host = "https://api.mosquitoalert.com/v1"
)


# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.PingApi(api_client)

    try:
        api_instance.retrieve()
    except Exception as e:
        print("Exception when calling PingApi->retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** |  |  -  |
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

