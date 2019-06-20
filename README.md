# gcp_log_grouper
A script to group log records dumped from Google Cloud Logging by GCP > Logging > Download logs (JSON).


Command:
```
python group_gcp_logs.py gae_app_module_id_service__logs__2019-06-20T12-53.json
```

will turn:
```
[
  {
    "protoPayload": {
      "@type": "type.googleapis.com/google.appengine.logging.v1.RequestLog",
      "versionId": "1",
      "requestId": "5d0b579700ff06cb6bc8a5d5f20001737e6f64696e2d6578740001736572766963653a31000100",
      "ip": "35.195..",
      "startTime": "2019-06-20T09:53:27.445291Z",
      "endTime": "2019-06-20T09:53:27.669205Z",
      "method": "DELETE",
      "resource": "/auxapi/v0/company/VA-260-680/",
      "status": 500,
      "line": [
        {
          "time": "2019-06-20T09:53:27.453428Z",
          "severity": "ERROR",
          "logMessage": "2019-06-20 09:53:27,453 access_logger INFO Start request DELETE /auxapi/v0/company/VA-260-680/ (95dc1d02-6231-4f64-87e7-d40094f0e845)"
        },
        ...
      ],
      "traceId": "1f871092b15a3a1f37a2b88f5471b61a",
    }
    ...
  },
  {
    "protoPayload": {...},
    ...
  }
  ```


into:
```
{
  "groups": {
    "/api/v1/books/?limit=10&offset=0&status__in=published%2Cissued": {
      "GET": {
        "errors": [
          {
            "ts": "2019-06-20T12:51:18.241439Z",
            "trace_id": "a7c4209aec1e096ad0526dafaf87c015",
            "last_lines": [
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'extra log': '', 'unique id': '88c408f8-5f7f-433a-b8fb-71239fb09fff', 'headers': {'HTTP_X_FORWARDED_HOST': 'api.int.cloud.im', 'HTTP_REFERER': 'https://vendor.connect.cloud.im/requests?account=VA-802-699', 'HTTP_X_APPENGINE_COUNTRY': 'US', 'HTTP_X_APPENGINE_CITYLATLONG': '0.000000,0.000000', 'HTTP_X_FORWARDED_PORT': '8443', 'HTTP_X_REAL_IP': '10.240.0.42', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', 'REMOTE_ADDR': '35.192.100.135', 'HTTP_VIA': '1.1 google', 'HTTP_X_APPENGINE_REGION': '?', 'HTTP_CONNECT_REQUEST_ID': '88c408f8-5f7f-433a-b8fb-71239fb09fff', 'HTTP_PRAGMA': 'no-cache', 'HTTP_X_FORWARDED_PROTO': 'https', 'HTTP_HOST': 'service-dot-sweeftservice.appspot.com', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_ACCEPT': '*/*', 'HTTP_X_REQUEST_ORIGIN': 'vendor.connect.cloud.im', 'HTTP_X_APPENGINE_CITY': '?', 'HTTP_X_COMPANY_ID': 'VA-802-699', 'HTTP_X_FORWARDED_FOR': '83.36.170.114, 35.190.95.53, 130.211.2.116, 10.240.0.42', 'HTTP_ACCEPT_LANGUAGE': 'es-ES,es;q=0.9,en;q=0.8', 'HTTP_X_GOOG_CLOUD_TRACE_PARENT': '00-a7c4209aec1e096ad0526dafaf87c015-ee42892cd805e438-00', 'HTTP_X_CLOUD_TRACE_CONTEXT': 'a7c4209aec1e096ad0526dafaf87c015/13517715098482273203'}, 'request time': 0.007979869842529297, 'user': u'marc.serratbote@ingrammicro.com'}",
              "2019-06-20 12:51:20,444 access_logger INFO Tastypie return response (88c408f8-5f7f-433a-b8fb-71239fb09fff)",
              "KeyError: u'authoR'",
              "    lambda name: compose_libraries(name, archive_map[name], fresh_books_map[name]),"
            ]
          },
          {
            "ts": "2019-06-20T12:51:05.034336Z",
            "trace_id": "b890847f9555c0edc6a252a37fbd901d",
            "last_lines": [
              "2019-06-20 12:51:07,311 access_logger INFO {'body': '', 'extra log': '', 'unique id': '1f9a7e0c-dbb2-46f9-80bd-4d56e8e3c076', 'headers': {'HTTP_X_FORWARDED_HOST': 'api.int.cloud.im', 'HTTP_REFERER': 'https://vendor.connect.cloud.im/requests?account=VA-802-699', 'HTTP_X_APPENGINE_COUNTRY': 'US', 'HTTP_X_APPENGINE_CITYLATLONG': '0.000000,0.000000', 'HTTP_X_FORWARDED_PORT': '8443', 'HTTP_X_REAL_IP': '10.240.0.48', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', 'REMOTE_ADDR': '35.192.100.135', 'HTTP_VIA': '1.1 google', 'HTTP_X_APPENGINE_REGION': '?', 'HTTP_CONNECT_REQUEST_ID': '1f9a7e0c-dbb2-46f9-80bd-4d56e8e3c076', 'HTTP_PRAGMA': 'no-cache', 'HTTP_X_FORWARDED_PROTO': 'https', 'HTTP_HOST': 'service-dot-sweeftservice.appspot.com', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_ACCEPT': '*/*', 'HTTP_X_REQUEST_ORIGIN': 'vendor.connect.cloud.im', 'HTTP_X_APPENGINE_CITY': '?', 'HTTP_X_COMPANY_ID': 'VA-802-699', 'HTTP_X_FORWARDED_FOR': '83.36.170.114, 35.190.95.53, 130.211.2.122, 10.240.0.48', 'HTTP_ACCEPT_LANGUAGE': 'es-ES,es;q=0.9,en;q=0.8', 'HTTP_X_GOOG_CLOUD_TRACE_PARENT': '00-b890847f9555c0edc6a252a37fbd901d-9b0bd3495a4fc898-00', 'HTTP_X_CLOUD_TRACE_CONTEXT': 'b890847f9555c0edc6a252a37fbd901d/17548499153578551330'}, 'request time': 0.8844659328460693, 'user': u'marc.serratbote@ingrammicro.com'}",
              "2019-06-20 12:51:07,308 access_logger INFO Tastypie return response (1f9a7e0c-dbb2-46f9-80bd-4d56e8e3c076)",
              "KeyError: u'authoR'",
              "    lambda name: compose_libraries(name, archive_map[name], fresh_books_map[name]),"
            ]
          },
        ],
        "total": 100
      },
      "total": 100
    }
  },
  "total": 100
}
```