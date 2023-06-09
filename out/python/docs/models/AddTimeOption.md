# openapi_client.model.add_time_option.AddTimeOption

AddTimeOption options for adding time to an issue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AddTimeOption options for adding time to an issue | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | decimal.Decimal, int,  | decimal.Decimal,  | time in seconds | value must be a 64 bit integer
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**user_name** | str,  | str,  | User who spent the time (optional) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

