#! /usr/bin/env python3

import sys

import arguments
import remote
import repository


def build(repository, arguments):
    print('Build:')
    # TODO identify
    print('TODO identify')
    # TODO extract
    print('TODO extract')
    # TODO apply
    print('TODO apply')
    # TODO archive
    print('TODO archive')


def check(repository, arguments):
    print('Check:')
    # TODO prepare threads
    print('TODO prepare threads')
    # TODO run threads
    print('TODO run threads')
    # TODO watch threads
    print('TODO watch threads')


def info(repository, arguments):
    print(repository)


def sync(repository, args):
    print('Sync:')
    r = remote.Remote(args)
    print(r)
    for architecture in args[arguments.ARCHITECTURES]:
        print(r.fetch_latest_distribution(architecture))
    # TODO prepare temporary directory
    print('prepare…')
    # TODO fetch
    print('fetch…')
    # TODO purge useless files
    print('purge…')
    # TODO clean temporary directory
    print('clean…')


def main():
    args = arguments.parse()
    repo = repository.Repository(args)
    func = getattr(sys.modules[__name__], args[arguments.ACTION])
    func(repo, args)


if __name__ == '__main__':
    main()
