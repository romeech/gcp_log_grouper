# gcp_log_grouper
A script to group log records dumped from **Google Cloud Logging by GCP > Logging > Download logs** (JSON).
Convert flat collection of JSON-objects representing log records into 2-level dictionary: Resource-Method-Errors.

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
      "method": "GET",
      "resource": "/api/v1/books/?limit=10&offset=0&status__in=published%2Cissued",
      "status": 500,
      "line": [
        {
          "time": "2019-06-20T09:53:27.453428Z",
          "severity": "ERROR",
          "logMessage": "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'user': u'author@books.org'}",
        },
        ...
      ],
      "traceId": "a7c4209aec1e096ad0526dafaf87c015",
    }
    ...
  },
  // yet another 100 of log records
]
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
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'user': u'author@books.org'}",
              "KeyError: u'authoR'",
              "    lambda name: compose_libraries(name, archive_map[name], fresh_books_map[name]),"
            ]
          },
          // 98 more the same errors...
        ],
        "total": 99
      },
      "POST": {
        "errors": [
          {
            "ts": "2019-06-20T12:51:05.034336Z",
            "trace_id": "b890847f9555c0edc6a252a37fbd901d",
            "last_lines": [
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'user': u'author@books.org'}",
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
            "trace_id": "e01fb8a6080e44ffa8282311c0d55465",
            "last_lines": [
              "2019-06-20 12:51:20,447 access_logger INFO {'body': '', 'user': u'author@books.org'}",
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


The script can also join several log dumps into one (if you need to analyse logs for several periods):
```
python group_gcp_logs.py --join file1.json file2.json file3.json
```
and process the file with joined records.
