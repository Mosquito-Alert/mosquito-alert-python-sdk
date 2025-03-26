# mosquito_alert.BitesApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BitesApi.md#create) | **POST** /bites/ | 
[**destroy**](BitesApi.md#destroy) | **DELETE** /bites/{uuid}/ | 
[**list**](BitesApi.md#list) | **GET** /bites/ | 
[**list_mine**](BitesApi.md#list_mine) | **GET** /me/bites/ | 
[**retrieve**](BitesApi.md#retrieve) | **GET** /bites/{uuid}/ | 


# **create**
> Bite create(bite_request)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.bite import Bite
from mosquito_alert.models.bite_request import BiteRequest
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.BitesApi(api_client)
    bite_request = mosquito_alert.BiteRequest() # BiteRequest | 

    try:
        api_response = api_instance.create(bite_request)
        print("The response of BitesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bite_request** | [**BiteRequest**](BiteRequest.md)|  | 

### Return type

[**Bite**](Bite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

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

# **destroy**
> destroy(uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.BitesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_instance.destroy(uuid)
    except Exception as e:
        print("Exception when calling BitesApi->destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedBiteList list(created_at_after=created_at_after, created_at_before=created_at_before, location_adm_nuts2=location_adm_nuts2, location_adm_nuts3=location_adm_nuts3, location_country_id=location_country_id, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_bite_list import PaginatedBiteList
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.BitesApi(api_client)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    location_adm_nuts2 = 'location_adm_nuts2_example' # str |  (optional)
    location_adm_nuts3 = 'location_adm_nuts3_example' # str |  (optional)
    location_country_id = 56 # int |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = 'user_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.list(created_at_after=created_at_after, created_at_before=created_at_before, location_adm_nuts2=location_adm_nuts2, location_adm_nuts3=location_adm_nuts3, location_country_id=location_country_id, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of BitesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitesApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **location_adm_nuts2** | **str**|  | [optional] 
 **location_adm_nuts3** | **str**|  | [optional] 
 **location_country_id** | **int**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedBiteList**](PaginatedBiteList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mine**
> PaginatedBiteList list_mine(created_at_after=created_at_after, created_at_before=created_at_before, location_adm_nuts2=location_adm_nuts2, location_adm_nuts3=location_adm_nuts3, location_country_id=location_country_id, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

Get Current User's Bites

### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_bite_list import PaginatedBiteList
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
    api_instance = mosquito_alert.BitesApi(api_client)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    location_adm_nuts2 = 'location_adm_nuts2_example' # str |  (optional)
    location_adm_nuts3 = 'location_adm_nuts3_example' # str |  (optional)
    location_country_id = 56 # int |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = 'user_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.list_mine(created_at_after=created_at_after, created_at_before=created_at_before, location_adm_nuts2=location_adm_nuts2, location_adm_nuts3=location_adm_nuts3, location_country_id=location_country_id, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of BitesApi->list_mine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitesApi->list_mine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **location_adm_nuts2** | **str**|  | [optional] 
 **location_adm_nuts3** | **str**|  | [optional] 
 **location_country_id** | **int**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedBiteList**](PaginatedBiteList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

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

# **retrieve**
> Bite retrieve(uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.bite import Bite
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): jwtAuth
configuration = mosquito_alert.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.BitesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.retrieve(uuid)
        print("The response of BitesApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BitesApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**Bite**](Bite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

