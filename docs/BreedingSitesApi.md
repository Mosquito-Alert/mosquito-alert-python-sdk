# mosquito_alert.BreedingSitesApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BreedingSitesApi.md#create) | **POST** /breeding-sites/ | 
[**destroy**](BreedingSitesApi.md#destroy) | **DELETE** /breeding-sites/{uuid}/ | 
[**geo_list**](BreedingSitesApi.md#geo_list) | **GET** /breeding-sites/geo/ | 
[**list**](BreedingSitesApi.md#list) | **GET** /breeding-sites/ | 
[**list_mine**](BreedingSitesApi.md#list_mine) | **GET** /me/breeding-sites/ | 
[**retrieve**](BreedingSitesApi.md#retrieve) | **GET** /breeding-sites/{uuid}/ | 


# **create**
> BreedingSite create(created_at, sent_at, location, photos, site_type, note=note, tags=tags, has_water=has_water, in_public_area=in_public_area, has_near_mosquitoes=has_near_mosquitoes, has_larvae=has_larvae)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.breeding_site import BreedingSite
from mosquito_alert.models.location_request import LocationRequest
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
    api_instance = mosquito_alert.BreedingSitesApi(api_client)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | 
    sent_at = '2013-10-20T19:20:30+01:00' # datetime | 
    location = mosquito_alert.LocationRequest() # LocationRequest | 
    photos = None # List[bytearray] | 
    site_type = 'site_type_example' # str | 
    note = 'note_example' # str |  (optional)
    tags = ['tags_example'] # List[str] |  (optional)
    has_water = True # bool | Either if the user perceived water in the breeding site. (optional)
    in_public_area = True # bool | Either if the breeding site is found in a public area. (optional)
    has_near_mosquitoes = True # bool | Either if the user perceived mosquitoes near the breeding site (less than 10 meters). (optional)
    has_larvae = True # bool | Either if the user perceived larvaes the breeding site. (optional)

    try:
        api_response = api_instance.create(created_at, sent_at, location, photos, site_type, note=note, tags=tags, has_water=has_water, in_public_area=in_public_area, has_near_mosquitoes=has_near_mosquitoes, has_larvae=has_larvae)
        print("The response of BreedingSitesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at** | **datetime**|  | 
 **sent_at** | **datetime**|  | 
 **location** | [**LocationRequest**](LocationRequest.md)|  | 
 **photos** | **List[bytearray]**|  | 
 **site_type** | **str**|  | 
 **note** | **str**|  | [optional] 
 **tags** | [**List[str]**](str.md)|  | [optional] 
 **has_water** | **bool**| Either if the user perceived water in the breeding site. | [optional] 
 **in_public_area** | **bool**| Either if the breeding site is found in a public area. | [optional] 
 **has_near_mosquitoes** | **bool**| Either if the user perceived mosquitoes near the breeding site (less than 10 meters). | [optional] 
 **has_larvae** | **bool**| Either if the user perceived larvaes the breeding site. | [optional] 

### Return type

[**BreedingSite**](BreedingSite.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
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
    api_instance = mosquito_alert.BreedingSitesApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_instance.destroy(uuid)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

void (empty response body)

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_list**
> List[BreedingSiteGeoModel] geo_list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, geo_precision=geo_precision, has_larvae=has_larvae, has_near_mosquitoes=has_near_mosquitoes, has_photos=has_photos, has_water=has_water, order_by=order_by, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, site_type=site_type, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.breeding_site_geo_model import BreedingSiteGeoModel
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
    api_instance = mosquito_alert.BreedingSitesApi(api_client)
    boundary_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    country_id = 56 # int |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    dist = 1000 # float | Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. (optional) (default to 1000)
    geo_precision = 3.4 # float | Latitude/Longitude precision (optional)
    has_larvae = True # bool |  (optional)
    has_near_mosquitoes = True # bool |  (optional)
    has_photos = True # bool | Has any photo (optional)
    has_water = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    point = [[0,10]] # List[float] | Point represented in **x,y** format. Represents **point** in **Distance to point filter** (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    search = 'search_example' # str | Un término de búsqueda. (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    site_type = ['site_type_example'] # List[Optional[str]] | Breeding site type.   (optional)
    tags = ['tags_example'] # List[str] | Múltiples valores separados por comas. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.geo_list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, geo_precision=geo_precision, has_larvae=has_larvae, has_near_mosquitoes=has_near_mosquitoes, has_photos=has_photos, has_water=has_water, order_by=order_by, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, site_type=site_type, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of BreedingSitesApi->geo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->geo_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary_uuid** | **UUID**|  | [optional] 
 **country_id** | **int**|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **dist** | **float**| Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. | [optional] [default to 1000]
 **geo_precision** | **float**| Latitude/Longitude precision | [optional] 
 **has_larvae** | **bool**|  | [optional] 
 **has_near_mosquitoes** | **bool**|  | [optional] 
 **has_photos** | **bool**| Has any photo | [optional] 
 **has_water** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **point** | [**List[float]**](float.md)| Point represented in **x,y** format. Represents **point** in **Distance to point filter** | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **search** | **str**| Un término de búsqueda. | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **site_type** | [**List[Optional[str]]**](str.md)| Breeding site type.   | [optional] 
 **tags** | [**List[str]**](str.md)| Múltiples valores separados por comas. | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **UUID**|  | [optional] 

### Return type

[**List[BreedingSiteGeoModel]**](BreedingSiteGeoModel.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/geo+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedBreedingSiteList list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_larvae=has_larvae, has_near_mosquitoes=has_near_mosquitoes, has_photos=has_photos, has_water=has_water, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, site_type=site_type, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_breeding_site_list import PaginatedBreedingSiteList
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
    api_instance = mosquito_alert.BreedingSitesApi(api_client)
    boundary_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    country_id = 56 # int |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    dist = 1000 # float | Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. (optional) (default to 1000)
    format = 'format_example' # str |  (optional)
    geo_precision = 3.4 # float | Latitude/Longitude precision (optional)
    has_larvae = True # bool |  (optional)
    has_near_mosquitoes = True # bool |  (optional)
    has_photos = True # bool | Has any photo (optional)
    has_water = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    page = 56 # int | Un número de página dentro del conjunto de resultados paginado. (optional)
    page_size = 56 # int | Número de resultados a devolver por página. (optional)
    point = [[0,10]] # List[float] | Point represented in **x,y** format. Represents **point** in **Distance to point filter** (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    search = 'search_example' # str | Un término de búsqueda. (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    site_type = ['site_type_example'] # List[Optional[str]] | Breeding site type.   (optional)
    tags = ['tags_example'] # List[str] | Múltiples valores separados por comas. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_larvae=has_larvae, has_near_mosquitoes=has_near_mosquitoes, has_photos=has_photos, has_water=has_water, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, site_type=site_type, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of BreedingSitesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary_uuid** | **UUID**|  | [optional] 
 **country_id** | **int**|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **dist** | **float**| Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. | [optional] [default to 1000]
 **format** | **str**|  | [optional] 
 **geo_precision** | **float**| Latitude/Longitude precision | [optional] 
 **has_larvae** | **bool**|  | [optional] 
 **has_near_mosquitoes** | **bool**|  | [optional] 
 **has_photos** | **bool**| Has any photo | [optional] 
 **has_water** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **page** | **int**| Un número de página dentro del conjunto de resultados paginado. | [optional] 
 **page_size** | **int**| Número de resultados a devolver por página. | [optional] 
 **point** | [**List[float]**](float.md)| Point represented in **x,y** format. Represents **point** in **Distance to point filter** | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **search** | **str**| Un término de búsqueda. | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **site_type** | [**List[Optional[str]]**](str.md)| Breeding site type.   | [optional] 
 **tags** | [**List[str]**](str.md)| Múltiples valores separados por comas. | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **UUID**|  | [optional] 

### Return type

[**PaginatedBreedingSiteList**](PaginatedBreedingSiteList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mine**
> PaginatedBreedingSiteList list_mine(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_larvae=has_larvae, has_near_mosquitoes=has_near_mosquitoes, has_photos=has_photos, has_water=has_water, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, site_type=site_type, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

Get Current User's Breeding Sites

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_breeding_site_list import PaginatedBreedingSiteList
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
    api_instance = mosquito_alert.BreedingSitesApi(api_client)
    boundary_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    country_id = 56 # int |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    dist = 1000 # float | Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. (optional) (default to 1000)
    format = 'format_example' # str |  (optional)
    geo_precision = 3.4 # float | Latitude/Longitude precision (optional)
    has_larvae = True # bool |  (optional)
    has_near_mosquitoes = True # bool |  (optional)
    has_photos = True # bool | Has any photo (optional)
    has_water = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    page = 56 # int | Un número de página dentro del conjunto de resultados paginado. (optional)
    page_size = 56 # int | Número de resultados a devolver por página. (optional)
    point = [[0,10]] # List[float] | Point represented in **x,y** format. Represents **point** in **Distance to point filter** (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    search = 'search_example' # str | Un término de búsqueda. (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    site_type = ['site_type_example'] # List[Optional[str]] | Breeding site type.   (optional)
    tags = ['tags_example'] # List[str] | Múltiples valores separados por comas. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.list_mine(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_larvae=has_larvae, has_near_mosquitoes=has_near_mosquitoes, has_photos=has_photos, has_water=has_water, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, site_type=site_type, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of BreedingSitesApi->list_mine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->list_mine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary_uuid** | **UUID**|  | [optional] 
 **country_id** | **int**|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **dist** | **float**| Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. | [optional] [default to 1000]
 **format** | **str**|  | [optional] 
 **geo_precision** | **float**| Latitude/Longitude precision | [optional] 
 **has_larvae** | **bool**|  | [optional] 
 **has_near_mosquitoes** | **bool**|  | [optional] 
 **has_photos** | **bool**| Has any photo | [optional] 
 **has_water** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **page** | **int**| Un número de página dentro del conjunto de resultados paginado. | [optional] 
 **page_size** | **int**| Número de resultados a devolver por página. | [optional] 
 **point** | [**List[float]**](float.md)| Point represented in **x,y** format. Represents **point** in **Distance to point filter** | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **search** | **str**| Un término de búsqueda. | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **site_type** | [**List[Optional[str]]**](str.md)| Breeding site type.   | [optional] 
 **tags** | [**List[str]**](str.md)| Múltiples valores separados por comas. | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **UUID**|  | [optional] 

### Return type

[**PaginatedBreedingSiteList**](PaginatedBreedingSiteList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

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
> BreedingSite retrieve(uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.breeding_site import BreedingSite
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
    api_instance = mosquito_alert.BreedingSitesApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_response = api_instance.retrieve(uuid)
        print("The response of BreedingSitesApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreedingSitesApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**BreedingSite**](BreedingSite.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth), [jwtAuth](../README.md#jwtAuth)

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

