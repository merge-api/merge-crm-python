# MergeCRMClient.NotesApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notes_create**](NotesApi.md#notes_create) | **POST** /notes | 
[**notes_list**](NotesApi.md#notes_list) | **GET** /notes | 
[**notes_meta_post_retrieve**](NotesApi.md#notes_meta_post_retrieve) | **GET** /notes/meta/post | 
[**notes_retrieve**](NotesApi.md#notes_retrieve) | **GET** /notes/{id} | 


# **notes_create**
> NoteResponse notes_create(x_account_token, note_endpoint_request)



Creates a `Note` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import notes_api
from MergeCRMClient.model.note_endpoint_request import NoteEndpointRequest
from MergeCRMClient.model.note_response import NoteResponse
from pprint import pprint
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
    api_instance = notes_api.NotesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    note_endpoint_request = NoteEndpointRequest(
        model=NoteRequest(
            remote_id="19202938",
            owner="0358cbc6-2040-430a-848e-aafacbadf3aa",
            content="Merge is hiring!",
            contact="contact_example",
            account="fba1fbc6-67c0-4cb2-a176-7896acd2ffd5",
            opportunity="754a244e-dd67-4731-a8d3-9bff9dc10465",
            remote_updated_at=dateutil_parser('2022-02-10T00:00:00Z'),
            remote_created_at=dateutil_parser('2021-11-10T00:00:00Z'),
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # NoteEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.notes_create(x_account_token, note_endpoint_request)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.notes_create(x_account_token, note_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **note_endpoint_request** | [**NoteEndpointRequest**](NoteEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_list**
> PaginatedNoteList notes_list(x_account_token)



Returns a list of `Note` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import notes_api
from MergeCRMClient.model.paginated_note_list import PaginatedNoteList
from pprint import pprint
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
    api_instance = notes_api.NotesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    account_id = "account_id_example" # str | If provided, will only return notes with this account. (optional)
    contact_id = "contact_id_example" # str | If provided, will only return notes with this contact. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "owner,contact,account,opportunity" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    opportunity_id = "opportunity_id_example" # str | If provided, will only return notes with this opportunity. (optional)
    owner_id = "owner_id_example" # str | If provided, will only return notes with this owner. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.notes_list(x_account_token)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.notes_list(x_account_token, account_id=account_id, contact_id=contact_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, opportunity_id=opportunity_id, owner_id=owner_id, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **account_id** | **str**| If provided, will only return notes with this account. | [optional]
 **contact_id** | **str**| If provided, will only return notes with this contact. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **opportunity_id** | **str**| If provided, will only return notes with this opportunity. | [optional]
 **owner_id** | **str**| If provided, will only return notes with this owner. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedNoteList**](PaginatedNoteList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_meta_post_retrieve**
> MetaResponse notes_meta_post_retrieve(x_account_token)



Returns metadata for `Note` POSTs.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import notes_api
from MergeCRMClient.model.meta_response import MetaResponse
from pprint import pprint
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
    api_instance = notes_api.NotesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.notes_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_meta_post_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

### Return type

[**MetaResponse**](MetaResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_retrieve**
> Note notes_retrieve(x_account_token, id)



Returns a `Note` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import notes_api
from MergeCRMClient.model.note import Note
from pprint import pprint
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
    api_instance = notes_api.NotesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "owner,contact,account,opportunity" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.notes_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.notes_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling NotesApi->notes_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Note**](Note.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

