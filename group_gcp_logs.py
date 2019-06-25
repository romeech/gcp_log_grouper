#!/usr/local/bin/python3

import json
import os
import sys


OUTPUT_FILENAME = 'grouped_records.json'
JOINED_FILENAME = 'joined_records.json'


def read_source(source_filename):
    source_log_dump_name = source_filename
    with open(source_log_dump_name, 'r') as log:
        log_obj = json.load(log)

    return log_obj


def dump_obj(obj, filename):
    with open(filename, "w+") as f:
        json.dump(obj=obj, fp=f, indent=2)


def dump_groups(groups_obj):
    dump_obj(groups_obj, OUTPUT_FILENAME)
    print("\t - Dump file: {}".format(os.path.join(os.getcwd(), OUTPUT_FILENAME)))


def dump_joined(joined_records):
    dump_obj(joined_records, JOINED_FILENAME)
    print("\t - File with joined records: {}".format(os.path.join(os.getcwd(), JOINED_FILENAME)))


def prepare_grouped_json(source_filename):
    log_obj = read_source(source_filename)

    groups = {}
    for row in log_obj:
        proto_payload = row.get('protoPayload')

        if proto_payload:
            resource = proto_payload['resource']
            method = proto_payload['method']

            last_lines = proto_payload.get('line', [])[-1:-5:-1]
            row_obj = {
                'ts': row['timestamp'],
                'trace_id': proto_payload['traceId'],
                'last_lines': [col['logMessage'] for col in last_lines],
            }
        else:
            http_request = row['httpRequest']
            resource = http_request['requestUrl']
            method = http_request['requestMethod']

            row_obj = {
                'ts': row['timestamp'],
                'trace_id': row['trace'].split('/')[-1],
                'last_lines': [],
            }

        if resource not in groups:
            groups[resource] = {}

        if not groups[resource].get(method):
            groups[resource][method] = {'errors': []}

        groups[resource][method]['errors'].append(row_obj)

    for resource, method_grps in groups.items():
        total_count = 0
        for method, grp in method_grps.items():
            grp['total'] = len(grp['errors'])
            total_count += len(grp['errors'])

        method_grps['total'] = total_count

    obj = {
        'groups': groups,
        'total': len(log_obj),
    }

    dump_groups(obj)


def join_gae_log_dumps(log_names):
    joined_records = []
    for logname in log_names:
        log_obj = read_source(logname)
        joined_records.extend(log_obj)

    dump_joined(joined_records)


if __name__ == '__main__':
    if sys.argv[1] == '--join':
        join_gae_log_dumps(sys.argv[2:])
        prepare_grouped_json(JOINED_FILENAME)
    else:
        prepare_grouped_json(sys.argv[1])
