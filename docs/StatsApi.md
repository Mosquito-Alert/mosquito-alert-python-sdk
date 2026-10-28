# mosquito_alert.StatsApi

All URIs are relative to *https://api.mosquitoalert.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areas_list**](StatsApi.md#areas_list) | **GET** /stats/areas/ | 
[**reports_list**](StatsApi.md#reports_list) | **GET** /stats/reports/ | 


# **areas_list**
> List[StatsArea] areas_list()

Tree of areas (and their subdivisions) the current user can request statistics for. Each node's `key` is the value to send as `?area=` .

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.stats_area import StatsArea
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
    api_instance = mosquito_alert.StatsApi(api_client)

    try:
        api_response = api_instance.areas_list()
        print("The response of StatsApi->areas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->areas_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StatsArea]**](StatsArea.md)

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

# **reports_list**
> List[ReportStatsResponse] reports_list(area=area, cumulative=cumulative, date_from=date_from, date_to=date_to, group_by=group_by, interval=interval, level=level, type=type)

Aggregated report counts (for displaying data tables or charts, for example). The keys present on each row of `data` depend on `group_by` (always includes `count`, plus `date` if grouped by date, `region_id`/`region_code`/`region_name` if grouped by region, and `type` if grouped by type).

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (jwtAuth):

```python
import mosquito_alert
from mosquito_alert.models.report_stats_response import ReportStatsResponse
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
    api_instance = mosquito_alert.StatsApi(api_client)
    area = 'area_example' # str | \"\\<level\\>:\\<id\\>\", e.g. \"country:ES\" or \"nuts2:34\". (optional)
    cumulative = True # bool | Whether to return cumulative counts over time. It only applies when grouping by date. Defaults to False. (optional)
    date_from = 'date_from_example' # str |  (optional)
    date_to = 'date_to_example' # str |  (optional)
    group_by = ['group_by_example'] # List[str] | Comma-separated subset of: date, type, region. (optional)
    interval = 'interval_example' # str | The interval at which to aggregate data when grouping by date. Defaults to week. (optional)
    level = 56 # int | The NUTS level to aggregate by when grouping by region. Defaults to NUTS 2. (optional)
    type = ['type_example'] # List[str] | Comma-separated subset of: bite, adult, site. (optional)

    try:
        api_response = api_instance.reports_list(area=area, cumulative=cumulative, date_from=date_from, date_to=date_to, group_by=group_by, interval=interval, level=level, type=type)
        print("The response of StatsApi->reports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->reports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| \&quot;\\&lt;level\\&gt;:\\&lt;id\\&gt;\&quot;, e.g. \&quot;country:ES\&quot; or \&quot;nuts2:34\&quot;. | [optional] 
 **cumulative** | **bool**| Whether to return cumulative counts over time. It only applies when grouping by date. Defaults to False. | [optional] 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **group_by** | [**List[str]**](str.md)| Comma-separated subset of: date, type, region. | [optional] 
 **interval** | **str**| The interval at which to aggregate data when grouping by date. Defaults to week. | [optional] 
 **level** | **int**| The NUTS level to aggregate by when grouping by region. Defaults to NUTS 2. | [optional] 
 **type** | [**List[str]**](str.md)| Comma-separated subset of: bite, adult, site. | [optional] 

### Return type

[**List[ReportStatsResponse]**](ReportStatsResponse.md)

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

