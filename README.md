system-n
========

Master repository for all things [KEA](https://kea.ai)

Description
-----------

KEA is a telecommunications platform that merchants use to take orders and requests automatically when customers call in.

Links
-----

 - [Intranet](https://extra.kea.ai)
 - [Github projects page](https://github.com/orgs/keacloud/projects/)
 - [Issues page](https://github.com/keacloud/system-n/issues)

Schematic
---------

![System-N Schematic | How it works](https://github.com/keacloud/system-n/blob/master/diagram.svg)

<!-- Created using https://bramp.github.io/js-sequence-diagrams/ with source:

Title: System-N

participant customer
participant twilio
participant postgres
participant aiml
participant wallaroo
participant simba
participant call center
participant restaurant

Note right of twilio: ────────\nKEA App\nBoundary\n────────

customer->twilio: Calls store\n phone number
Note right of customer: Redirected\nto twilio #

Note over postgres: Primary API\n(PostgREST)
twilio->postgres: Make request\nto application

Note over aiml: Dialogue\nEngine
postgres->aiml: Generate\nresponse

aiml->twilio: TwiML response
twilio->customer:Handle call
customer->twilio:

Note over wallaroo: Task\nPipeline
postgres->wallaroo: Trigger entity\nrecognition

Note over simba: TaskRouter
wallaroo->simba: Create order task

Note over call center: Call center\nTeam
simba->call center: Assign task\nto correct worker\nfor verification

call center->postgres: Order status
postgres->wallaroo: Order status
wallaroo->restaurant: Send order to POS system
wallaroo->customer: Send confirmation and receipt

Note left of restaurant: ────────\nKEA App\nBoundary\n────────
-->

Process
-------

 - All code begins life as part of a component.
 - Once tested and deployed, refactor aggressively.
 - Recursively, move generalizable components to libraries.
 - Open source libraries once sufficient documentation is added.
 - Let the world maintain it for ya.

Branches
--------

 - `staging`: [default] Base branch for fix/feature branch. Only merges allowed after CI passes.
 - `master`: The untouchable branch. Only _automatic_ merges allowed after CI passes.
 - `develop`: **Special** Orphan branch. All experimental stuff base on this. Be aware that merging into _staging_ is non-trivial.

 **Notes**

 - Naming convention:
     * Bugfix branches -> `fix/<short_descriptive_name>`
     * Feature branches -> `feature/<short_descriptive_name>`
     * Patch branches -> `patch/<short_descriptive_name>`
     * Experimental branches -> `experiment/<short_descriptive_name>`

 - Branch bases and merge points:
     * Bugfix branches -> `staging` or `master`.
     * Feature branches -> `staging` only.
     * Patch branches -> any branch except `staging`, `master` or `develop`.
     * Experimental branches -> `develop` only.

 **Flow**

 - Bug fixes:
     1. Create branch of `staging` or `master`.
     2. Add code, lint, make tests pass etc.
     3. Make sure branch is updated and can be safely merged back.
     4. Rebase into one commit, if possible.
     5. Create pull request on original branch.
     6. Merge and delete fix branch.

 - New featues:
     1. Same as for bug fixes except only on `staging`.
     2. See above.

 - Experiments:
     1. Before beginning an experiment, find last history intersection of `develop` and `staging`.
     2. Base an experiment branch off of that intersection commit.
     3. Remaining steps same as for features except only on `develop`. See above.

Directory Structure
-------------------

 - Logically separate projects are referenced as [git-submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
 - Use [git-hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) amply to maintain sanity checks.
 - Entire directory is a **\<Component\>** composed of mainly:
     * Any application code.
     * 0 or more `components`, which are basically nested **\<Component\>** s.
     * 0 or more `libraries`, each structured as **\<Library\>**.
     * Required `README.md` and (optional) `docs/` folder.
     * Required `tests` directory containing any tests.
     * Required `tools` directory structured as **\<Tools\>**.
     * Optional `metadata` and `static` directories which are free-form.

 - A **\<Library\>** has:
     * Any library code.
     * Required `README.md` and (optional) `docs/` folder.
     * Required `publish` **\<Script\>**

 - **\<Tools\>** have:
     * Optional `README.md`.
     * Optional `config` directory, containing configuration files.
     * These scripts:
        + Optional `init` **\<Script\>**.
        + Optional `build` **\<Script\>**.
        + Optional `lint` **\<Script\>**.
        + Optional `deploy` **\<Script\>**.
        + Required `test` **\<Script\>**.

     * Any other relevant code.

 - **\<Script\>** is:
     * Either a standalone `sh` executable.
     * Or a directory with a `main*` preferably `main.wscript` file.
     * Any other relevant code.

```
system-n/
  |   README.md
  |   (you are here)
  |
  └── docs/
  |   (contains general purpose documentation referencing docs recursively in all submodules)
  |   |
  |   └── README.md
  |   └── **/*.md
  |
  └── **/* ...
  |   (Application code)
  |
  └── components/
  |   (contains individual components that make up the entire KEA stack)
  |   |
  |   └── sample-subcomponent/
  |   |   |
  |   |   └── README.md
  |   |   └── { ... }
  |   |   |
  |   |   └── **/* ...
  |   |       (Application code)
  |   |
  |   └── other-component/ ...
  |
  └── tools/
  |   (contains lint / build / deploy scripts for getting up and running)
  |   |
  |   └── README.md
  |   |
  |   └── config/
  |   |   |
  |   |   └── **/*.(yml|json|xml)   # Config files
  |   |
  |   └── build/
  |   └── init/
  |   └── lint/
  |   └── deploy/
  |   └── test/
  |   └── sample/
  |       |
  |       └── main.wscript
  |       |   (Build scripts using waf)
  |       |
  |       └── **/*.wscript ...
  |
  └── libraries/
  └── metadata/
  └── static/
  └── test/
```

Notes
-----

> Why is a raven like a writing desk? ~ _Alice in Wonderland_

> Because it can produce a few notes, tho they are very flat; and it is never put with the wrong end in front!
