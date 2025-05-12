# mosquito_alert.NotificationsApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](NotificationsApi.md#create) | **POST** /notifications/ | 
[**list**](NotificationsApi.md#list) | **GET** /notifications/ | 
[**list_mine**](NotificationsApi.md#list_mine) | **GET** /me/notifications/ | 
[**partial_update**](NotificationsApi.md#partial_update) | **PATCH** /notifications/{id}/ | 
[**retrieve**](NotificationsApi.md#retrieve) | **GET** /notifications/{id}/ | 
[**update**](NotificationsApi.md#update) | **PUT** /notifications/{id}/ | 


# **create**
> List[CreateNotification] create(meta_notification_request=meta_notification_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.create_notification import CreateNotification
from mosquito_alert.models.meta_notification_request import MetaNotificationRequest
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
    api_instance = mosquito_alert.NotificationsApi(api_client)
    meta_notification_request = mosquito_alert.MetaNotificationRequest() # MetaNotificationRequest |  (optional)

    try:
        api_response = api_instance.create(meta_notification_request=meta_notification_request)
        print("The response of NotificationsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_notification_request** | [**MetaNotificationRequest**](MetaNotificationRequest.md)|  | [optional] 

### Return type

[**List[CreateNotification]**](CreateNotification.md)

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

# **list**
> PaginatedNotificationList list(is_read=is_read, order_by=order_by, page=page, page_size=page_size)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_notification_list import PaginatedNotificationList
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
    api_instance = mosquito_alert.NotificationsApi(api_client)
    is_read = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list(is_read=is_read, order_by=order_by, page=page, page_size=page_size)
        print("The response of NotificationsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_read** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedNotificationList**](PaginatedNotificationList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **list_mine**
> PaginatedNotificationList list_mine(is_read=is_read, order_by=order_by, page=page, page_size=page_size)

Get Current User's Notifications

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_notification_list import PaginatedNotificationList
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
    api_instance = mosquito_alert.NotificationsApi(api_client)
    is_read = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.list_mine(is_read=is_read, order_by=order_by, page=page, page_size=page_size)
        print("The response of NotificationsApi->list_mine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_mine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_read** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedNotificationList**](PaginatedNotificationList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **partial_update**
> Notification partial_update(id, patched_notification_request=patched_notification_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.notification import Notification
from mosquito_alert.models.patched_notification_request import PatchedNotificationRequest
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
    api_instance = mosquito_alert.NotificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this notification.
    patched_notification_request = mosquito_alert.PatchedNotificationRequest() # PatchedNotificationRequest |  (optional)

    try:
        api_response = api_instance.partial_update(id, patched_notification_request=patched_notification_request)
        print("The response of NotificationsApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification. | 
 **patched_notification_request** | [**PatchedNotificationRequest**](PatchedNotificationRequest.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

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
> Notification retrieve(id)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.notification import Notification
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
    api_instance = mosquito_alert.NotificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this notification.

    try:
        api_response = api_instance.retrieve(id)
        print("The response of NotificationsApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification. | 

### Return type

[**Notification**](Notification.md)

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
> Notification update(id, notification_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.notification import Notification
from mosquito_alert.models.notification_request import NotificationRequest
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
    api_instance = mosquito_alert.NotificationsApi(api_client)
    id = 56 # int | A unique integer value identifying this notification.
    notification_request = mosquito_alert.NotificationRequest() # NotificationRequest | 

    try:
        api_response = api_instance.update(id, notification_request)
        print("The response of NotificationsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notification. | 
 **notification_request** | [**NotificationRequest**](NotificationRequest.md)|  | 

### Return type

[**Notification**](Notification.md)

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

