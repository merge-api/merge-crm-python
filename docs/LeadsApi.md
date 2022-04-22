# MergeCRMClient.LeadsApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leads_create**](LeadsApi.md#leads_create) | **POST** /leads | 
[**leads_list**](LeadsApi.md#leads_list) | **GET** /leads | 
[**leads_meta_post_retrieve**](LeadsApi.md#leads_meta_post_retrieve) | **GET** /leads/meta/post | 
[**leads_retrieve**](LeadsApi.md#leads_retrieve) | **GET** /leads/{id} | 


# **leads_create**
> LeadResponse leads_create(x_account_token, lead_endpoint_request)



Creates a `Lead` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import leads_api
from MergeCRMClient.model.lead_endpoint_request import LeadEndpointRequest
from MergeCRMClient.model.lead_response import LeadResponse
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
    api_instance = leads_api.LeadsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    lead_endpoint_request = LeadEndpointRequest(
        model=LeadRequest(
            remote_id="19202938",
            owner="0358cbc6-2040-430a-848e-aafacbadf3aa",
            lead_source="API Blogger",
            title="Co-Founder",
            company="Merge API",
            first_name="Gil",
            last_name="Feig",
            remote_updated_at=dateutil_parser('2022-02-10T00:00:00Z'),
            remote_created_at=dateutil_parser('2021-11-10T00:00:00Z'),
            converted_date=dateutil_parser('2022-03-10T00:00:00Z'),
            converted_contact="converted_contact_example",
            converted_account="9c9de072-29cf-48e3-9578-1ca5b145b40e",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # LeadEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.leads_create(x_account_token, lead_endpoint_request)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_create(x_account_token, lead_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **lead_endpoint_request** | [**LeadEndpointRequest**](LeadEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**LeadResponse**](LeadResponse.md)

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

# **leads_list**
> PaginatedLeadList leads_list(x_account_token)



Returns a list of `Lead` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import leads_api
from MergeCRMClient.model.paginated_lead_list import PaginatedLeadList
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
    api_instance = leads_api.LeadsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    converted_account_id = "converted_account_id_example" # str | If provided, will only return leads with this account. (optional)
    converted_contact_id = "converted_contact_id_example" # str | If provided, will only return leads with this contact. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "owner,converted_contact,converted_account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was deleted in the third-party service. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    owner_id = "owner_id_example" # str | If provided, will only return leads with this owner. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.leads_list(x_account_token)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_list(x_account_token, converted_account_id=converted_account_id, converted_contact_id=converted_contact_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, owner_id=owner_id, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **converted_account_id** | **str**| If provided, will only return leads with this account. | [optional]
 **converted_contact_id** | **str**| If provided, will only return leads with this contact. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was deleted in the third-party service. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **owner_id** | **str**| If provided, will only return leads with this owner. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedLeadList**](PaginatedLeadList.md)

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

# **leads_meta_post_retrieve**
> MetaResponse leads_meta_post_retrieve(x_account_token)



Returns metadata for `Lead` POSTs.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import leads_api
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
    api_instance = leads_api.LeadsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.leads_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_meta_post_retrieve: %s\n" % e)
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

# **leads_retrieve**
> Lead leads_retrieve(x_account_token, id)



Returns a `Lead` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeCRMClient
from MergeCRMClient.api import leads_api
from MergeCRMClient.model.lead import Lead
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
    api_instance = leads_api.LeadsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "owner,converted_contact,converted_account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.leads_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeCRMClient.ApiException as e:
        print("Exception when calling LeadsApi->leads_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Lead**](Lead.md)

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

