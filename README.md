# Minimal System Repository

A tool to handle local/remote msys/mingw repositories.

## Features

* [ ] display information
* [ ] synchronize data
    * [ ] fetch remote catalogs
    * [ ] download packages
        * [ ] single threading
        * [ ] multi threading
    * [ ] generate signatures from catalogs
* [ ] check integrity
    * [ ] catalogs
    * [ ] packages
        * [x] single threading
        * [ ] multi threading
        * [ ] progress bars
* [ ] build archive
    * [ ] get base file system
        * [ ] extract from distribution
        * [ ] bootstrap mintty, msys, pacman
    * [ ] apply configuration
    * [ ] archive directory
* [ ] build dependency graph
    * [ ] generate graphviz diagram
    * [ ] render final image

## Info

* pacman needs .db catalog, but .files seems optional
