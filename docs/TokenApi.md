# mosquito_alert.TokenApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_create**](TokenApi.md#token_create) | **POST** /token/ | 
[**token_refresh_create**](TokenApi.md#token_refresh_create) | **POST** /token/refresh/ | 


# **token_create**
> AppUserTokenObtainPair token_create(app_user_token_obtain_pair_request)



Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Example


```python
import mosquito_alert
from mosquito_alert.models.app_user_token_obtain_pair import AppUserTokenObtainPair
from mosquito_alert.models.app_user_token_obtain_pair_request import AppUserTokenObtainPairRequest
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
    api_instance = mosquito_alert.TokenApi(api_client)
    app_user_token_obtain_pair_request = mosquito_alert.AppUserTokenObtainPairRequest() # AppUserTokenObtainPairRequest | 

    try:
        api_response = api_instance.token_create(app_user_token_obtain_pair_request)
        print("The response of TokenApi->token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_user_token_obtain_pair_request** | [**AppUserTokenObtainPairRequest**](AppUserTokenObtainPairRequest.md)|  | 

### Return type

[**AppUserTokenObtainPair**](AppUserTokenObtainPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_refresh_create**
> TokenRefresh token_refresh_create(token_refresh_request)



Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Example


```python
import mosquito_alert
from mosquito_alert.models.token_refresh import TokenRefresh
from mosquito_alert.models.token_refresh_request import TokenRefreshRequest
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
    api_instance = mosquito_alert.TokenApi(api_client)
    token_refresh_request = mosquito_alert.TokenRefreshRequest() # TokenRefreshRequest | 

    try:
        api_response = api_instance.token_refresh_create(token_refresh_request)
        print("The response of TokenApi->token_refresh_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->token_refresh_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_refresh_request** | [**TokenRefreshRequest**](TokenRefreshRequest.md)|  | 

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

