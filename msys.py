ARCHIVE = '.tar.xz'
ARCHITECTURE = 'x86_64'
CATALOG = '.files'
CHARSET = 'u8'
REPOSITORY = 'https://repo.msys2.org'
SIGNATURE = '.sig'
SUBSYSTEM = 'msys'

ARCHITECTURES = [ARCHITECTURE, 'i686']
ARCHITECTURES_SUBSYSTEMS = {
    ARCHITECTURE: [SUBSYSTEM, 'clang64', 'mingw64', 'ucrt64'],
    'i686': [SUBSYSTEM, 'clang32', 'mingw32'],
}
SUBSYSTEMS = [SUBSYSTEM, 'clang', 'mingw', 'ucrt']
