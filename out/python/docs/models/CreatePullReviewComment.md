# openapi_client.model.create_pull_review_comment.CreatePullReviewComment

CreatePullReviewComment represent a review comment for creation api

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreatePullReviewComment represent a review comment for creation api | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**body** | str,  | str,  |  | [optional] 
**new_position** | decimal.Decimal, int,  | decimal.Decimal,  | if comment to new file line or 0 | [optional] value must be a 64 bit integer
**old_position** | decimal.Decimal, int,  | decimal.Decimal,  | if comment to old file line or 0 | [optional] value must be a 64 bit integer
**path** | str,  | str,  | the tree path | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

