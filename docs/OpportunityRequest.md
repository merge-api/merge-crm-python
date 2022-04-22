# OpportunityRequest

# The Opportunity Object ### Description The `Opportunity` object is used to represent an opportunity in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The opportunity&#39;s name. | [optional] 
**description** | **str, none_type** | The opportunity&#39;s description. | [optional] 
**amount** | **int, none_type** | The opportunity&#39;s amount. | [optional] 
**owner** | **str, none_type** |  | [optional] 
**account** | **str, none_type** |  | [optional] 
**stage** | **str, none_type** |  | [optional] 
**status** | **object, none_type** | The opportunity&#39;s status. | [optional] 
**last_activity_at** | **datetime, none_type** | When the opportunity&#39;s last activity occurred. | [optional] 
**close_date** | **datetime, none_type** | When the opportunity was closed. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s opportunity was created. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


