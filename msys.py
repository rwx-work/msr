ARCHIVE = '.tar.xz'
ARCHITECTURES = ['x86_64', 'i686']
ARCHITECTURES_BITS = {
    'x86_64': 64,
    'i686': 32,
}
CATALOG = '.files'
CHARSET = 'u8'
CRT = 'mingw'
DISTRIBUTION = 'distrib'
SIGNATURE = '.sig'
SUBSYSTEM = 'msys'

ARCHITECTURES_SUBSYSTEMS = {
    'x86_64': [SUBSYSTEM, 'clang64', 'mingw64', 'ucrt64'],
    'i686': [SUBSYSTEM, 'clang32', 'mingw32'],
}
SUBSYSTEMS = [SUBSYSTEM, 'clang', 'mingw', 'ucrt']


def get_subsystems(architecture, families):
    list = []
    bits = ARCHITECTURES_BITS[architecture]
    for family in families:
        if family == SUBSYSTEM:
            subsystem = family
        else:
            subsystem = f'{family}{bits}'
        if subsystem in ARCHITECTURES_SUBSYSTEMS[architecture]:
            list.append(subsystem)
    return list
