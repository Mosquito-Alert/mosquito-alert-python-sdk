# mosquito_alert_api.BreedingSitesApi

All URIs are relative to *https://api.mosquitoalert.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**breeding_sites_create**](BreedingSitesApi.md#breeding_sites_create) | **POST** /api/v1/breeding-sites/ | 
[**breeding_sites_destroy**](BreedingSitesApi.md#breeding_sites_destroy) | **DELETE** /api/v1/breeding-sites/{uuid}/ | 
[**breeding_sites_list**](BreedingSitesApi.md#breeding_sites_list) | **GET** /api/v1/breeding-sites/ | 
[**breeding_sites_retrieve**](BreedingSitesApi.md#breeding_sites_retrieve) | **GET** /api/v1/breeding-sites/{uuid}/ | 


# **breeding_sites_create**
> BreedingSite breeding_sites_create(breeding_site_request)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.breeding_site import BreedingSite
from mosquito_alert_api.models.breeding_site_request import BreedingSiteRequest
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
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
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.BreedingSitesApi(api_client)
    breeding_site_request = mosquito_alert_api.BreedingSiteRequest() # BreedingSiteRequest | 

    try:
        api_response = api_instance.breeding_sites_create(breeding_site_request)
        print("The response of BreedingSitesApi->breeding_sites_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->breeding_sites_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **breeding_site_request** | [**BreedingSiteRequest**](BreedingSiteRequest.md)|  | 

### Return type

[**BreedingSite**](BreedingSite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **breeding_sites_destroy**
> breeding_sites_destroy(uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
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
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.BreedingSitesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_instance.breeding_sites_destroy(uuid)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->breeding_sites_destroy: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **breeding_sites_list**
> PaginatedBreedingSiteList breeding_sites_list(created_at_after=created_at_after, created_at_before=created_at_before, has_photos=has_photos, location_country_id=location_country_id, location_nuts_2=location_nuts_2, location_nuts_3=location_nuts_3, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.paginated_breeding_site_list import PaginatedBreedingSiteList
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
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
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.BreedingSitesApi(api_client)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    has_photos = True # bool | Has any photo (optional)
    location_country_id = 56 # int |  (optional)
    location_nuts_2 = 'location_nuts_2_example' # str |  (optional)
    location_nuts_3 = 'location_nuts_3_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = 'user_uuid_example' # str |  (optional)

    try:
        api_response = api_instance.breeding_sites_list(created_at_after=created_at_after, created_at_before=created_at_before, has_photos=has_photos, location_country_id=location_country_id, location_nuts_2=location_nuts_2, location_nuts_3=location_nuts_3, order_by=order_by, page=page, page_size=page_size, received_at_after=received_at_after, received_at_before=received_at_before, short_id=short_id, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of BreedingSitesApi->breeding_sites_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->breeding_sites_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **has_photos** | **bool**| Has any photo | [optional] 
 **location_country_id** | **int**|  | [optional] 
 **location_nuts_2** | **str**|  | [optional] 
 **location_nuts_3** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **str**|  | [optional] 

### Return type

[**PaginatedBreedingSiteList**](PaginatedBreedingSiteList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **breeding_sites_retrieve**
> BreedingSite breeding_sites_retrieve(uuid)



### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert_api
from mosquito_alert_api.models.breeding_site import BreedingSite
from mosquito_alert_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mosquitoalert.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mosquito_alert_api.Configuration(
    host = "https://api.mosquitoalert.com"
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
configuration = mosquito_alert_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mosquito_alert_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert_api.BreedingSitesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.breeding_sites_retrieve(uuid)
        print("The response of BreedingSitesApi->breeding_sites_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->breeding_sites_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**BreedingSite**](BreedingSite.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

