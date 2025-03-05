# mosquito_alert.AuthApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](AuthApi.md#change_password) | **POST** /auth/password/change/ | 
[**obtain_token**](AuthApi.md#obtain_token) | **POST** /auth/token/ | 
[**refresh_token**](AuthApi.md#refresh_token) | **POST** /auth/token/refresh/ | 
[**signup_guest**](AuthApi.md#signup_guest) | **POST** /auth/signup/guest/ | 
[**verify_token**](AuthApi.md#verify_token) | **POST** /auth/token/verify/ | 


# **change_password**
> change_password(password_change_request)

### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.password_change_request import PasswordChangeRequest
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
    api_instance = mosquito_alert.AuthApi(api_client)
    password_change_request = mosquito_alert.PasswordChangeRequest() # PasswordChangeRequest | 

    try:
        api_instance.change_password(password_change_request)
    except Exception as e:
        print("Exception when calling AuthApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_change_request** | [**PasswordChangeRequest**](PasswordChangeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obtain_token**
> AppUserTokenObtainPair obtain_token(app_user_token_obtain_pair_request)

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

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
    api_instance = mosquito_alert.AuthApi(api_client)
    app_user_token_obtain_pair_request = mosquito_alert.AppUserTokenObtainPairRequest() # AppUserTokenObtainPairRequest | 

    try:
        api_response = api_instance.obtain_token(app_user_token_obtain_pair_request)
        print("The response of AuthApi->obtain_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->obtain_token: %s\n" % e)
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
**400** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> TokenRefresh refresh_token(token_refresh_request)

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

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
    api_instance = mosquito_alert.AuthApi(api_client)
    token_refresh_request = mosquito_alert.TokenRefreshRequest() # TokenRefreshRequest | 

    try:
        api_response = api_instance.refresh_token(token_refresh_request)
        print("The response of AuthApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_token: %s\n" % e)
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
**400** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_guest**
> GuestRegistration signup_guest(guest_registration_request)

### Example


```python
import mosquito_alert
from mosquito_alert.models.guest_registration import GuestRegistration
from mosquito_alert.models.guest_registration_request import GuestRegistrationRequest
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
    api_instance = mosquito_alert.AuthApi(api_client)
    guest_registration_request = mosquito_alert.GuestRegistrationRequest() # GuestRegistrationRequest | 

    try:
        api_response = api_instance.signup_guest(guest_registration_request)
        print("The response of AuthApi->signup_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->signup_guest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_registration_request** | [**GuestRegistrationRequest**](GuestRegistrationRequest.md)|  | 

### Return type

[**GuestRegistration**](GuestRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**404** |  |  -  |
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_token**
> verify_token(token_verify_request)

Takes a token and indicates if it is valid.  This view provides no
information about a token's fitness for a particular use.

### Example


```python
import mosquito_alert
from mosquito_alert.models.token_verify_request import TokenVerifyRequest
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
    api_instance = mosquito_alert.AuthApi(api_client)
    token_verify_request = mosquito_alert.TokenVerifyRequest() # TokenVerifyRequest | 

    try:
        api_instance.verify_token(token_verify_request)
    except Exception as e:
        print("Exception when calling AuthApi->verify_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_verify_request** | [**TokenVerifyRequest**](TokenVerifyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**404** |  |  -  |
**200** | No response body |  -  |
**401** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

