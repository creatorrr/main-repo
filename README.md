keacloud/main-repo
==================

Master repository for all things [kea](https://kea.ai)

Description
-----------

[kea](https://kea.ai) is a telecommunications platform that merchants use to take orders and requests automatically when customers call in.

Links
-----

 - [Github projects page](https://github.com/orgs/keacloud/projects/)
 - [Issues page](https://github.com/keacloud/main-repo/issues)
 - [Pipefy](https://app.pipefy.com/organizations/113878#)

Schematic
---------

![System-N Schematic | How it works](https://github.com/keacloud/main-repo/blob/master/docs/diagram.svg)

<!-- Created using https://bramp.github.io/js-sequence-diagrams/ with source:

Title: System-N

participant customer
participant twilio
participant data_api
participant dialog_manager
participant bg_tasks
participant taskrouter
participant call center
participant restaurant

Note right of twilio: ────────\nkea App\nBoundary\n────────

customer->twilio: Calls store\n phone number
Note right of customer: Redirected\nto twilio #

Note over data_api: Primary API\n(PostgREST)
twilio->data_api: Make request\nto application

Note over dialog_manager: Dialogue\nEngine
data_api->dialog_manager: Generate\nresponse

dialog_manager->twilio: TwiML response
twilio->customer:Handle call
customer->twilio:

Note over bg_tasks: Background\nTasks
data_api->bg_tasks: Trigger entity\nrecognition

Note over taskrouter: Task\nRouter
bg_tasks->taskrouter: Create order task

Note over call center: Call center\nTeam
taskrouter->call center: Assign task\nto correct worker\nfor verification

call center->data_api: Order status
data_api->bg_tasks: Order status
bg_tasks->restaurant: Send order to POS system
bg_tasks->customer: Send confirmation and receipt

Note left of restaurant: ────────\nkea App\nBoundary\n────────
-->

Notes
-----

### Stack

 - [Kubernetes](https://kubernetes.io/) to manage our clusters.
 - [Aiven](https://aiven.io) for all of our managed databases.
 - [PostgreSQL](https://postgresql.org) as our primary source of truth.

### Kubernetes base stack

![Base stack](https://github.com/keacloud/main-repo/blob/master/docs/base-k8s-stack.png)

### Kubernetes extensions

 - [kubewatch](https://github.com/kubernetes/charts/blob/master/stable/kubewatch)
 - [eventrouter](https://github.com/heptiolabs/eventrouter)
 - [kubeless](http://kubeless.io)
 - [kubedb-memcached](https://github.com/kubedb/memcached)
 - [helm](https://github.com/heptio/contour/)
 - [gitkube](https://github.com/hasura/gitkube)
 - [argo](https://github.com/argoproj/argo)
 - [contour](https://github.com/heptio/contour/)
 - [vault](https://www.vaultproject.io/docs/)
 - [kubernetes-vault](https://github.com/Boostport/kubernetes-vault/)
 - [weave-cloud](https://cloud.weave.works)
 - [metabase](https://github.com/kubernetes/charts/blob/master/stable/metabase/)
 - [cert-manager](https://cert-manager.readthedocs.io/)
 - [kapacitor](https://github.com/kubernetes/charts/blob/master/stable/kapacitor/)
 - [influxdb](https://github.com/kubernetes/charts/blob/master/stable/influxdb/)

### Kubernetes static tools

 - [psykube](https://github.com/psykube/psykube)
 - [kompose](https://github.com/kubernetes/kompose)
 - [kubeval](https://github.com/garethr/kubeval)
 - [kubesec](https://kubesec.io)
 - [telepresence](https://www.telepresence.io/tutorials/docker)

Environments
------------

 - Identical kubernetes environments for `production` and `staging`.
 - `master` branch -> `production`
 - `staging` branch -> `staging`
 - Different subdomains, `k1.kea.cloud` and `k2.kea.cloud`.
 - Different deployment strategies.

### Component deployment (staging)

 - Add a `Dockerfile` that runs the component.
 - Build and test `docker` image locally.
 - Add the `gitkube` git remote.
 - Push code to the remote, `gitkube` builds images and updates components!

### Component deployment (production)

 - Add a `Dockerfile` that runs the component.
 - Build and test `docker` image locally.
 - Push code to gihub `master` branch, Google Container registry automatically picks up changes and builds the image.
 - `Weave Cloud` checks the registry and updates components automatically.

Process
-------

 - All code begins life as part of a component.
 - Once tested and deployed, refactor aggressively.
 - Recursively, move generalizable components to libraries.
 - Open source libraries once sufficient documentation is added.
 - Let the world maintain it for ya.
 - Stand on the shoulders of giants, use [kubernetes](https://kubernetes.io/) and friends for managed CI/CD.

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
     6. Make sure all CI tests pass.
     7. Merge and delete fix branch.

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
     * Required `README.md` and (optional) `docs/` folder.
     * Required `tests` directory containing any tests.
     * Optional `deply` directory that contains kubernetes stack `yaml` files.
     * Optional `scripts` directory structured as **\<Scripts\>**.
     * Optional `metadata` directories which are free-form.

 - **\<Scripts\>** have:
     * Any scripts.
     * Optional `config` directory, containing configuration files.
     * Optional `init` script
     * Optional `build` script
     * Optional `lint` script
     * Optional `deploy` script

```
main-repo/
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
  |   (contains individual components that make up the entire kea stack)
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
  └── deploy/
  |   (contains yaml kubernetes scripts for getting up and running)
  |   |
  |   └── *.yaml
  |   |
  |   └── helm-charts/
  |   |   |
  |   |   └── **/*.yaml
  |
  └── scripts/
  |   (contains lint / build / deploy scripts for getting up and running)
  |   |
  |   └── README.md
  |   |
  |   └── config/
  |   |   |
  |   |   └── **/*.(yml|json|xml)   # Config files
  |   |
  |   └── build
  |   └── init
  |   └── lint
  |   └── deploy
  |
  └── metadata/
  └── tests/
```

Misc
----

> Why is a raven like a writing desk? ~ _Alice in Wonderland_

> Because it can produce a few notes, tho they are very flat; and it is never put with the wrong end in front!
