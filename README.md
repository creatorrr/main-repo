system-n
========

Master repository for all things [KEA](https://kea.ai)

Description
-----------

KEA is a telecommunications platform that merchants use to take orders and requests automatically when customers call in.

Process
-------

 - All code begins life as part of a component.
 - Once tested and deployed, refactor aggressively.
 - Recursively, move generalizable components to libraries.
 - Open source libraries once sufficient documentation is added.
 - Let the world maintain it for ya.

Branches
--------

 - `master`: The untouchable branch. Only merges allowed after CI passes.
 - `staging`: Base branch for fix/feature branch. Only merges allowed after CI passes.
 - `develop`: **Special** Orphan branch. All experimental stuff base on this. Be aware that merging into _staging_ is non-trivial.

Notes
-----

Structure
---------

 - Logically separate projects are referenced as [git-submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
 - Use [git-hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) amply to maintain sanity checks.

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
