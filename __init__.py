#! /usr/bin/env python3

import sys

import arguments
import local
import synchronization


def build():
    # TODO identify
    print('TODO identify')
    # TODO extract
    print('TODO extract')
    # TODO apply
    print('TODO apply')
    # TODO archive
    print('TODO archive')


def check():
    # TODO prepare threads
    print('TODO prepare threads')
    # TODO run threads
    print('TODO run threads')
    # TODO watch threads
    print('TODO watch threads')


def info():
    print(local.Local())


def sync():
    sync = synchronization.Synchronization()
    print(sync)
    sync.run()


def main():
    getattr(sys.modules[__name__], arguments.action)()


if __name__ == '__main__':
    main()
