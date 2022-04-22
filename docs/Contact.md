# Contact

# The Contact Object ### Description The `Contact` object is used to represent a contact in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**first_name** | **str, none_type** | The contact&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The contact&#39;s last name. | [optional] 
**account** | **str, none_type** |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] [readonly] 
**email_addresses** | [**[EmailAddress]**](EmailAddress.md) |  | [optional] [readonly] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] [readonly] 
**last_activity_at** | **datetime, none_type** | When the contact&#39;s last activity occurred. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s contact was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


