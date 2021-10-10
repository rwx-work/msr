import os

ARCHIVE = '.tar.xz'
ARCHITECTURE = 'x86_64'
CATALOG = '.files'
CHARSET = 'u8'
DISTRIBUTION = 'distrib'
REPOSITORY = 'https://repo.msys2.org'
SIGNATURE = '.sig'
SUBSYSTEM = 'msys'

ARCHITECTURES = [ARCHITECTURE, 'i686']
ARCHITECTURES_BITS = {
    ARCHITECTURE: 64,
    'i686': 32,
}
ARCHITECTURES_SUBSYSTEMS = {
    ARCHITECTURE: [SUBSYSTEM, 'clang64', 'mingw64', 'ucrt64'],
    'i686': [SUBSYSTEM, 'clang32', 'mingw32'],
}
SUBSYSTEMS = [SUBSYSTEM, 'clang', 'mingw', 'ucrt']


def get_distribution(architecture):
    return os.path.join(DISTRIBUTION, architecture.name)


def get_subsystems(architecture, families):
    list = []
    for family in families:
        if family == SUBSYSTEM:
            subsystem = family
        else:
            subsystem = f'{family}{architecture.bits}'
        if subsystem in ARCHITECTURES_SUBSYSTEMS[architecture.name]:
            list.append(subsystem)
    return list
