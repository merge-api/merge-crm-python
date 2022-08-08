# Lead

# The Lead Object ### Description The `Lead` object is used to represent a lead in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**owner** | **str, none_type** |  | [optional] 
**lead_source** | **str, none_type** | The lead&#39;s source. | [optional] 
**title** | **str, none_type** | The lead&#39;s title. | [optional] 
**company** | **str, none_type** | The lead&#39;s company. | [optional] 
**first_name** | **str, none_type** | The lead&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The lead&#39;s last name. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] [readonly] 
**email_addresses** | [**[EmailAddress]**](EmailAddress.md) |  | [optional] [readonly] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] [readonly] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s lead was updated. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s lead was created. | [optional] 
**converted_date** | **datetime, none_type** | When the lead was converted. | [optional] 
**converted_contact** | **str, none_type** |  | [optional] 
**converted_account** | **str, none_type** |  | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


