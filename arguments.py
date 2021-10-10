import argparse
import os

import msys

ACTION = 'action'
ARCHITECTURES = 'architectures'
COMPRESSION = 'compression'
DIRECTORY = 'directory'
FILESYSTEM = 'filesystem'
REMOTE = 'remote'
SUBSYSTEMS = 'subsystems'
TEMPORARY = 'temporary'
THREADS = 'threads'
VERBOSE = 'verbose'


class Formatter(argparse.RawTextHelpFormatter,
                argparse.ArgumentDefaultsHelpFormatter):
    pass


def parse():
    parser = argparse.ArgumentParser(formatter_class=Formatter)

    parser.add_argument(f'-{VERBOSE[0]}', f'--{VERBOSE}', type=bool, help='''\
verbose output
''')

    parser.add_argument(f'-{DIRECTORY[0]}', f'--{DIRECTORY}', type=str,
                        help='''\
msys repository's directory
''')
    parser.add_argument(f'--{TEMPORARY}', type=str, help='''\
msys repository's temporary directory
''')
    parser.add_argument(f'-{THREADS[0]}', f'--{THREADS}', type=int, help='''\
number of threads to use
''')
    parser.add_argument(f'{ACTION}', type=str, nargs='?',
                        choices=['build', 'check', 'info', 'sync'], help='''\
action to perform onto msys repository
''')

    sync = parser.add_argument_group('sync')
    sync.add_argument(f'-{REMOTE[0]}', f'--{REMOTE}', type=str, help='''\
msys remote repository's location
''')
    sync.add_argument(f'-{ARCHITECTURES[0]}', f'--{ARCHITECTURES}', type=str,
                      nargs='+', choices=msys.ARCHITECTURES, help='''\
list of architectures to sync
''')
    sync.add_argument(f'-{SUBSYSTEMS[0]}', f'--{SUBSYSTEMS}', type=str,
                      nargs='+', choices=msys.SUBSYSTEMS, help='''\
list of subsystems to sync
''')

    build = parser.add_argument_group('build')
    parser.add_argument(f'-{FILESYSTEM[0]}', f'--{FILESYSTEM}', type=str,
                        help='''\
directory containing modifications applying to filesystem
''')
    build.add_argument(f'-{COMPRESSION[0]}', f'--{COMPRESSION}', type=str,
                       choices=['gz', 'xz', 'zst'], help='''\
compression applying to archive
''')

    parser.set_defaults(
        directory=os.curdir,
        temporary='tmp',
        threads=2,

        action='info',

        remote=msys.REPOSITORY,
        architectures=[msys.ARCHITECTURE],
        subsystems=[msys.SUBSYSTEM, 'mingw'],

        filesystem='fs',
        compression='zst',
    )

    return vars(parser.parse_args())

D = parse()

architectures = D[ARCHITECTURES]
