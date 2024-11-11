# PredictionScoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ae_albopictus** | **float** | Score value for the class Aedes albopictus | 
**ae_aegypti** | **float** | Score value for the class Aedes aegypti | 
**ae_japonicus** | **float** | Score value for the class Aedes japonicus | 
**ae_koreicus** | **float** | Score value for the class Aedes koreicus | 
**culex** | **float** | Score value for the class Culex (s.p) | 
**anopheles** | **float** | Score value for the class Anopheles (s.p.) | 
**culiseta** | **float** | Score value for the class Culiseta (s.p.) | 
**other_species** | **float** | Score value for the class Ohter species | 
**not_sure** | **float** | Score value for the class Unidentifiable | 

## Example

```python
from mosquito_alert_api.models.prediction_score_request import PredictionScoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionScoreRequest from a JSON string
prediction_score_request_instance = PredictionScoreRequest.from_json(json)
# print the JSON string representation of the object
print(PredictionScoreRequest.to_json())

# convert the object into a dict
prediction_score_request_dict = prediction_score_request_instance.to_dict()
# create an instance of PredictionScoreRequest from a dict
prediction_score_request_from_dict = PredictionScoreRequest.from_dict(prediction_score_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


