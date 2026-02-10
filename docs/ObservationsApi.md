# mosquito_alert.ObservationsApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ObservationsApi.md#create) | **POST** /observations/ | 
[**destroy**](ObservationsApi.md#destroy) | **DELETE** /observations/{uuid}/ | 
[**geo_list**](ObservationsApi.md#geo_list) | **GET** /observations/geo/ | 
[**list**](ObservationsApi.md#list) | **GET** /observations/ | 
[**list_mine**](ObservationsApi.md#list_mine) | **GET** /me/observations/ | 
[**retrieve**](ObservationsApi.md#retrieve) | **GET** /observations/{uuid}/ | 


# **create**
> Observation create(created_at, sent_at, location, photos, note=note, tags=tags, event_environment=event_environment, event_moment=event_moment, mosquito_appearance=mosquito_appearance)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.location_request import LocationRequest
from mosquito_alert.models.observation import Observation
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
    api_instance = mosquito_alert.ObservationsApi(api_client)
    created_at = '2013-10-20T19:20:30+01:00' # datetime | 
    sent_at = '2013-10-20T19:20:30+01:00' # datetime | 
    location = mosquito_alert.LocationRequest() # LocationRequest | 
    photos = None # List[bytearray] | 
    note = 'note_example' # str |  (optional)
    tags = ['tags_example'] # List[str] |  (optional)
    event_environment = 'event_environment_example' # str | The environment where the event took place. (optional)
    event_moment = 'event_moment_example' # str | The moment of the day when the event took place. (optional)
    mosquito_appearance = mosquito_alert.MosquitoAppearanceRequest() # MosquitoAppearanceRequest | User-provided description of the mosquito's appearance (optional)

    try:
        api_response = api_instance.create(created_at, sent_at, location, photos, note=note, tags=tags, event_environment=event_environment, event_moment=event_moment, mosquito_appearance=mosquito_appearance)
        print("The response of ObservationsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at** | **datetime**|  | 
 **sent_at** | **datetime**|  | 
 **location** | [**LocationRequest**](LocationRequest.md)|  | 
 **photos** | **List[bytearray]**|  | 
 **note** | **str**|  | [optional] 
 **tags** | [**List[str]**](str.md)|  | [optional] 
 **event_environment** | **str**| The environment where the event took place. | [optional] 
 **event_moment** | **str**| The moment of the day when the event took place. | [optional] 
 **mosquito_appearance** | [**MosquitoAppearanceRequest**](MosquitoAppearanceRequest.md)| User-provided description of the mosquito&#39;s appearance | [optional] 

### Return type

[**Observation**](Observation.md)

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
    api_instance = mosquito_alert.ObservationsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_instance.destroy(uuid)
    except Exception as e:
        print("Exception when calling ObservationsApi->destroy: %s\n" % e)
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
> List[ObservationGeoModel] geo_list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_photos=has_photos, identification_taxon_ids=identification_taxon_ids, identification_taxon_ids_lookup=identification_taxon_ids_lookup, negate_identification_taxon_ids=negate_identification_taxon_ids, order_by=order_by, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.observation_geo_model import ObservationGeoModel
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
    api_instance = mosquito_alert.ObservationsApi(api_client)
    boundary_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    country_id = 56 # int |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    dist = 1000 # float | Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. (optional) (default to 1000)
    format = 'format_example' # str |  (optional)
    geo_precision = 3.4 # float | Latitude/Longitude precision (optional)
    has_photos = True # bool | Has any photo (optional)
    identification_taxon_ids = ['identification_taxon_ids_example'] # List[str] |  (optional)
    identification_taxon_ids_lookup = 'identification_taxon_ids_lookup_example' # str |  (optional)
    negate_identification_taxon_ids = True # bool | Negate identification_taxon_ids filter (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    point = [[0,10]] # List[float] | Point represented in **x,y** format. Represents **point** in **Distance to point filter** (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    search = 'search_example' # str | Un término de búsqueda. (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    tags = ['tags_example'] # List[str] | Múltiples valores separados por comas. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.geo_list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_photos=has_photos, identification_taxon_ids=identification_taxon_ids, identification_taxon_ids_lookup=identification_taxon_ids_lookup, negate_identification_taxon_ids=negate_identification_taxon_ids, order_by=order_by, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of ObservationsApi->geo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->geo_list: %s\n" % e)
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
 **has_photos** | **bool**| Has any photo | [optional] 
 **identification_taxon_ids** | [**List[str]**](str.md)|  | [optional] 
 **identification_taxon_ids_lookup** | **str**|  | [optional] 
 **negate_identification_taxon_ids** | **bool**| Negate identification_taxon_ids filter | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **point** | [**List[float]**](float.md)| Point represented in **x,y** format. Represents **point** in **Distance to point filter** | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **search** | **str**| Un término de búsqueda. | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **tags** | [**List[str]**](str.md)| Múltiples valores separados por comas. | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **UUID**|  | [optional] 

### Return type

[**List[ObservationGeoModel]**](ObservationGeoModel.md)

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
> PaginatedObservationList list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_photos=has_photos, identification_taxon_ids=identification_taxon_ids, identification_taxon_ids_lookup=identification_taxon_ids_lookup, negate_identification_taxon_ids=negate_identification_taxon_ids, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_observation_list import PaginatedObservationList
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
    api_instance = mosquito_alert.ObservationsApi(api_client)
    boundary_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    country_id = 56 # int |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    dist = 1000 # float | Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. (optional) (default to 1000)
    format = 'format_example' # str |  (optional)
    geo_precision = 3.4 # float | Latitude/Longitude precision (optional)
    has_photos = True # bool | Has any photo (optional)
    identification_taxon_ids = ['identification_taxon_ids_example'] # List[str] |  (optional)
    identification_taxon_ids_lookup = 'identification_taxon_ids_lookup_example' # str |  (optional)
    negate_identification_taxon_ids = True # bool | Negate identification_taxon_ids filter (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    page = 56 # int | Un número de página dentro del conjunto de resultados paginado. (optional)
    page_size = 56 # int | Número de resultados a devolver por página. (optional)
    point = [[0,10]] # List[float] | Point represented in **x,y** format. Represents **point** in **Distance to point filter** (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    search = 'search_example' # str | Un término de búsqueda. (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    tags = ['tags_example'] # List[str] | Múltiples valores separados por comas. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.list(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_photos=has_photos, identification_taxon_ids=identification_taxon_ids, identification_taxon_ids_lookup=identification_taxon_ids_lookup, negate_identification_taxon_ids=negate_identification_taxon_ids, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of ObservationsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->list: %s\n" % e)
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
 **has_photos** | **bool**| Has any photo | [optional] 
 **identification_taxon_ids** | [**List[str]**](str.md)|  | [optional] 
 **identification_taxon_ids_lookup** | **str**|  | [optional] 
 **negate_identification_taxon_ids** | **bool**| Negate identification_taxon_ids filter | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **page** | **int**| Un número de página dentro del conjunto de resultados paginado. | [optional] 
 **page_size** | **int**| Número de resultados a devolver por página. | [optional] 
 **point** | [**List[float]**](float.md)| Point represented in **x,y** format. Represents **point** in **Distance to point filter** | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **search** | **str**| Un término de búsqueda. | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **tags** | [**List[str]**](str.md)| Múltiples valores separados por comas. | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **UUID**|  | [optional] 

### Return type

[**PaginatedObservationList**](PaginatedObservationList.md)

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
> PaginatedObservationList list_mine(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_photos=has_photos, identification_taxon_ids=identification_taxon_ids, identification_taxon_ids_lookup=identification_taxon_ids_lookup, negate_identification_taxon_ids=negate_identification_taxon_ids, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)

Get Current User's Observations

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_observation_list import PaginatedObservationList
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
    api_instance = mosquito_alert.ObservationsApi(api_client)
    boundary_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    country_id = 56 # int |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    dist = 1000 # float | Represents **Distance** in **Distance to point** filter. Default value is used only if ***point*** is passed. (optional) (default to 1000)
    format = 'format_example' # str |  (optional)
    geo_precision = 3.4 # float | Latitude/Longitude precision (optional)
    has_photos = True # bool | Has any photo (optional)
    identification_taxon_ids = ['identification_taxon_ids_example'] # List[str] |  (optional)
    identification_taxon_ids_lookup = 'identification_taxon_ids_lookup_example' # str |  (optional)
    negate_identification_taxon_ids = True # bool | Negate identification_taxon_ids filter (optional)
    order_by = ['order_by_example'] # List[str] | Ordenamiento   (optional)
    page = 56 # int | Un número de página dentro del conjunto de resultados paginado. (optional)
    page_size = 56 # int | Número de resultados a devolver por página. (optional)
    point = [[0,10]] # List[float] | Point represented in **x,y** format. Represents **point** in **Distance to point filter** (optional)
    received_at_after = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    received_at_before = '2013-10-20T19:20:30+01:00' # datetime | Received at (optional)
    search = 'search_example' # str | Un término de búsqueda. (optional)
    short_id = 'short_id_example' # str | Short ID (optional)
    tags = ['tags_example'] # List[str] | Múltiples valores separados por comas. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    user_uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        api_response = api_instance.list_mine(boundary_uuid=boundary_uuid, country_id=country_id, created_at_after=created_at_after, created_at_before=created_at_before, dist=dist, format=format, geo_precision=geo_precision, has_photos=has_photos, identification_taxon_ids=identification_taxon_ids, identification_taxon_ids_lookup=identification_taxon_ids_lookup, negate_identification_taxon_ids=negate_identification_taxon_ids, order_by=order_by, page=page, page_size=page_size, point=point, received_at_after=received_at_after, received_at_before=received_at_before, search=search, short_id=short_id, tags=tags, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_uuid=user_uuid)
        print("The response of ObservationsApi->list_mine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->list_mine: %s\n" % e)
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
 **has_photos** | **bool**| Has any photo | [optional] 
 **identification_taxon_ids** | [**List[str]**](str.md)|  | [optional] 
 **identification_taxon_ids_lookup** | **str**|  | [optional] 
 **negate_identification_taxon_ids** | **bool**| Negate identification_taxon_ids filter | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenamiento   | [optional] 
 **page** | **int**| Un número de página dentro del conjunto de resultados paginado. | [optional] 
 **page_size** | **int**| Número de resultados a devolver por página. | [optional] 
 **point** | [**List[float]**](float.md)| Point represented in **x,y** format. Represents **point** in **Distance to point filter** | [optional] 
 **received_at_after** | **datetime**| Received at | [optional] 
 **received_at_before** | **datetime**| Received at | [optional] 
 **search** | **str**| Un término de búsqueda. | [optional] 
 **short_id** | **str**| Short ID | [optional] 
 **tags** | [**List[str]**](str.md)| Múltiples valores separados por comas. | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 
 **user_uuid** | **UUID**|  | [optional] 

### Return type

[**PaginatedObservationList**](PaginatedObservationList.md)

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
> Observation retrieve(uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.observation import Observation
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
    api_instance = mosquito_alert.ObservationsApi(api_client)
    uuid = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_response = api_instance.retrieve(uuid)
        print("The response of ObservationsApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **UUID**|  | 

### Return type

[**Observation**](Observation.md)

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

