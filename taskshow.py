#!/usr/bin/env python

import argparse
import Config
import Tasks






if __name__ == '__main__':

    config = Config.Config()

    parser = argparse.ArgumentParser(description='TaskShow')

    # standard flag
    parser.add_argument('--verbose', action='store_true',
        help='verbose flag' )

    taskd_g = parser.add_argument_group(title='Taskd Options')
    taskd_g.add_argument('--ca', type=str, default='',
        help='Taskd server CA certificate')
    taskd_g.add_argument('--cert', type=str, default='',
        help='Client certificate')
    taskd_g.add_argument('--key', type=str, default='',
        help='Client key')
    taskd_g.add_argument('--server', type=str, default='',
        help='Taskd server hostname')
    taskd_g.add_argument('--port', type=int, default=443,
        help='Taskd port number')
    taskd_g.add_argument('--uuid', type=str, default='',
        help='User UUID for Taskd server')
    taskd_g.add_argument('--group', type=str, default='FreeCinc',
        help='Group name for Taskd server (default: FreeCinc)')
    taskd_g.add_argument('--user', type=str, default='',
        help='User name for Taskd server')
    taskd_g.add_argument('--taskrc', type=str, default='',
        help='Taskrc file to read settings from')


    test_g = parser.add_argument_group(title='Testing Options')
    test_g.add_argument('--test', action='store_true',
        help='Execute Python unittests')

    
    # positional argument
    # parser.add_argument("echo")

    args = parser.parse_args()

    # preload the config object
    if args.ca:
        config.ca = args.ca
    if args.cert:
        config.cert = args.cert
    if args.key:
        config.key = args.key
    if args.server:
        config.server = args.server
    if args.port:
        config.port = args.port
    if args.group:
        config.group = args.group
    if args.user:
        config.user = args.user
    if args.uuid:
        config.uuid = args.uuid


    config.write_taskrc()


