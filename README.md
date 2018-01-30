system-n
========

Master repository for all things [KEA](https://kea.ai)

Description
-----------

KEA is a telecommunications platform that merchants use to take orders and requests automatically when customers call in.

Notes
-----

Structure
---------

```
system-n/
  |   README.md
  |   (you are here)
  |
  └── components/
  |   (contains individual components that make up the entire KEA stack)
  |   |
  |   └── sample/
  |   |   |
  |   |   └── README.md
  |   |   └── docs/
  |   |   └── test               # Standalone executable to test component
  |   |   └── build              # Standalone executable to build component
  |   |   └── lint               # Standalone executable to lint component
  |   |   └── deploy             # Standalone executable to deploy component
  |   |   |
  |   |   └── **/* ...
  |   |       (Application code)
  |   |
  |   └── componentA/ ...
  |
  └── deploy/
  |   (contains build / deploy scripts for getting stack up and running)
  |   |
  |   └── README.md
  |   |
  |   └── config/
  |   |   |
  |   |   └── **/*.(yml|json|xml)   # Config files
  |   |
  |   └── sample.wscript
  |   └── main.wscript
  |   |   (Build scripts using waf)
  |   |
  |   └── **/*.wscript ...
  |
  └── docs/
  |   (contains general purpose documentation referencing docs recursively in all submodules)
  |   |
  |   └── README.md
  |   └── **/*.md
  |
  └── tools/
  |   (contains tools needed for common tasks)
  |   |
  |   └── README.md
  |   |
  |   └── build/
  |   └── init/
  |   └── install/
  |   └── misc/
  |   └── run/
  |
  └── libraries/
  └── metadata/
  └── static/
  └── test/
```
