# mosquito-alert
Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Mosquito_Alert/mosquito-alert-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Mosquito_Alert/mosquito-alert-python-sdk.git`)

Then import the package:
```python
import mosquito_alert
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mosquito_alert
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    bite_request = mosquito_alert.BiteRequest() # BiteRequest | 

    try:
        api_response = api_instance.bites_create(bite_request)
        print("The response of BitesApi->bites_create:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BitesApi->bites_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mosquitoalert.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BitesApi* | [**bites_create**](docs/BitesApi.md#bites_create) | **POST** /bites/ | 
*BitesApi* | [**bites_destroy**](docs/BitesApi.md#bites_destroy) | **DELETE** /bites/{uuid}/ | 
*BitesApi* | [**bites_list**](docs/BitesApi.md#bites_list) | **GET** /bites/ | 
*BitesApi* | [**bites_retrieve**](docs/BitesApi.md#bites_retrieve) | **GET** /bites/{uuid}/ | 
*BreedingSitesApi* | [**breeding_sites_create**](docs/BreedingSitesApi.md#breeding_sites_create) | **POST** /breeding-sites/ | 
*BreedingSitesApi* | [**breeding_sites_destroy**](docs/BreedingSitesApi.md#breeding_sites_destroy) | **DELETE** /breeding-sites/{uuid}/ | 
*BreedingSitesApi* | [**breeding_sites_list**](docs/BreedingSitesApi.md#breeding_sites_list) | **GET** /breeding-sites/ | 
*BreedingSitesApi* | [**breeding_sites_retrieve**](docs/BreedingSitesApi.md#breeding_sites_retrieve) | **GET** /breeding-sites/{uuid}/ | 
*CampaignsApi* | [**campaigns_list**](docs/CampaignsApi.md#campaigns_list) | **GET** /campaigns/ | 
*CampaignsApi* | [**campaigns_retrieve**](docs/CampaignsApi.md#campaigns_retrieve) | **GET** /campaigns/{id}/ | 
*CountriesApi* | [**countries_retrieve**](docs/CountriesApi.md#countries_retrieve) | **GET** /countries/{id}/ | 
*FixesApi* | [**fixes_create**](docs/FixesApi.md#fixes_create) | **POST** /fixes/ | 
*NotificationsApi* | [**notifications_create**](docs/NotificationsApi.md#notifications_create) | **POST** /notifications/ | 
*NotificationsApi* | [**notifications_list**](docs/NotificationsApi.md#notifications_list) | **GET** /notifications/ | 
*NotificationsApi* | [**notifications_partial_update**](docs/NotificationsApi.md#notifications_partial_update) | **PATCH** /notifications/{id}/ | 
*NotificationsApi* | [**notifications_retrieve**](docs/NotificationsApi.md#notifications_retrieve) | **GET** /notifications/{id}/ | 
*NotificationsApi* | [**notifications_update**](docs/NotificationsApi.md#notifications_update) | **PUT** /notifications/{id}/ | 
*ObservationsApi* | [**observations_create**](docs/ObservationsApi.md#observations_create) | **POST** /observations/ | 
*ObservationsApi* | [**observations_destroy**](docs/ObservationsApi.md#observations_destroy) | **DELETE** /observations/{uuid}/ | 
*ObservationsApi* | [**observations_list**](docs/ObservationsApi.md#observations_list) | **GET** /observations/ | 
*ObservationsApi* | [**observations_prediction_create**](docs/ObservationsApi.md#observations_prediction_create) | **POST** /observations/{uuid}/prediction/ | 
*ObservationsApi* | [**observations_prediction_destroy**](docs/ObservationsApi.md#observations_prediction_destroy) | **DELETE** /observations/{uuid}/prediction/ | 
*ObservationsApi* | [**observations_prediction_retrieve**](docs/ObservationsApi.md#observations_prediction_retrieve) | **GET** /observations/{uuid}/prediction/ | 
*ObservationsApi* | [**observations_retrieve**](docs/ObservationsApi.md#observations_retrieve) | **GET** /observations/{uuid}/ | 
*PartnersApi* | [**partners_list**](docs/PartnersApi.md#partners_list) | **GET** /partners/ | 
*PartnersApi* | [**partners_retrieve**](docs/PartnersApi.md#partners_retrieve) | **GET** /partners/{id}/ | 
*PhotosApi* | [**photos_prediction_create**](docs/PhotosApi.md#photos_prediction_create) | **POST** /photos/{uuid}/prediction/ | 
*PhotosApi* | [**photos_prediction_destroy**](docs/PhotosApi.md#photos_prediction_destroy) | **DELETE** /photos/{uuid}/prediction/ | 
*PhotosApi* | [**photos_prediction_retrieve**](docs/PhotosApi.md#photos_prediction_retrieve) | **GET** /photos/{uuid}/prediction/ | 
*PhotosApi* | [**photos_retrieve**](docs/PhotosApi.md#photos_retrieve) | **GET** /photos/{uuid}/ | 
*TokenApi* | [**token_create**](docs/TokenApi.md#token_create) | **POST** /token/ | 
*TokenApi* | [**token_refresh_create**](docs/TokenApi.md#token_refresh_create) | **POST** /token/refresh/ | 
*UsersApi* | [**users_create**](docs/UsersApi.md#users_create) | **POST** /users/ | 
*UsersApi* | [**users_partial_update**](docs/UsersApi.md#users_partial_update) | **PATCH** /users/{uuid}/ | 
*UsersApi* | [**users_retrieve**](docs/UsersApi.md#users_retrieve) | **GET** /users/{uuid}/ | 
*UsersApi* | [**users_update**](docs/UsersApi.md#users_update) | **PUT** /users/{uuid}/ | 


## Documentation For Models

 - [AppUserTokenObtainPair](docs/AppUserTokenObtainPair.md)
 - [AppUserTokenObtainPairRequest](docs/AppUserTokenObtainPairRequest.md)
 - [BaseNotificationCreate](docs/BaseNotificationCreate.md)
 - [Bite](docs/Bite.md)
 - [BiteRequest](docs/BiteRequest.md)
 - [BoundingBox](docs/BoundingBox.md)
 - [BoundingBoxRequest](docs/BoundingBoxRequest.md)
 - [BreedingSite](docs/BreedingSite.md)
 - [BreedingSiteRequest](docs/BreedingSiteRequest.md)
 - [Campaign](docs/Campaign.md)
 - [Country](docs/Country.md)
 - [CreateUser](docs/CreateUser.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [DetailNotification](docs/DetailNotification.md)
 - [DetailNotificationRequest](docs/DetailNotificationRequest.md)
 - [Device](docs/Device.md)
 - [DeviceRequest](docs/DeviceRequest.md)
 - [Fix](docs/Fix.md)
 - [FixLocation](docs/FixLocation.md)
 - [FixLocationRequest](docs/FixLocationRequest.md)
 - [FixRequest](docs/FixRequest.md)
 - [MetaNotificationRequest](docs/MetaNotificationRequest.md)
 - [Observation](docs/Observation.md)
 - [ObservationPrediction](docs/ObservationPrediction.md)
 - [ObservationPredictionRequest](docs/ObservationPredictionRequest.md)
 - [ObservationRequest](docs/ObservationRequest.md)
 - [Package](docs/Package.md)
 - [PackageRequest](docs/PackageRequest.md)
 - [PaginatedBiteList](docs/PaginatedBiteList.md)
 - [PaginatedBreedingSiteList](docs/PaginatedBreedingSiteList.md)
 - [PaginatedCampaignList](docs/PaginatedCampaignList.md)
 - [PaginatedDetailNotificationList](docs/PaginatedDetailNotificationList.md)
 - [PaginatedObservationList](docs/PaginatedObservationList.md)
 - [PaginatedPartnerList](docs/PaginatedPartnerList.md)
 - [Partner](docs/Partner.md)
 - [PartnerPoint](docs/PartnerPoint.md)
 - [PatchedDetailNotificationRequest](docs/PatchedDetailNotificationRequest.md)
 - [PatchedUserRequest](docs/PatchedUserRequest.md)
 - [Photo](docs/Photo.md)
 - [PhotoPrediction](docs/PhotoPrediction.md)
 - [PhotoPredictionRequest](docs/PhotoPredictionRequest.md)
 - [PredictionScore](docs/PredictionScore.md)
 - [PredictionScoreRequest](docs/PredictionScoreRequest.md)
 - [ReportLocation](docs/ReportLocation.md)
 - [ReportLocationPoint](docs/ReportLocationPoint.md)
 - [ReportLocationRequest](docs/ReportLocationRequest.md)
 - [ReportPhoto](docs/ReportPhoto.md)
 - [ReportPhotoRequest](docs/ReportPhotoRequest.md)
 - [TokenRefresh](docs/TokenRefresh.md)
 - [TokenRefreshRequest](docs/TokenRefreshRequest.md)
 - [TopicNotificationCreateRequest](docs/TopicNotificationCreateRequest.md)
 - [User](docs/User.md)
 - [UserNotificationCreateRequest](docs/UserNotificationCreateRequest.md)
 - [UserRequest](docs/UserRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="cookieAuth"></a>
### cookieAuth

- **Type**: API key
- **API key parameter name**: sessionid
- **Location**: 

<a id="jwtAuth"></a>
### jwtAuth

- **Type**: Bearer authentication (JWT)

<a id="tokenAuth"></a>
### tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

it@mosquitoalert.com


