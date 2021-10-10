ARCHIVE = '.tar.xz'
ARCHITECTURES = ['x86_64', 'i686']
ARCHITECTURES_BITS = {
    'x86_64': 64,
    'i686': 32,
}
ARCHITECTURES_SUBSYSTEMS = {
    'x86_64': ['msys', 'clang64', 'mingw64', 'ucrt64'],
    'i686': ['msys', 'clang32', 'mingw32'],
}
CATALOG = '.files'
CHARSET = 'u8'
DISTRIBUTION = 'distrib'
SIGNATURE = '.sig'
SUBSYSTEM = 'msys'
SUBSYSTEMS = [SUBSYSTEM, 'clang', 'mingw', 'ucrt']
