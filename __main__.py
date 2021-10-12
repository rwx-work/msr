#! /usr/bin/env python3

import hashlib
import os
import sys

import arguments
import local
import synchronization


def build():
    pass


def check():
    packages = []
    broken = []
    lo = local.Local()
    for architecture in lo.architectures:
        for subsystem in architecture.subsystems.values():
            for package in subsystem.catalog.packages.values():
                packages.append((subsystem, package))
    for index, items in enumerate(packages):
        print('\r', index, '/', len(packages), '←', 'checked', end='')
        subsystem, package = items
        path = os.path.join(subsystem.path, package.filename)
        with open(path, 'br') as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            if hash != package.sha256sum:
                broken.append(package)
    print()
    print('', str(len(broken)).rjust(len(str(len(packages)))),
          '/', len(packages), '←', 'broken')


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
