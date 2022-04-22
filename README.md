# MergeCRMClient
The unified API for building rich integrations with multiple CRM platforms.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.merge.dev/](https://www.merge.dev/)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/merge-api/merge-crm-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/merge-api/merge-crm-python.git`)

Then import the package:
```python
import MergeCRMClient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import MergeCRMClient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import MergeCRMClient
from pprint import pprint
from MergeCRMClient.api import account_details_api
from MergeCRMClient.model.account_details import AccountDetails
# Defining the host is optional and defaults to https://api.merge.dev/api/crm/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeCRMClient.Configuration(
    host = "https://api.merge.dev/api/crm/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with MergeCRMClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_details_api.AccountDetailsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    try:
        api_response = api_instance.account_details_retrieve(x_account_token)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling AccountDetailsApi->account_details_retrieve: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountDetailsApi* | [**account_details_retrieve**](docs/AccountDetailsApi.md#account_details_retrieve) | **GET** /account-details | 
*AccountTokenApi* | [**account_token_retrieve**](docs/AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 
*AccountsApi* | [**accounts_create**](docs/AccountsApi.md#accounts_create) | **POST** /accounts | 
*AccountsApi* | [**accounts_list**](docs/AccountsApi.md#accounts_list) | **GET** /accounts | 
*AccountsApi* | [**accounts_meta_post_retrieve**](docs/AccountsApi.md#accounts_meta_post_retrieve) | **GET** /accounts/meta/post | 
*AccountsApi* | [**accounts_retrieve**](docs/AccountsApi.md#accounts_retrieve) | **GET** /accounts/{id} | 
*AvailableActionsApi* | [**available_actions_retrieve**](docs/AvailableActionsApi.md#available_actions_retrieve) | **GET** /available-actions | 
*ContactsApi* | [**contacts_create**](docs/ContactsApi.md#contacts_create) | **POST** /contacts | 
*ContactsApi* | [**contacts_list**](docs/ContactsApi.md#contacts_list) | **GET** /contacts | 
*ContactsApi* | [**contacts_meta_post_retrieve**](docs/ContactsApi.md#contacts_meta_post_retrieve) | **GET** /contacts/meta/post | 
*ContactsApi* | [**contacts_retrieve**](docs/ContactsApi.md#contacts_retrieve) | **GET** /contacts/{id} | 
*DeleteAccountApi* | [**delete_account_create**](docs/DeleteAccountApi.md#delete_account_create) | **POST** /delete-account | 
*ForceResyncApi* | [**sync_status_resync_create**](docs/ForceResyncApi.md#sync_status_resync_create) | **POST** /sync-status/resync | 
*GenerateKeyApi* | [**generate_key_create**](docs/GenerateKeyApi.md#generate_key_create) | **POST** /generate-key | 
*IssuesApi* | [**issues_list**](docs/IssuesApi.md#issues_list) | **GET** /issues | 
*IssuesApi* | [**issues_retrieve**](docs/IssuesApi.md#issues_retrieve) | **GET** /issues/{id} | 
*LeadsApi* | [**leads_create**](docs/LeadsApi.md#leads_create) | **POST** /leads | 
*LeadsApi* | [**leads_list**](docs/LeadsApi.md#leads_list) | **GET** /leads | 
*LeadsApi* | [**leads_meta_post_retrieve**](docs/LeadsApi.md#leads_meta_post_retrieve) | **GET** /leads/meta/post | 
*LeadsApi* | [**leads_retrieve**](docs/LeadsApi.md#leads_retrieve) | **GET** /leads/{id} | 
*LinkTokenApi* | [**link_token_create**](docs/LinkTokenApi.md#link_token_create) | **POST** /link-token | 
*LinkedAccountsApi* | [**linked_accounts_list**](docs/LinkedAccountsApi.md#linked_accounts_list) | **GET** /linked-accounts | 
*NotesApi* | [**notes_create**](docs/NotesApi.md#notes_create) | **POST** /notes | 
*NotesApi* | [**notes_list**](docs/NotesApi.md#notes_list) | **GET** /notes | 
*NotesApi* | [**notes_meta_post_retrieve**](docs/NotesApi.md#notes_meta_post_retrieve) | **GET** /notes/meta/post | 
*NotesApi* | [**notes_retrieve**](docs/NotesApi.md#notes_retrieve) | **GET** /notes/{id} | 
*OpportunitiesApi* | [**opportunities_create**](docs/OpportunitiesApi.md#opportunities_create) | **POST** /opportunities | 
*OpportunitiesApi* | [**opportunities_list**](docs/OpportunitiesApi.md#opportunities_list) | **GET** /opportunities | 
*OpportunitiesApi* | [**opportunities_meta_post_retrieve**](docs/OpportunitiesApi.md#opportunities_meta_post_retrieve) | **GET** /opportunities/meta/post | 
*OpportunitiesApi* | [**opportunities_retrieve**](docs/OpportunitiesApi.md#opportunities_retrieve) | **GET** /opportunities/{id} | 
*PassthroughApi* | [**passthrough_create**](docs/PassthroughApi.md#passthrough_create) | **POST** /passthrough | 
*RegenerateKeyApi* | [**regenerate_key_create**](docs/RegenerateKeyApi.md#regenerate_key_create) | **POST** /regenerate-key | 
*StagesApi* | [**stages_list**](docs/StagesApi.md#stages_list) | **GET** /stages | 
*StagesApi* | [**stages_retrieve**](docs/StagesApi.md#stages_retrieve) | **GET** /stages/{id} | 
*SyncStatusApi* | [**sync_status_list**](docs/SyncStatusApi.md#sync_status_list) | **GET** /sync-status | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users | 
*UsersApi* | [**users_retrieve**](docs/UsersApi.md#users_retrieve) | **GET** /users/{id} | 
*WebhookReceiversApi* | [**webhook_receivers_create**](docs/WebhookReceiversApi.md#webhook_receivers_create) | **POST** /webhook-receivers | 
*WebhookReceiversApi* | [**webhook_receivers_list**](docs/WebhookReceiversApi.md#webhook_receivers_list) | **GET** /webhook-receivers | 


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountDetails](docs/AccountDetails.md)
 - [AccountDetailsAndActions](docs/AccountDetailsAndActions.md)
 - [AccountDetailsAndActionsIntegration](docs/AccountDetailsAndActionsIntegration.md)
 - [AccountDetailsAndActionsStatusEnum](docs/AccountDetailsAndActionsStatusEnum.md)
 - [AccountIntegration](docs/AccountIntegration.md)
 - [AccountRequest](docs/AccountRequest.md)
 - [AccountToken](docs/AccountToken.md)
 - [Address](docs/Address.md)
 - [AddressRequest](docs/AddressRequest.md)
 - [AddressTypeEnum](docs/AddressTypeEnum.md)
 - [AvailableActions](docs/AvailableActions.md)
 - [CRMAccountEndpointRequest](docs/CRMAccountEndpointRequest.md)
 - [CRMAccountResponse](docs/CRMAccountResponse.md)
 - [CRMContactEndpointRequest](docs/CRMContactEndpointRequest.md)
 - [CRMContactResponse](docs/CRMContactResponse.md)
 - [CategoriesEnum](docs/CategoriesEnum.md)
 - [CategoryEnum](docs/CategoryEnum.md)
 - [Contact](docs/Contact.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [CountryEnum](docs/CountryEnum.md)
 - [DataPassthroughRequest](docs/DataPassthroughRequest.md)
 - [DebugModeLog](docs/DebugModeLog.md)
 - [DebugModelLogSummary](docs/DebugModelLogSummary.md)
 - [EmailAddress](docs/EmailAddress.md)
 - [EmailAddressRequest](docs/EmailAddressRequest.md)
 - [EncodingEnum](docs/EncodingEnum.md)
 - [EndUserDetailsRequest](docs/EndUserDetailsRequest.md)
 - [ErrorValidationProblem](docs/ErrorValidationProblem.md)
 - [GenerateRemoteKeyRequest](docs/GenerateRemoteKeyRequest.md)
 - [Issue](docs/Issue.md)
 - [IssueStatusEnum](docs/IssueStatusEnum.md)
 - [Lead](docs/Lead.md)
 - [LeadEndpointRequest](docs/LeadEndpointRequest.md)
 - [LeadRequest](docs/LeadRequest.md)
 - [LeadResponse](docs/LeadResponse.md)
 - [LinkToken](docs/LinkToken.md)
 - [LinkedAccountStatus](docs/LinkedAccountStatus.md)
 - [MetaResponse](docs/MetaResponse.md)
 - [MethodEnum](docs/MethodEnum.md)
 - [ModelOperation](docs/ModelOperation.md)
 - [MultipartFormFieldRequest](docs/MultipartFormFieldRequest.md)
 - [Note](docs/Note.md)
 - [NoteEndpointRequest](docs/NoteEndpointRequest.md)
 - [NoteRequest](docs/NoteRequest.md)
 - [NoteResponse](docs/NoteResponse.md)
 - [Opportunity](docs/Opportunity.md)
 - [OpportunityEndpointRequest](docs/OpportunityEndpointRequest.md)
 - [OpportunityRequest](docs/OpportunityRequest.md)
 - [OpportunityResponse](docs/OpportunityResponse.md)
 - [OpportunityStatusEnum](docs/OpportunityStatusEnum.md)
 - [PaginatedAccountDetailsAndActionsList](docs/PaginatedAccountDetailsAndActionsList.md)
 - [PaginatedAccountList](docs/PaginatedAccountList.md)
 - [PaginatedContactList](docs/PaginatedContactList.md)
 - [PaginatedIssueList](docs/PaginatedIssueList.md)
 - [PaginatedLeadList](docs/PaginatedLeadList.md)
 - [PaginatedNoteList](docs/PaginatedNoteList.md)
 - [PaginatedOpportunityList](docs/PaginatedOpportunityList.md)
 - [PaginatedStageList](docs/PaginatedStageList.md)
 - [PaginatedSyncStatusList](docs/PaginatedSyncStatusList.md)
 - [PaginatedUserList](docs/PaginatedUserList.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PhoneNumberRequest](docs/PhoneNumberRequest.md)
 - [RemoteKey](docs/RemoteKey.md)
 - [RemoteKeyForRegenerationRequest](docs/RemoteKeyForRegenerationRequest.md)
 - [RemoteResponse](docs/RemoteResponse.md)
 - [RequestFormatEnum](docs/RequestFormatEnum.md)
 - [Stage](docs/Stage.md)
 - [SyncStatus](docs/SyncStatus.md)
 - [SyncStatusStatusEnum](docs/SyncStatusStatusEnum.md)
 - [User](docs/User.md)
 - [ValidationProblemSource](docs/ValidationProblemSource.md)
 - [WarningValidationProblem](docs/WarningValidationProblem.md)
 - [WebhookReceiver](docs/WebhookReceiver.md)
 - [WebhookReceiverRequest](docs/WebhookReceiverRequest.md)


## Documentation For Authorization


## tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@merge.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in MergeCRMClient.apis and MergeCRMClient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from MergeCRMClient.api.default_api import DefaultApi`
- `from MergeCRMClient.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import MergeCRMClient
from MergeCRMClient.apis import *
from MergeCRMClient.models import *
```

