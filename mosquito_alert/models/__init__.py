# coding: utf-8

# flake8: noqa
"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from mosquito_alert.models.app_user_token_obtain_pair import AppUserTokenObtainPair
from mosquito_alert.models.app_user_token_obtain_pair_request import AppUserTokenObtainPairRequest
from mosquito_alert.models.bite import Bite
from mosquito_alert.models.bite_request import BiteRequest
from mosquito_alert.models.bounding_box import BoundingBox
from mosquito_alert.models.bounding_box_request import BoundingBoxRequest
from mosquito_alert.models.breeding_site import BreedingSite
from mosquito_alert.models.breeding_site_request import BreedingSiteRequest
from mosquito_alert.models.campaign import Campaign
from mosquito_alert.models.country import Country
from mosquito_alert.models.create_notification import CreateNotification
from mosquito_alert.models.create_user import CreateUser
from mosquito_alert.models.create_user_request import CreateUserRequest
from mosquito_alert.models.device import Device
from mosquito_alert.models.device_os import DeviceOs
from mosquito_alert.models.device_os_request import DeviceOsRequest
from mosquito_alert.models.device_request import DeviceRequest
from mosquito_alert.models.device_update import DeviceUpdate
from mosquito_alert.models.device_update_request import DeviceUpdateRequest
from mosquito_alert.models.fix import Fix
from mosquito_alert.models.fix_location import FixLocation
from mosquito_alert.models.fix_location_request import FixLocationRequest
from mosquito_alert.models.fix_request import FixRequest
from mosquito_alert.models.location import Location
from mosquito_alert.models.location_point import LocationPoint
from mosquito_alert.models.location_request import LocationRequest
from mosquito_alert.models.meta_notification_request import MetaNotificationRequest
from mosquito_alert.models.mobile_app import MobileApp
from mosquito_alert.models.mobile_app_request import MobileAppRequest
from mosquito_alert.models.notification import Notification
from mosquito_alert.models.notification_request import NotificationRequest
from mosquito_alert.models.observation import Observation
from mosquito_alert.models.observation_prediction import ObservationPrediction
from mosquito_alert.models.observation_prediction_request import ObservationPredictionRequest
from mosquito_alert.models.observation_request import ObservationRequest
from mosquito_alert.models.paginated_bite_list import PaginatedBiteList
from mosquito_alert.models.paginated_breeding_site_list import PaginatedBreedingSiteList
from mosquito_alert.models.paginated_campaign_list import PaginatedCampaignList
from mosquito_alert.models.paginated_notification_list import PaginatedNotificationList
from mosquito_alert.models.paginated_observation_list import PaginatedObservationList
from mosquito_alert.models.paginated_partner_list import PaginatedPartnerList
from mosquito_alert.models.partner import Partner
from mosquito_alert.models.partner_point import PartnerPoint
from mosquito_alert.models.patched_device_update_request import PatchedDeviceUpdateRequest
from mosquito_alert.models.patched_notification_request import PatchedNotificationRequest
from mosquito_alert.models.patched_user_request import PatchedUserRequest
from mosquito_alert.models.photo import Photo
from mosquito_alert.models.photo_prediction import PhotoPrediction
from mosquito_alert.models.photo_prediction_request import PhotoPredictionRequest
from mosquito_alert.models.prediction_score import PredictionScore
from mosquito_alert.models.prediction_score_request import PredictionScoreRequest
from mosquito_alert.models.simple_photo import SimplePhoto
from mosquito_alert.models.simple_photo_request import SimplePhotoRequest
from mosquito_alert.models.token_refresh import TokenRefresh
from mosquito_alert.models.token_refresh_request import TokenRefreshRequest
from mosquito_alert.models.topic_notification_create_request import TopicNotificationCreateRequest
from mosquito_alert.models.user import User
from mosquito_alert.models.user_notification_create_request import UserNotificationCreateRequest
from mosquito_alert.models.user_request import UserRequest
