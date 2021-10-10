#! /usr/bin/env python3

import sys

import arguments
import local
import synchronization


def build(args):
    # TODO identify
    print('TODO identify')
    # TODO extract
    print('TODO extract')
    # TODO apply
    print('TODO apply')
    # TODO archive
    print('TODO archive')


def check(args):
    # TODO prepare threads
    print('TODO prepare threads')
    # TODO run threads
    print('TODO run threads')
    # TODO watch threads
    print('TODO watch threads')


def info(args):
    print(local.Local(args))


def sync(args):
    sync = synchronization.Synchronization(args)
    print(sync)
    sync.run()


def main():
    args = arguments.parse()
    function = getattr(sys.modules[__name__], args[arguments.ACTION])
    function(args)


if __name__ == '__main__':
    main()
