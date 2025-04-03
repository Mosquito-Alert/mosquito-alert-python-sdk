# mosquito_alert.IdentificationTasksApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](IdentificationTasksApi.md#list) | **GET** /identification-tasks/ | 
[**photos_list**](IdentificationTasksApi.md#photos_list) | **GET** /identification-tasks/{observation_uuid}/photos/ | 
[**photos_retrieve**](IdentificationTasksApi.md#photos_retrieve) | **GET** /identification-tasks/{observation_uuid}/photos/{uuid}/ | 
[**predictions_create**](IdentificationTasksApi.md#predictions_create) | **POST** /identification-tasks/{observation_uuid}/predictions/ | 
[**predictions_destroy**](IdentificationTasksApi.md#predictions_destroy) | **DELETE** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**predictions_list**](IdentificationTasksApi.md#predictions_list) | **GET** /identification-tasks/{observation_uuid}/predictions/ | 
[**predictions_partial_update**](IdentificationTasksApi.md#predictions_partial_update) | **PATCH** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**predictions_retrieve**](IdentificationTasksApi.md#predictions_retrieve) | **GET** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**predictions_update**](IdentificationTasksApi.md#predictions_update) | **PUT** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**retrieve**](IdentificationTasksApi.md#retrieve) | **GET** /identification-tasks/{observation_uuid}/ | 


# **list**
> PaginatedIdentificationTaskList list(assignees=assignees, created_at_after=created_at_after, created_at_before=created_at_before, fully_predicted=fully_predicted, is_flagged=is_flagged, is_safe=is_safe, num_annotations_max=num_annotations_max, num_annotations_min=num_annotations_min, num_assignations_max=num_assignations_max, num_assignations_min=num_assignations_min, order_by=order_by, page=page, page_size=page_size, revision_type=revision_type, status=status, updated_at_after=updated_at_after, updated_at_before=updated_at_before)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_identification_task_list import PaginatedIdentificationTaskList
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    assignees = [56] # List[int] |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    fully_predicted = True # bool | Filters identification task based on whether all associated photos have predictions. Set to True to include identification tasks where every photo has a prediction; set to False to include identification tasks where at least one photo is missing a prediction. (optional)
    is_flagged = True # bool |  (optional)
    is_safe = True # bool |  (optional)
    num_annotations_max = 56 # int |  (optional)
    num_annotations_min = 56 # int |  (optional)
    num_assignations_max = 56 # int |  (optional)
    num_assignations_min = 56 # int |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    revision_type = 'revision_type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)

    try:
        api_response = api_instance.list(assignees=assignees, created_at_after=created_at_after, created_at_before=created_at_before, fully_predicted=fully_predicted, is_flagged=is_flagged, is_safe=is_safe, num_annotations_max=num_annotations_max, num_annotations_min=num_annotations_min, num_assignations_max=num_assignations_max, num_assignations_min=num_assignations_min, order_by=order_by, page=page, page_size=page_size, revision_type=revision_type, status=status, updated_at_after=updated_at_after, updated_at_before=updated_at_before)
        print("The response of IdentificationTasksApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignees** | [**List[int]**](int.md)|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **fully_predicted** | **bool**| Filters identification task based on whether all associated photos have predictions. Set to True to include identification tasks where every photo has a prediction; set to False to include identification tasks where at least one photo is missing a prediction. | [optional] 
 **is_flagged** | **bool**|  | [optional] 
 **is_safe** | **bool**|  | [optional] 
 **num_annotations_max** | **int**|  | [optional] 
 **num_annotations_min** | **int**|  | [optional] 
 **num_assignations_max** | **int**|  | [optional] 
 **num_assignations_min** | **int**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **revision_type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 

### Return type

[**PaginatedIdentificationTaskList**](PaginatedIdentificationTaskList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **photos_list**
> PaginatedSimplePhotoList photos_list(observation_uuid, page=page, page_size=page_size)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_simple_photo_list import PaginatedSimplePhotoList
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.photos_list(observation_uuid, page=page, page_size=page_size)
        print("The response of IdentificationTasksApi->photos_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->photos_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedSimplePhotoList**](PaginatedSimplePhotoList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **photos_retrieve**
> SimplePhoto photos_retrieve(observation_uuid, uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.simple_photo import SimplePhoto
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    uuid = 'uuid_example' # str | 

    try:
        api_response = api_instance.photos_retrieve(observation_uuid, uuid)
        print("The response of IdentificationTasksApi->photos_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->photos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **uuid** | **str**|  | 

### Return type

[**SimplePhoto**](SimplePhoto.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **predictions_create**
> CreatePhotoPrediction predictions_create(observation_uuid, create_photo_prediction_request)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.create_photo_prediction import CreatePhotoPrediction
from mosquito_alert.models.create_photo_prediction_request import CreatePhotoPredictionRequest
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    create_photo_prediction_request = mosquito_alert.CreatePhotoPredictionRequest() # CreatePhotoPredictionRequest | 

    try:
        api_response = api_instance.predictions_create(observation_uuid, create_photo_prediction_request)
        print("The response of IdentificationTasksApi->predictions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->predictions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **create_photo_prediction_request** | [**CreatePhotoPredictionRequest**](CreatePhotoPredictionRequest.md)|  | 

### Return type

[**CreatePhotoPrediction**](CreatePhotoPrediction.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **predictions_destroy**
> predictions_destroy(observation_uuid, photo_uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    photo_uuid = 'photo_uuid_example' # str | 

    try:
        api_instance.predictions_destroy(observation_uuid, photo_uuid)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->predictions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **photo_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **predictions_list**
> PaginatedPhotoPredictionList predictions_list(observation_uuid, page=page, page_size=page_size)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_photo_prediction_list import PaginatedPhotoPredictionList
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.predictions_list(observation_uuid, page=page, page_size=page_size)
        print("The response of IdentificationTasksApi->predictions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->predictions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPhotoPredictionList**](PaginatedPhotoPredictionList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **predictions_partial_update**
> PhotoPrediction predictions_partial_update(observation_uuid, photo_uuid, patched_photo_prediction_request=patched_photo_prediction_request)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.patched_photo_prediction_request import PatchedPhotoPredictionRequest
from mosquito_alert.models.photo_prediction import PhotoPrediction
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    photo_uuid = 'photo_uuid_example' # str | 
    patched_photo_prediction_request = mosquito_alert.PatchedPhotoPredictionRequest() # PatchedPhotoPredictionRequest |  (optional)

    try:
        api_response = api_instance.predictions_partial_update(observation_uuid, photo_uuid, patched_photo_prediction_request=patched_photo_prediction_request)
        print("The response of IdentificationTasksApi->predictions_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->predictions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **photo_uuid** | **str**|  | 
 **patched_photo_prediction_request** | [**PatchedPhotoPredictionRequest**](PatchedPhotoPredictionRequest.md)|  | [optional] 

### Return type

[**PhotoPrediction**](PhotoPrediction.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **predictions_retrieve**
> PhotoPrediction predictions_retrieve(observation_uuid, photo_uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.photo_prediction import PhotoPrediction
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    photo_uuid = 'photo_uuid_example' # str | 

    try:
        api_response = api_instance.predictions_retrieve(observation_uuid, photo_uuid)
        print("The response of IdentificationTasksApi->predictions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->predictions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **photo_uuid** | **str**|  | 

### Return type

[**PhotoPrediction**](PhotoPrediction.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

# **predictions_update**
> PhotoPrediction predictions_update(observation_uuid, photo_uuid, photo_prediction_request)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.photo_prediction import PhotoPrediction
from mosquito_alert.models.photo_prediction_request import PhotoPredictionRequest
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    photo_uuid = 'photo_uuid_example' # str | 
    photo_prediction_request = mosquito_alert.PhotoPredictionRequest() # PhotoPredictionRequest | 

    try:
        api_response = api_instance.predictions_update(observation_uuid, photo_uuid, photo_prediction_request)
        print("The response of IdentificationTasksApi->predictions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->predictions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **photo_uuid** | **str**|  | 
 **photo_prediction_request** | [**PhotoPredictionRequest**](PhotoPredictionRequest.md)|  | 

### Return type

[**PhotoPrediction**](PhotoPrediction.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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
> IdentificationTask retrieve(observation_uuid)

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import mosquito_alert
from mosquito_alert.models.identification_task import IdentificationTask
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

# Enter a context with an instance of the API client
with mosquito_alert.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | 

    try:
        api_response = api_instance.retrieve(observation_uuid)
        print("The response of IdentificationTasksApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**|  | 

### Return type

[**IdentificationTask**](IdentificationTask.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

