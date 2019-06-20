# gcp_log_grouper
A script to group log records dumped from Google Cloud Logging by GCP > Logging > Download logs (JSON).


Command:
```
python group_gcp_logs.py gae_app_module_id_service__logs__2019-06-20T12-53.json
```

will turn:
```
#!json
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
  // yet another 100 of log records
]
```


into:
```
#!json
{
  "groups": {
    "/api/v1/books/?limit=10&offset=0&status__in=published%2Cissued": {
      "GET": {
        "errors": [
          {
            "ts": "2019-06-20T12:51:18.241439Z",
            "trace_id": "a7c4209aec1e096ad0526dafaf87c015",
            "last_lines": [
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'extra log': '', 'unique id': '88c408f8-5f7f-433a-b8fb-71239fb09fff', 'headers': {...}, 'request time': 0.007979869842529297, 'user': u'author@books.org'}",
              "2019-06-20 12:51:20,444 access_logger INFO Tastypie return response (88c408f8-5f7f-433a-b8fb-71239fb09fff)",
              "KeyError: u'authoR'",
              "    lambda name: compose_libraries(name, archive_map[name], fresh_books_map[name]),"
            ]
          },
          // 97 more the same errors...
        ],
        "total": 98
      },
      "POST": {
        "errors": [
          {
            "ts": "2019-06-20T12:51:05.034336Z",
            "trace_id": "b890847f9555c0edc6a252a37fbd901d",
            "last_lines": [
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'extra log': '', 'unique id': '88c408f8-5f7f-433a-b8fb-71239fb09fff', 'headers': {...}, 'request time': 0.007979869842529297, 'user': u'author@books.org'}",,
              "2019-06-20 12:51:07,308 access_logger INFO Tastypie return response (1f9a7e0c-dbb2-46f9-80bd-4d56e8e3c076)",
              "KeyError: u'authoR'",
              "    lambda name: compose_libraries(name, archive_map[name], fresh_books_map[name]),"
            ]
          },
        ],
        "total": 1,
      },
      "total": 1
    },
    "/api/v1/authors/": {
      "POST": {
        "errors": [
          {
            "ts": "2019-06-20T12:51:18.241439Z",
            "trace_id": "a7c4209aec1e096ad0526dafaf87c015",
            "last_lines": [
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'extra log': '', 'unique id': '88c408f8-5f7f-433a-b8fb-71239fb09fff', 'headers': {...}, 'request time': 0.007979869842529297, 'user': u'author@books.org'}",
              "2019-06-20 12:51:20,444 access_logger INFO Tastypie return response (3ff5c472-38b6-41e9-89e0-e43ab9227556)",
              "ValidationError: Author already exists.",
            ]
          },
        ],
        "total": 1,
      },
      "total": 1
    }
  },
  "total": 100
}
```