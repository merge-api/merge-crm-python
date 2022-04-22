# Account

# The Account Object ### Description The `Account` object is used to represent an account in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**owner** | **str, none_type** |  | [optional] 
**name** | **str, none_type** | The account&#39;s name. | [optional] 
**description** | **str, none_type** | The account&#39;s description. | [optional] 
**industry** | **str, none_type** | The account&#39;s industry. | [optional] 
**website** | **str, none_type** | The account&#39;s website. | [optional] 
**number_of_employees** | **int, none_type** | The account&#39;s number of employees. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] [readonly] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] [readonly] 
**last_activity_at** | **datetime, none_type** | When the account&#39;s last activity  occurred. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s account was updated. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s account was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


