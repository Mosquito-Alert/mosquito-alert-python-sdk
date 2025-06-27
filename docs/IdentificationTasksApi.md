# mosquito_alert.IdentificationTasksApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_create**](IdentificationTasksApi.md#annotations_create) | **POST** /identification-tasks/{observation_uuid}/annotations/ | 
[**annotations_list**](IdentificationTasksApi.md#annotations_list) | **GET** /identification-tasks/{observation_uuid}/annotations/ | 
[**annotations_list_mine**](IdentificationTasksApi.md#annotations_list_mine) | **GET** /me/identification-tasks/annotations/ | 
[**annotations_retrieve**](IdentificationTasksApi.md#annotations_retrieve) | **GET** /identification-tasks/{observation_uuid}/annotations/{id}/ | 
[**assign_next**](IdentificationTasksApi.md#assign_next) | **POST** /identification-tasks/assignments/next/ | 
[**list**](IdentificationTasksApi.md#list) | **GET** /identification-tasks/ | 
[**list_mine**](IdentificationTasksApi.md#list_mine) | **GET** /me/identification-tasks/ | 
[**predictions_create**](IdentificationTasksApi.md#predictions_create) | **POST** /identification-tasks/{observation_uuid}/predictions/ | 
[**predictions_destroy**](IdentificationTasksApi.md#predictions_destroy) | **DELETE** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**predictions_list**](IdentificationTasksApi.md#predictions_list) | **GET** /identification-tasks/{observation_uuid}/predictions/ | 
[**predictions_partial_update**](IdentificationTasksApi.md#predictions_partial_update) | **PATCH** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**predictions_retrieve**](IdentificationTasksApi.md#predictions_retrieve) | **GET** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**predictions_update**](IdentificationTasksApi.md#predictions_update) | **PUT** /identification-tasks/{observation_uuid}/predictions/{photo_uuid}/ | 
[**retrieve**](IdentificationTasksApi.md#retrieve) | **GET** /identification-tasks/{observation_uuid}/ | 


# **annotations_create**
> Annotation annotations_create(observation_uuid, annotation_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.annotation import Annotation
from mosquito_alert.models.annotation_request import AnnotationRequest
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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    annotation_request = mosquito_alert.AnnotationRequest() # AnnotationRequest | 

    try:
        api_response = api_instance.annotations_create(observation_uuid, annotation_request)
        print("The response of IdentificationTasksApi->annotations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->annotations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **annotation_request** | [**AnnotationRequest**](AnnotationRequest.md)|  | 

### Return type

[**Annotation**](Annotation.md)

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

# **annotations_list**
> PaginatedAnnotationList annotations_list(observation_uuid, classification_confidence_label=classification_confidence_label, classification_confidence_max=classification_confidence_max, classification_confidence_min=classification_confidence_min, classification_taxon_ids=classification_taxon_ids, created_at_after=created_at_after, created_at_before=created_at_before, is_decisive=is_decisive, is_favourite=is_favourite, is_flagged=is_flagged, order_by=order_by, page=page, page_size=page_size, type=type, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_ids=user_ids)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_annotation_list import PaginatedAnnotationList
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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation
    classification_confidence_label = 'classification_confidence_label_example' # str |  (optional)
    classification_confidence_max = 3.4 # float |  (optional)
    classification_confidence_min = 3.4 # float |  (optional)
    classification_taxon_ids = [56] # List[int] |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    is_decisive = True # bool |  (optional)
    is_favourite = True # bool |  (optional)
    is_flagged = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type = 'type_example' # str |  (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Updated at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Updated at (optional)
    user_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.annotations_list(observation_uuid, classification_confidence_label=classification_confidence_label, classification_confidence_max=classification_confidence_max, classification_confidence_min=classification_confidence_min, classification_taxon_ids=classification_taxon_ids, created_at_after=created_at_after, created_at_before=created_at_before, is_decisive=is_decisive, is_favourite=is_favourite, is_flagged=is_flagged, order_by=order_by, page=page, page_size=page_size, type=type, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_ids=user_ids)
        print("The response of IdentificationTasksApi->annotations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->annotations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_uuid** | **str**| UUID of the Observation | 
 **classification_confidence_label** | **str**|  | [optional] 
 **classification_confidence_max** | **float**|  | [optional] 
 **classification_confidence_min** | **float**|  | [optional] 
 **classification_taxon_ids** | [**List[int]**](int.md)|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **is_decisive** | **bool**|  | [optional] 
 **is_favourite** | **bool**|  | [optional] 
 **is_flagged** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at_after** | **datetime**| Updated at | [optional] 
 **updated_at_before** | **datetime**| Updated at | [optional] 
 **user_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**PaginatedAnnotationList**](PaginatedAnnotationList.md)

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

# **annotations_list_mine**
> PaginatedAnnotationList annotations_list_mine(classification_confidence_label=classification_confidence_label, classification_confidence_max=classification_confidence_max, classification_confidence_min=classification_confidence_min, classification_taxon_ids=classification_taxon_ids, created_at_after=created_at_after, created_at_before=created_at_before, is_decisive=is_decisive, is_favourite=is_favourite, is_flagged=is_flagged, order_by=order_by, page=page, page_size=page_size, type=type, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_ids=user_ids)

Get my annotations

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.paginated_annotation_list import PaginatedAnnotationList
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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    classification_confidence_label = 'classification_confidence_label_example' # str |  (optional)
    classification_confidence_max = 3.4 # float |  (optional)
    classification_confidence_min = 3.4 # float |  (optional)
    classification_taxon_ids = [56] # List[int] |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    is_decisive = True # bool |  (optional)
    is_favourite = True # bool |  (optional)
    is_flagged = True # bool |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type = 'type_example' # str |  (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Updated at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Updated at (optional)
    user_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.annotations_list_mine(classification_confidence_label=classification_confidence_label, classification_confidence_max=classification_confidence_max, classification_confidence_min=classification_confidence_min, classification_taxon_ids=classification_taxon_ids, created_at_after=created_at_after, created_at_before=created_at_before, is_decisive=is_decisive, is_favourite=is_favourite, is_flagged=is_flagged, order_by=order_by, page=page, page_size=page_size, type=type, updated_at_after=updated_at_after, updated_at_before=updated_at_before, user_ids=user_ids)
        print("The response of IdentificationTasksApi->annotations_list_mine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->annotations_list_mine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_confidence_label** | **str**|  | [optional] 
 **classification_confidence_max** | **float**|  | [optional] 
 **classification_confidence_min** | **float**|  | [optional] 
 **classification_taxon_ids** | [**List[int]**](int.md)|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **is_decisive** | **bool**|  | [optional] 
 **is_favourite** | **bool**|  | [optional] 
 **is_flagged** | **bool**|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | **str**|  | [optional] 
 **updated_at_after** | **datetime**| Updated at | [optional] 
 **updated_at_before** | **datetime**| Updated at | [optional] 
 **user_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**PaginatedAnnotationList**](PaginatedAnnotationList.md)

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

# **annotations_retrieve**
> Annotation annotations_retrieve(id, observation_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.annotation import Annotation
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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    id = 56 # int | A unique integer value identifying this expert report annotation.
    observation_uuid = 'observation_uuid_example' # str | UUID of the Observation

    try:
        api_response = api_instance.annotations_retrieve(id, observation_uuid)
        print("The response of IdentificationTasksApi->annotations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->annotations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this expert report annotation. | 
 **observation_uuid** | **str**| UUID of the Observation | 

### Return type

[**Annotation**](Annotation.md)

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

# **assign_next**
> Assignment assign_next()

Assign the next available identification task.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.assignment import Assignment
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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)

    try:
        api_response = api_instance.assign_next()
        print("The response of IdentificationTasksApi->assign_next:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->assign_next: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Assignment**](Assignment.md)

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
**201** |  |  -  |
**204** | No available tasks pending to assign |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedIdentificationTaskList list(annotator_ids=annotator_ids, assignee_ids=assignee_ids, created_at_after=created_at_after, created_at_before=created_at_before, fully_predicted=fully_predicted, is_flagged=is_flagged, is_safe=is_safe, num_annotations_max=num_annotations_max, num_annotations_min=num_annotations_min, observation_country_ids=observation_country_ids, order_by=order_by, page=page, page_size=page_size, result_agreement_max=result_agreement_max, result_agreement_min=result_agreement_min, result_confidence_max=result_confidence_max, result_confidence_min=result_confidence_min, result_source=result_source, result_taxon_ids=result_taxon_ids, result_uncertainty_max=result_uncertainty_max, result_uncertainty_min=result_uncertainty_min, review_type=review_type, status=status, updated_at_after=updated_at_after, updated_at_before=updated_at_before)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    annotator_ids = [56] # List[int] |  (optional)
    assignee_ids = [56] # List[int] |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    fully_predicted = True # bool | Filters identification task based on whether all associated photos have predictions. Set to True to include identification tasks where every photo has a prediction; set to False to include identification tasks where at least one photo is missing a prediction. (optional)
    is_flagged = True # bool |  (optional)
    is_safe = True # bool |  (optional)
    num_annotations_max = 56 # int |  (optional)
    num_annotations_min = 56 # int |  (optional)
    observation_country_ids = [56] # List[int] |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    result_agreement_max = 3.4 # float |  (optional)
    result_agreement_min = 3.4 # float |  (optional)
    result_confidence_max = None # decimal.Decimal |  (optional)
    result_confidence_min = None # decimal.Decimal |  (optional)
    result_source = ['result_source_example'] # List[str] |  (optional)
    result_taxon_ids = [56] # List[int] |  (optional)
    result_uncertainty_max = 3.4 # float |  (optional)
    result_uncertainty_min = 3.4 # float |  (optional)
    review_type = 'review_type_example' # str |  (optional)
    status = ['status_example'] # List[str] |  (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)

    try:
        api_response = api_instance.list(annotator_ids=annotator_ids, assignee_ids=assignee_ids, created_at_after=created_at_after, created_at_before=created_at_before, fully_predicted=fully_predicted, is_flagged=is_flagged, is_safe=is_safe, num_annotations_max=num_annotations_max, num_annotations_min=num_annotations_min, observation_country_ids=observation_country_ids, order_by=order_by, page=page, page_size=page_size, result_agreement_max=result_agreement_max, result_agreement_min=result_agreement_min, result_confidence_max=result_confidence_max, result_confidence_min=result_confidence_min, result_source=result_source, result_taxon_ids=result_taxon_ids, result_uncertainty_max=result_uncertainty_max, result_uncertainty_min=result_uncertainty_min, review_type=review_type, status=status, updated_at_after=updated_at_after, updated_at_before=updated_at_before)
        print("The response of IdentificationTasksApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotator_ids** | [**List[int]**](int.md)|  | [optional] 
 **assignee_ids** | [**List[int]**](int.md)|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **fully_predicted** | **bool**| Filters identification task based on whether all associated photos have predictions. Set to True to include identification tasks where every photo has a prediction; set to False to include identification tasks where at least one photo is missing a prediction. | [optional] 
 **is_flagged** | **bool**|  | [optional] 
 **is_safe** | **bool**|  | [optional] 
 **num_annotations_max** | **int**|  | [optional] 
 **num_annotations_min** | **int**|  | [optional] 
 **observation_country_ids** | [**List[int]**](int.md)|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **result_agreement_max** | **float**|  | [optional] 
 **result_agreement_min** | **float**|  | [optional] 
 **result_confidence_max** | **decimal.Decimal**|  | [optional] 
 **result_confidence_min** | **decimal.Decimal**|  | [optional] 
 **result_source** | [**List[str]**](str.md)|  | [optional] 
 **result_taxon_ids** | [**List[int]**](int.md)|  | [optional] 
 **result_uncertainty_max** | **float**|  | [optional] 
 **result_uncertainty_min** | **float**|  | [optional] 
 **review_type** | **str**|  | [optional] 
 **status** | [**List[str]**](str.md)|  | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 

### Return type

[**PaginatedIdentificationTaskList**](PaginatedIdentificationTaskList.md)

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
> PaginatedIdentificationTaskList list_mine(annotator_ids=annotator_ids, assignee_ids=assignee_ids, created_at_after=created_at_after, created_at_before=created_at_before, fully_predicted=fully_predicted, is_flagged=is_flagged, is_safe=is_safe, num_annotations_max=num_annotations_max, num_annotations_min=num_annotations_min, observation_country_ids=observation_country_ids, order_by=order_by, page=page, page_size=page_size, result_agreement_max=result_agreement_max, result_agreement_min=result_agreement_min, result_confidence_max=result_confidence_max, result_confidence_min=result_confidence_min, result_source=result_source, result_taxon_ids=result_taxon_ids, result_uncertainty_max=result_uncertainty_max, result_uncertainty_min=result_uncertainty_min, review_type=review_type, status=status, updated_at_after=updated_at_after, updated_at_before=updated_at_before)

Get identification tasks annotated by me

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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
    api_instance = mosquito_alert.IdentificationTasksApi(api_client)
    annotator_ids = [56] # List[int] |  (optional)
    assignee_ids = [56] # List[int] |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Created at (optional)
    fully_predicted = True # bool | Filters identification task based on whether all associated photos have predictions. Set to True to include identification tasks where every photo has a prediction; set to False to include identification tasks where at least one photo is missing a prediction. (optional)
    is_flagged = True # bool |  (optional)
    is_safe = True # bool |  (optional)
    num_annotations_max = 56 # int |  (optional)
    num_annotations_min = 56 # int |  (optional)
    observation_country_ids = [56] # List[int] |  (optional)
    order_by = ['order_by_example'] # List[str] | Ordenado   (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    result_agreement_max = 3.4 # float |  (optional)
    result_agreement_min = 3.4 # float |  (optional)
    result_confidence_max = None # decimal.Decimal |  (optional)
    result_confidence_min = None # decimal.Decimal |  (optional)
    result_source = ['result_source_example'] # List[str] |  (optional)
    result_taxon_ids = [56] # List[int] |  (optional)
    result_uncertainty_max = 3.4 # float |  (optional)
    result_uncertainty_min = 3.4 # float |  (optional)
    review_type = 'review_type_example' # str |  (optional)
    status = ['status_example'] # List[str] |  (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Update at (optional)

    try:
        api_response = api_instance.list_mine(annotator_ids=annotator_ids, assignee_ids=assignee_ids, created_at_after=created_at_after, created_at_before=created_at_before, fully_predicted=fully_predicted, is_flagged=is_flagged, is_safe=is_safe, num_annotations_max=num_annotations_max, num_annotations_min=num_annotations_min, observation_country_ids=observation_country_ids, order_by=order_by, page=page, page_size=page_size, result_agreement_max=result_agreement_max, result_agreement_min=result_agreement_min, result_confidence_max=result_confidence_max, result_confidence_min=result_confidence_min, result_source=result_source, result_taxon_ids=result_taxon_ids, result_uncertainty_max=result_uncertainty_max, result_uncertainty_min=result_uncertainty_min, review_type=review_type, status=status, updated_at_after=updated_at_after, updated_at_before=updated_at_before)
        print("The response of IdentificationTasksApi->list_mine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentificationTasksApi->list_mine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotator_ids** | [**List[int]**](int.md)|  | [optional] 
 **assignee_ids** | [**List[int]**](int.md)|  | [optional] 
 **created_at_after** | **datetime**| Created at | [optional] 
 **created_at_before** | **datetime**| Created at | [optional] 
 **fully_predicted** | **bool**| Filters identification task based on whether all associated photos have predictions. Set to True to include identification tasks where every photo has a prediction; set to False to include identification tasks where at least one photo is missing a prediction. | [optional] 
 **is_flagged** | **bool**|  | [optional] 
 **is_safe** | **bool**|  | [optional] 
 **num_annotations_max** | **int**|  | [optional] 
 **num_annotations_min** | **int**|  | [optional] 
 **observation_country_ids** | [**List[int]**](int.md)|  | [optional] 
 **order_by** | [**List[str]**](str.md)| Ordenado   | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **result_agreement_max** | **float**|  | [optional] 
 **result_agreement_min** | **float**|  | [optional] 
 **result_confidence_max** | **decimal.Decimal**|  | [optional] 
 **result_confidence_min** | **decimal.Decimal**|  | [optional] 
 **result_source** | [**List[str]**](str.md)|  | [optional] 
 **result_taxon_ids** | [**List[int]**](int.md)|  | [optional] 
 **result_uncertainty_max** | **float**|  | [optional] 
 **result_uncertainty_min** | **float**|  | [optional] 
 **review_type** | **str**|  | [optional] 
 **status** | [**List[str]**](str.md)|  | [optional] 
 **updated_at_after** | **datetime**| Update at | [optional] 
 **updated_at_before** | **datetime**| Update at | [optional] 

### Return type

[**PaginatedIdentificationTaskList**](PaginatedIdentificationTaskList.md)

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

# **predictions_create**
> CreatePhotoPrediction predictions_create(observation_uuid, create_photo_prediction_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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

# **predictions_destroy**
> predictions_destroy(observation_uuid, photo_uuid)

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

# **predictions_list**
> PaginatedPhotoPredictionList predictions_list(observation_uuid, page=page, page_size=page_size)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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

# **predictions_partial_update**
> PhotoPrediction predictions_partial_update(observation_uuid, photo_uuid, patched_photo_prediction_request=patched_photo_prediction_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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

# **predictions_retrieve**
> PhotoPrediction predictions_retrieve(observation_uuid, photo_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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

# **predictions_update**
> PhotoPrediction predictions_update(observation_uuid, photo_uuid, photo_prediction_request)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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
> IdentificationTask retrieve(observation_uuid)

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

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

