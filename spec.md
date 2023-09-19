# BIDS Applications

## version 0.0.1

## Available under the CC-BY 4.0 International license.

Extension moderators/leads:

Christopher J Markiewicz
&lt;[markiewicz@stanford.edu](mailto:markiewicz@stanford.edu)>, Gregory Kiar
&lt;[gregory.kiar@childmind.org](mailto:gregory.kiar@childmind.org)>

Contributors:

Tristan Glatard
&lt;[tristan.glatard@concordia.ca](mailto:tristan.glatard@concordia.ca)>, Pierre
Rioux &lt;[pierre.rioux@mcgill.ca](mailto:pierre.rioux@mcgill.ca)>, Yaroslav O.
Halchenko &lt;[yoh@dartmouth.edu](mailto:yoh@dartmouth.edu)> Eric Earl
&lt;[eric.earl@nih.gov](mailto:eric.earl@nih.gov)>, Pradeep Reddy Raamana
&lt;raamanap@pitt.edu>, Aki Nikolaidis
&lt;[aki.nikolaidis@childmind.org](mailto:aki.nikolaidis@childmind.org)>,
Guiomar Niso &lt;[guiomar.niso@ctb.upm.es](mailto:guiomar.niso@ctb.upm.es)>,
Lennart Walger &lt;[lennart.walger@ukbonn.de](mailto:lennart.walger@ukbonn.de)>,
Sebastien Tourbier
&lt;[sebastien.tourbier1@gmail.com](mailto:sebastien.tourbier1@gmail.com)>,
Alejandro de la Vega &lt;[delavega@utexas.edu](mailto:delavega@utexas.edu)>,
Robert Luke &lt;robert.luke@mq.edu.au>

The Problem: Neuroimaging is a field with an enormous library of powerful tools
and openly available datasets that can be difficult to get to work together.

What is BIDS? The Brain Imaging Data Structure (BIDS) is a community-driven
standardized data organization protocol that gives analysis tools a common
specification for data input, see this link. BIDS solves the dataset complexity
problem by providing a consistent representation for data sharing and adoption.

So why do we need the BIDS Application Specification? While BIDS is great for
standardizing datasets, analytical tools can take a variety of forms, arguments,
and complexities, limiting their ability to be applied interchangeably. The BIDS
Application Specification solves this problem by creating a community-driven
standardized structure for software definitions and their execution.

What is this document? This document is a draft for the BIDS Application
specification for the purposes of tool description, provenance and
reproducibility. This is a working document in draft stage and any comments are
welcome. This document inherits all components of the original specification
(e.g. how to store imaging data, events, stimuli and behavioral data), and
should be seen as an extension of it, not a replacement.

How can I help? There are many open comments on the document, and all of them
would benefit from your input. As you read this document, please feel free to
ask questions, complete remaining tasks, or reach out to any of the listed
contributors and moderators.

## Scope of BIDS Applications

While the BIDS format is great for standardizing datasets, analytical tools
operating on that structure can take a variety of forms, arguments, and
complexities, limiting their ability to be applied interchangeably. The BIDS
Application Specification solves this problem by creating a community-driven
standardized structure for software definitions and their execution.

This specification extends the Brain Imaging Data Structure (BIDS) Specification
to describe how software pipelines and analytic tools should interact with
BIDS-formatted datasets. These tools will be referred to as "BIDS Apps" or "BIDS
Applications", and can accept any valid BIDS dataset prior to producing some
result (including a message of inaction, as may be applicable in some cases).

### Goals of BIDS Applications

This extension is motivated by a desire to automatically and reproducibly
process neuroscientific data. It seeks to specify file types and metadata for
describing the execution of command-line programs that operate upon BIDS
datasets. Graphical and web-based interfaces are outside the scope of this
extension, though it is expected that this specification will simplify the
integration of BIDS datasets and applications into such platforms.

This is guided by the following requirements and desiderata:

- A tool's parameters should be easily translatable to the BIDS application
  input specification.
- A specification should be maximally descriptive rather than prescriptive.
- A structured execution specification should be produced as a result of using
  an application.
- The specification should be sufficiently descriptive to perfectly reproduce
  analyses.
- A structured set of input parameters should be usable in place of command-line
  arguments.
- It should be possible to make multiple BIDS datasets available to an
  application.

### Relation of BIDS Applications to BIDS

The core principles of the original BIDS-Raw specification are inherited by the
BIDS Application specification. This specification is a successor to BIDS-Apps,
which were described in Gorgolewski, et al. 2017
(doi:[10.1371/journal.pcbi.1005209](https://doi.org/10.1371/journal.pcbi.1005209)),
here referred to as BIDS-Apps 1.0. Backwards compatibility with BIDS-Apps 1.0 is
not an explicit goal, but can be achieved in many cases as is discussed in
Section [3.1.2.1](#3-1-2-1-backwards-compatibility-9). A summary of changes from
BIDS-Apps 1.0 is included as
[Appendix A](#a-summary-of-changes-from-bids-apps-1-0-17).

This specification is seen as complementary to BIDS-Derivatives, which is part
of BIDS as of version 1.4.0, and the most recent stable version may be found at
[https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html).
It is not required that every BIDS Application produce a
BIDS-Derivatives-compliant result dataset, but any outputs that may be required
by the BIDS Application specification must be compliant with the
BIDS-Derivatives specification.

Please refer to general BIDS specification document for context and general
guidelines (definitions, units, directory structure, missing values, stimulus
and event information, etc.):
[https://bids-specification.readthedocs.io/en/stable/](https://bids-specification.readthedocs.io/en/stable/)

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [[RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

The terminology that will be used is inherited from BIDS-Raw and includes the
following:

- **Dataset** — a set of neuroimaging and behavioral data acquired for a purpose
  of a particular study. A dataset consists of data acquired from one or more
  subjects and/or sessions.
- **Subject** — a person or animal participating in the study. Interchangeable
  with "**Participant**".
- **Session** — a consistent logical grouping of neuroimaging and other data
  across subjects.
- **Run** — an uninterrupted repetition of data acquisition that has the same
  acquisition parameters and task (however events can change from run to run due
  to different subject response or randomized nature of the stimuli).
- **&lt;index>** - a nonnegative integer, possibly prefixed with arbitrary
  number of 0s for consistent indentation, for example, it is 01 in run-01
  following run-&lt;index> specification.
- **&lt;label>** - an alphanumeric value, possibly prefixed with arbitrary
  number of 0s for consistent indentation, for example, it is rest in task-rest
  following task-&lt;label> specification.

## BIDS Application Specification

There are three domains of requirements that BIDS Applications must specify: (1)
User interface components; (2) Required application behaviors; (3) Required
application outputs.

BIDS contains "required", "recommended" and "optional" fields. These are
indicated throughout the document:

- **REQUIRED**: essential to be BIDS compliant (i.e. MUST as per RFC2199)
- **RECOMMENDED**: gives a warning if not present (i.e. SHOULD as per RFC2199)
- **OPTIONAL**: no warning if missing (i.e. MAY as per RFC2199)

Ultimately, through using Boutiques to define tools and their parameters, the
goal is that each tool can be interacted with as follows:

```
    $ # Using Boutiques directly, the "exec launch" commands will run the app
    $ bosh exec launch bids-app --invocation input_params.json
    $ # Eventually, we envision that BIDS Application interface will also support
    $ # simple, lightweight overrides to provide some of these common values via
    $ # the command line directly.
    $ bids-launch bids-app --input-dataset /path/to/bids /path/to/derivatives \
        --output-location /path/to/output \
        --analysis-level subject--subject-label 01 02 \
        --random-seed 0xBID5CAFE
```

In the next sections, the `bids-app` tool, a Boutiques descriptor, and the
`input_params.json`, a set of invocation parameters corresponding to this app,
will be defined.

### User interface

A uniform user interface is essential to scalable deployment of BIDS
Applications. This section describes the common interface components that may be
relied upon by users or platforms running these applications (callers).
Command-line interfaces map between positional or flag arguments provided
through an interactive shell program (e.g. Bash) to a program and program
behavior. However, tools written in different languages or following different
conventions may represent and parse these arguments distinctly. For the purposes
of automated execution of diverse tools, a more useful interface is a mapping of
parameter identifiers to their values, abstracting the way they are represented
on the command-line (CLI). Boutiques is a standard developed for this mapping.
[Boutiques](https://github.com/boutiques/boutiques) provides a
[JSON schema](https://github.com/boutiques/boutiques/tree/master/schema) and
related tools to describe, validate, execute and share command-line tools, among
other utilities. The Boutiques toolkit, named bosh, will be referred to when
discussing examples throughout this specification.

Instead of requiring specific positional arguments and flags which assign common
names to expected options (e.g., "subject-label") in the command-line interfaces
themselves, BIDS Applications should provide a Boutiques descriptor — a
standardized JSON file that describes the command line behavior and operation of
a tool — that map the tool-specific common arguments to these common names,
without requiring rewriting of the command-line tools. In the sections below,
the identifiers assigned in the Boutiques descriptor are described in the
"Argument ID" column of relevant tables.

The Boutiques descriptor for a program SHOULD be retrievable by calling the
application with the `--bids-exec-spec` flag and no other arguments.

#### Interface descriptor

A human-readable schema for a Boutiques descriptor may be found at
[https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md](https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md).
This section attempts to summarize the salient points of that document, but the
Boutiques schema is authoritative and complete. In addition to the Boutiques
fields (see Tables 1–4, 6), BIDS conformant descriptors MUST include a custom
object (see Table 2) containing the BIDSApplicationVersion key and associated
value which indicates the version of the BIDS application specification to which
they conform, together with some additional optional fields. Descriptors SHOULD
be simply named as name.json.

<table>
  <tr>
   <td colspan="2" ><strong>Table 1: </strong>List of relevant base Boutiques properties and their role within BIDS Applications.
   </td>
  </tr>
  <tr>
   <td><strong>Field name</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>command-line</code></strong>
   </td>
   <td>REQUIRED. String. A template string including the command and references to the value-keys of all possible inputs. The ordering imposed here may be significant, in particular for non-optional arguments.
   </td>
  </tr>
  <tr>
   <td><strong><code>custom</code></strong>
   </td>
   <td>REQUIRED. Object. Object which can contain extensible metadata. This has a single required element, as described in Table 2.
   </td>
  </tr>
  <tr>
   <td><strong><code>inputs</code></strong>
   </td>
   <td>REQUIRED. List. List of objects which contain input parameter definitions. Described in Table 3.
   </td>
  </tr>
  <tr>
   <td><strong><code>name</code></strong>
   </td>
   <td>REQUIRED. String.  The name of the BIDS Application.
   </td>
  </tr>
  <tr>
   <td><strong><code>output-files</code></strong>
   </td>
   <td>REQUIRED. List. List of objects which contain output parameter definitions. Described in Table 6.
   </td>
  </tr>
  <tr>
   <td><strong><code>schema-version</code></strong>
   </td>
   <td>REQUIRED. String. Boutiques schema version. Must be "≥0.5". This is not to be confused with the BIDS Application schema and associated version.
   </td>
  </tr>
  <tr>
   <td><strong><code>tool-version</code></strong>
   </td>
   <td>REQUIRED. String. Version of the BIDS Application.
   </td>
  </tr>
  <tr>
   <td><strong><code>description</code></strong>
   </td>
   <td>RECOMMENDED. String. A plain-text description of the BIDS Application.
   </td>
  </tr>
  <tr>
   <td><strong><code>descriptor-url</code></strong>
   </td>
   <td>RECOMMENDED. String. Link to the descriptor itself. Likely a GitHub repo alongside the described tool, for example.
   </td>
  </tr>
  <tr>
   <td><strong><code>doi</code></strong>
   </td>
   <td>RECOMMENDED. String. DOI of the descriptor returned once published via Boutiques. (Note: This is not the DOI of the tool itself.)
   </td>
  </tr>
  <tr>
   <td><strong><code>suggested-resources</code></strong>
   </td>
   <td>RECOMMENDED. Object. Contains an execution walltime-estimate in seconds, memory usage in MB, and CPU/GPU usage in number of core threads/devices.
   </td>
  </tr>
  <tr>
   <td><strong><code>container-image</code></strong>
   </td>
   <td>OPTIONAL. Object. The name and location of a container image, such as those in Docker or Singularity formats, containing the configured application.
   </td>
  </tr>
  <tr>
   <td><strong><code>error-codes</code></strong>
   </td>
   <td>OPTIONAL. List. List of objects that contain error code information. The reserved error conditions are described in Table 7.
   </td>
  </tr>
  <tr>
   <td><strong><code>groups</code></strong>
   </td>
   <td>OPTIONAL. List. List of objects that contain relational information among input parameters as described in Table 4. This is not to be confused with any other BIDS-relevant definition of groups.
   </td>
  </tr>
</table>

The `custom` object has the following defined fields for use in the context of
BIDS Applications:

<table>
  <tr>
   <td colspan="2" ><strong>Table 2: </strong>List of custom object properties and roles within the BIDS Application specification.
   </td>
  </tr>
  <tr>
   <td><strong>Field name</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>BIDSAppSpecVersion</code></strong>
   </td>
   <td>REQUIRED. String. The version of the BIDS application specification with which the application complies.
   </td>
  </tr>
  <tr>
   <td><strong><code>OutputDataSpecification</code></strong>
   </td>
   <td>OPTIONAL. List. If output data conforms to a standard definition (e.g. NIDM-1.1.0), these data standards may be included as a list of strings.
   </td>
  </tr>
  <tr>
   <td><strong><code>&lt;unspecified></code></strong>
   </td>
   <td>OPTIONAL. Any. Any key referring to arbitrary metadata that may be relevant or of interest to the application and its users.
   </td>
  </tr>
</table>

### Input specification

Inputs to BIDS apps may be specified as JSON objects that map input ids to
values. The objects found within the required inputs list have the following
fields, described fully in
[https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md#inputs](https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md#inputs)
([source](https://github.com/boutiques/boutiques/blob/0.5.25/tools/python/boutiques/schema/descriptor.schema.json#L247-L448)):

<table>
  <tr>
   <td colspan="2" ><strong>Table 3: </strong>List of relevant inputs object properties for the BIDS Application specification.
   </td>
  </tr>
  <tr>
   <td><strong>Field name</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>command-line-flag</code></strong>
   </td>
   <td>OPTIONAL. String. For non-positional arguments, the flag which is associated with the argument on the command-line.
   </td>
  </tr>
  <tr>
   <td><strong><code>id</code></strong>
   </td>
   <td>REQUIRED. String. The argument ID. Alphanumeric values and underscores only. CamelCase is recommended.
   </td>
  </tr>
  <tr>
   <td><strong><code>list</code></strong>
   </td>
   <td>OPTIONAL. Boolean. Indicates whether or not the input field is a list of inputs. One of<strong><code> {true, false}</code></strong>. If omitted, it will be interpreted as false (e.g., non-list input).
   </td>
  </tr>
  <tr>
   <td><strong><code>name</code></strong>
   </td>
   <td>REQUIRED. String. Plain text name of input for display. Can contain spaces.
   </td>
  </tr>
  <tr>
   <td><strong><code>optional</code></strong>
   </td>
   <td>OPTIONAL. Boolean. Indicates whether or not the input field is required. One of <strong><code>{true, false}</code></strong>. If omitted, will be interpreted as false (e.g. non-optional input).
   </td>
  </tr>
  <tr>
   <td><strong><code>type</code></strong>
   </td>
   <td>REQUIRED. String. One of <strong><code>{"String", "File", "Flag", "Number"}</code></strong>.
   </td>
  </tr>
  <tr>
   <td><strong><code>value-choices</code></strong>
   </td>
   <td>OPTIONAL. List. List of possible values that the parameter may take.
   </td>
  </tr>
  <tr>
   <td><strong><code>value-key</code></strong>
   </td>
   <td>OPTIONAL. String. String to replace in command-line template string. If specified, this MUST NOT be either a superset or subset of the value-key attribute associated with another object in the descriptor; to ensure this, brackets are typically used (e.g. "<strong>[value]</strong>").
   </td>
  </tr>
</table>

In addition to describing inputs themselves, groups of inputs and their
relationships can be defined as follows in Table 4:

<table>
  <tr>
   <td colspan="2" ><strong>Table 4: </strong>List of group object properties and their role within the BIDS Application specification.
   </td>
  </tr>
  <tr>
   <td><strong>Field name</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>all-or-none</code></strong>
   </td>
   <td>OPTIONAL. Boolean. True if all parameters included in this group need to be included together..
   </td>
  </tr>
  <tr>
   <td><strong><code>description</code></strong>
   </td>
   <td>RECOMMENDED. String. Description of the input group.
   </td>
  </tr>
  <tr>
   <td><strong><code>id</code></strong>
   </td>
   <td>REQUIRED. String. A short, unique, informative identifier containing only alphanumeric characters and underscores.
   </td>
  </tr>
  <tr>
   <td><strong><code>members</code></strong>
   </td>
   <td>REQUIRED. List. IDs of the input parameters belonging to this group.
   </td>
  </tr>
  <tr>
   <td><strong><code>mutually-exclusive</code></strong>
   </td>
   <td>OPTIONAL. Boolean. True if only one input in the group may be selected at runtime.
   </td>
  </tr>
  <tr>
   <td><strong><code>name</code></strong>
   </td>
   <td>REQUIRED. String. A human-readable name for the input group.
   </td>
  </tr>
  <tr>
   <td><strong><code>one-is-required</code></strong>
   </td>
   <td>OPTIONAL. Boolean. True if at least one of the inputs in the group must be selected.
   </td>
  </tr>
</table>

#### Required arguments

BIDS Applications MUST provide the following arguments. Notes that "Argument ID"
is what is required to exist as the state "id" in the Boutiques descriptor, and
will be validated, while the example CLI Flag provides a possible way this could
be expressed in the tool's interface.

<table>
  <tr>
   <td colspan="3" ><strong>Table 5: </strong>List of custom object properties and roles within the BIDS Application specification.
   </td>
  </tr>
  <tr>
   <td><strong>Argument ID</strong>
   </td>
   <td><strong>e.g. CLI Flag</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>AnalysisLevel</code></strong>
   </td>
   <td><strong><code>--analysis-level</code></strong>
   </td>
   <td>REQUIRED. String. String with value-choices which are a subset of {run, session, subject, dataset, meta}. The app may support one or more of these analysis levels. A default may be set, and unsupported analysis levels should return an exit code of 17, consistent with the definition in Table 7.
   </td>
  </tr>
  <tr>
   <td><strong><code>Help</code></strong>
   </td>
   <td><strong><code>--help</code></strong>
   </td>
   <td>REQUIRED. Flag. Flag that specifies whether or not to show the help-text that describes how the tool may be correctly used.
   </td>
  </tr>
  <tr>
   <td><strong><code>InputDataset</code></strong>
   </td>
   <td><strong><code>--input-dataset</code></strong>
   </td>
   <td>REQUIRED. List. List of URIs/paths of the BIDS datasets to be processed. Whether or not the order of listed datasets is important MUST be specified in the parameter description. The tool MUST NOT reorder the user-specified list.
   </td>
  </tr>
  <tr>
   <td><strong><code>OutputLocation</code></strong>
   </td>
   <td><strong><code>--output-location</code></strong>
   </td>
   <td>REQUIRED. List. One URI/path to the location where all outputs will be stored.
   </td>
  </tr>
  <tr>
   <td><strong><code>ToolVersion</code></strong>
   </td>
   <td><strong><code>--version</code></strong>
   </td>
   <td>REQUIRED. Flag. Returns the version of the tool being used.
   </td>
  </tr>
</table>

##### Backwards compatibility

If an app wishes to maintain backwards compatibility with BIDS-Apps 1.0, then
the following command-line should be valid:

```bash
    bids-app InputDataset OutputLocation AnalysisLevel [options]
```

In this case, InputDataset is limited to a list of length one. It is worth
noting that all legacy apps can be supported in this spec, they just need to
write a descriptor which maps the inputs as they are expected and defined, here,
to their associated values in the original application.

#### Reserved arguments

The ability to filter BIDS entities (e.g. subject, session, or run) allows for
the selection of subsets of datasets. To be extensible as new entities are added
to the BIDS specification, the reserved arguments are defined here as a rule
which maps to BIDS entities, rather than specifying the moving goalpost of an
exhaustive list. The arguments may be specified as follows:

- The argument ID SHOULD be in CamelCase, with the form &lt;entity>Label or
  &lt;entity>Index, depending on whether the associated values are constrained
  to be alphanumeric or numeric, respectively.
- The argument MUST accept values referring to labels/indices, as consistent
  with the above, in either the form of a list or a file containing a
  line-delimited list. The items provided SHOULD NOT include the entity label in
  addition to the labels/indices.

While several examples exist within Table 5, to the following demonstrates how
the above rules can be applied for the BIDS entity "subject":

ID: `SubjectLabel`

CLI flag: `--subject-label`

Acceptable and equivalent usages:

```
    --subject-label 01 02 03
    --subject-label subject_ids.txt
```

\_Contents of `subject_ids.txt`:

```
01
02
03
```

In all cases where such arguments are defined and applied, only files in the
BIDS dataset that have a value for the specified entities will be subject to
filtering. That is, if a file does not have a given entity (e.g., entity value
for it is &lt;None>), the file will be included.

Applications are not required to support these arguments, but MUST NOT assign
these arguments to other meanings. To reduce conflicts, BIDS Applications SHOULD
avoid using this convention except for entities that are anticipated to be
standardized.

Example of an Interface descriptor: see 4.1.

For example, suppose we have an application with the following descriptor:

`example_app.json`:

```json
{
    "name": "Example BIDS App",
    "command-line": "bids-app [InputDataset] [OutputLocation] [AnalysisLevel] [ParticipantLabel] [OurRandomSeed]""inputs": [
        {
            "id": "InputDataset",
            "name": "Input datasets",
            "value-key": "[InputDataset]",
            "type": "File",
            "list": true,
            "optional": false,
            "command-line-flag": "--input-datasets"
        },
        {
            "id": "OutputLocation",
            "name": "Output location",
            "value-key": "[OutputLocation]",
            "type": "File",
            "optional": false,
            "command-line-flag": "--output-location"
        },
        {
            "id": "AnalysisLevel",
            "name": "Analysis level",
            "value-key": "[AnalysisLevel]",
            "type": "String",
            "optional": false,
            "value-choices": [
                "run",
                "session",
                "subject",
                "dataset"
            ],
            "default": "session",
            "command-line-flag": "--analysis-level"
        },
        {
            "id": "SubjectLabel",
            "name": "Subject labels",
            "value-key": "[SubjectLabel]",
            "type": "String",
            "list": true,
            "optional": true,
            "command-line-flag": "--subject-label"
        },
        {
            "id": "RandomSeed",
            "name": "Seed for pseudorandom number generator",
            "value-key": "[RandomSeed]",
            "type": "Number",
            "optional": true,
            "command-line-flag": "--random-seed"
        }
    ]
}
```

`input_params.json`

```json
{
  "InputDataset": ["/path/to/bids", "/path/to/derivatives"],
  "OutputLocation": "/path/to/output",
  "AnalysisLevel": "subject",
  "SubjectLabel": ["01", "02"],
  "RandomSeed": "0xB1D5CAF3"
}
```

### Outputs

#### File formats for the application specification and report

BIDS Apps MUST be able to be called via the BIDS Application Boutiques
descriptor and corresponding input parameter dictionary files, commonly referred
to in the Boutiques parlance as "invocations", and accept any BIDS dataset. It
is RECOMMENDED that BIDS Applications produce BIDS-Derivatives-compliant
datasets.

<table>
  <tr>
   <td colspan="2" >Table 6: List of relevant output-files object properties for the BIDS Application specification.
   </td>
  </tr>
  <tr>
   <td><strong>Field name</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>command-line-flag</code></strong>
   </td>
   <td>OPTIONAL. String. Flag associated with the argument on the command-line. Examples: -o, --output
   </td>
  </tr>
  <tr>
   <td><strong><code>description</code></strong>
   </td>
   <td>RECOMMENDED. String. A plain-text description of the output-files of the BIDS Application.
   </td>
  </tr>
  <tr>
   <td><strong><code>file-template</code></strong>
   </td>
   <td>OPTIONAL. Array of strings. An array of strings that may contain value keys and together populate the self-contained structure of a configuration file.
   </td>
  </tr>
  <tr>
   <td><strong><code>id</code></strong>
   </td>
   <td>REQUIRED. String. A short, unique, informative identifier containing only alphanumeric characters and underscores. Typically used to generate variable names. (should conform <strong><code>^[0-9,_,a-z,A-Z]*$</code></strong>). Example: "data_file"
   </td>
  </tr>
  <tr>
   <td><strong><code>list</code></strong>
   </td>
   <td>OPTIONAL. Boolean. True if output is a list of values.
   </td>
  </tr>
  <tr>
   <td><strong><code>name</code></strong>
   </td>
   <td>REQUIRED. String. A human-readable output name. Example: 'Supplementary input file for X task'.
   </td>
  </tr>
  <tr>
   <td><strong><code>optional</code></strong>
   </td>
   <td>OPTIONAL. Boolean. True if output may not be produced by the tool.
   </td>
  </tr>
  <tr>
   <td><strong><code>path-template</code></strong>
   </td>
   <td>OPTIONAL. String. Describes the output file path relative to the execution directory. May contain input value keys and wildcards. Example: "xx".
   </td>
  </tr>
  <tr>
   <td><strong><code>path-template-stripped-extensions</code></strong>
   </td>
   <td>OPTIONAL. List. List of file extensions that will be stripped from the input values before being substituted in the path template. Example: [".nii",".nii.gz"].
   </td>
  </tr>
  <tr>
   <td><strong><code>value-key</code></strong>
   </td>
   <td>OPTIONAL. String. A string contained in command-line, substituted by the output value and/or flag at runtime.
   </td>
  </tr>
</table>

#### Execution Report & Updating Dataset Description

When generated, an execution report that completely describes the processing
that was executed and the dataset MUST comply with the BIDS Provenance Extension
Proposal (BEP28). These outputs are OPTIONAL, and if provided, should be
specified in the `output-files` section of the tool descriptor.

Similarly, the dataset_description.json file SHOULD be updated to reflect the
processing that has occurred by the BIDS Application.

### Behaviors

For a given set of arguments, the behavior of a BIDS Application will typically
vary based on the contents of the input dataset. The dataset may be
BIDS-compliant, or it may not; and it may contain the file types the BIDS App
requires, or it may not. This section describes the expected behavior under each
combination of cases, and describes RECOMMENDED exit codes on systems that
support them.

#### Valid BIDS datasets

If the dataset is BIDS-compliant and contains the files required by the
application, then the application should make a best effort to perform its task
to completion.

If the dataset is BIDS-compliant but does not contain the files required by the
application, then the application MAY fail immediately or when attempting to
open a missing file. In this case, it is RECOMMENDED to use exit code 66
(NOINPUT).

#### Invalid BIDS datasets

If the dataset is not BIDS-compliant, then the BIDS App MAY fail immediately
with exit code 16.

If the dataset contains the required files but is not BIDS-compliant (e.g., a
"dirty" dataset that has more files than needed), then the BIDS App MAY treat
the dataset as valid.

#### Exit codes

An exit code or [exit status](https://en.wikipedia.org/wiki/Exit_status) is an
integer indicating the reason for termination for use by the parent program or
operating system. The interpretation of exit codes varies across systems, and
programmers SHOULD follow the conventions of the systems for which they are
programming.

Most operating systems, including POSIX (Linux, Mac OSX) and Windows use 0 to
indicate success and >0 to indicate failure. POSIX systems are limited to an
unsigned byte (range: 0-255), so these recommendations are limited to that
range. Exit codes 64-78 are specified in BSD
[sysexits(3)](https://www.freebsd.org/cgi/man.cgi?query=sysexits&sektion=3), and
should be avoided unless applicable. Exit codes 2 and 126-165 may be set by
[Bash](https://www.tldp.org/LDP/abs/html/exitcodes.html), and so will be
reserved.

The following exit codes are RECOMMENDED for consistent error handling under
POSIX and Windows environments:

<table>
  <tr>
   <td colspan="2" >Table 7: Reserved exit codes and their definitions.
   </td>
  </tr>
  <tr>
   <td><strong>Exit code</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td><strong><code>0</code></strong>
   </td>
   <td>SUCCESS. The program completed successfully.
   </td>
  </tr>
  <tr>
   <td><strong><code>1</code></strong>
   </td>
   <td>FAILURE. The program failed for unspecified reasons.
   </td>
  </tr>
  <tr>
   <td><strong><code>2</code></strong>
   </td>
   <td>Reserved
   </td>
  </tr>
  <tr>
   <td><strong><code>16-31</code></strong>
   </td>
   <td><em>BIDS-related codes. Reserved except the following</em>
   </td>
  </tr>
  <tr>
   <td><strong><code>16</code></strong>
   </td>
   <td>An input dataset failed BIDS validation.
   </td>
  </tr>
  <tr>
   <td><strong><code>17</code></strong>
   </td>
   <td>Unknown analysis level.
   </td>
  </tr>
  <tr>
   <td><strong><code>18</code></strong>
   </td>
   <td>Entity-based filtering options selected no files.
   </td>
  </tr>
  <tr>
   <td><strong><code>19</code></strong>
   </td>
   <td>Both command-line arguments and a parameter invocation file were passed to the application.
   </td>
  </tr>
  <tr>
   <td><strong><code>64-78</code></strong>
   </td>
   <td><em>BSD codes - Reserved except the following.</em>
   </td>
  </tr>
  <tr>
   <td><strong><code>64</code></strong>
   </td>
   <td>USAGE. The command was used incorrectly.
   </td>
  </tr>
  <tr>
   <td><strong><code>65</code></strong>
   </td>
   <td>DATAERR. The input data was incorrect in some way.
   </td>
  </tr>
  <tr>
   <td><strong><code>66</code></strong>
   </td>
   <td>NOINPUT. The input data was missing or unreadable.
   </td>
  </tr>
  <tr>
   <td><strong><code>73</code></strong>
   </td>
   <td>CANTCREAT. An output file/directory cannot be created.
   </td>
  </tr>
  <tr>
   <td><strong><code>74</code></strong>
   </td>
   <td>IOERR. Failure during file reading/writing.
   </td>
  </tr>
  <tr>
   <td><strong><code>75</code></strong>
   </td>
   <td>TEMPFAIL. Temporary failure. Another run is expected to succeed.
   </td>
  </tr>
  <tr>
   <td><strong><code>126-165</code></strong>
   </td>
   <td><em>BASH codes - Reserved</em>
   </td>
  </tr>
</table>

## Example BIDS App

This section describes a BIDS Application named bids-app that can only operate
at the participant analysis leveland accepts a numeric seed for a random number
generator.

### Interface descriptor

```json
{
  "name": "Example BIDS App",
  "tool-version": "0.0.1",
  "schema-version": "0.5",
  "custom": {
    "BIDSApplicationVersion": "2.0"
  },
  "command-line": "bids-app [InputDataset] [OutputLocation] [AnalysisLevel] [ParticipantLabel] [RandomSeed]",
  "inputs": [
    {
      "id": "InputDataset",
      "name": "Input datasets",
      "value-key": "[InputDataset]",
      "type": "File",
      "list": true,
      "optional": false,
      "command-line-flag": "--input-dataset"
    },
    {
      "id": "OutputLocation",
      "name": "Output location",
      "value-key": "[OutputLocation]",
      "type": "File",
      "optional": false,
      "command-line-flag": "--output-location"
    },
    {
      "id": "AnalysisLevel",
      "name": "Analysis level",
      "value-key": "[AnalysisLevel]",
      "type": "String",
      "optional": true,
      "value-choices": ["participant"],
      "default-value": "participant",
      "command-line-flag": "--analysis-level"
    },
    {
      "id": "SubjectLabel",
      "name": "Participant labels",
      "value-key": "[ParticipantLabel]",
      "type": "String",
      "list": true,
      "optional": true,
      "command-line-flag": "--participant-label"
    },
    {
      "id": "OurRandomSeed",
      "name": "Seed for pseudorandom number generator",
      "description": "Example parameter that may be relevant.",
      "value-key": "[OurRandomSeed]",
      "type": "Number",
      "optional": true,
      "command-line-flag": "--random-seed"
    }
  ]
}
```

### Invocation definition

Two example input definitions follow:

`input_params1.json`

```json
{
  "InputDataset": ["/path/to/bids", "/path/to/derivatives"],
  "OutputLocation": "/path/to/output",
  "AnalysisLevel": "participant",
  "SubjectLabel": ["01", "02"],
  "RandomSeed": 2983578366
}
```

`input_params2.json`

```json
{
  "InputDataset": ["/path/to/bids", "/path/to/derivatives"],
  "OutputLocation": "/path/to/output",
  "AnalysisLevel": "participant"
}
```

#### BIDS App compatible example

Before the BIDS Application specification existed there were BIDS Apps.
Attention has been paid to ensure that BIDS Exec apps can be compatible with
existing BIDS Apps.

For example, the term participant was widely used in BIDS Apps, whereas subject
is the preferred term in BIDS. To allow backwards compatibility here you can
use:

```json
{
  "id": "SubjectLabel",
  "name": "Participant labels",
  "value-key": "[ParticipantLabel]",
  "type": "String",
  "list": true,
  "optional": true,
  "command-line-flag": "--participant-label"
}
```

## Change-log

**v0.0.1 YYYY-MM-DD:**

- Initial work on specification
- X, Y and Z features added

## A. Summary of changes from BIDS Apps 1.0

### New features

- Adopted Boutiques validatable and runnable descriptive standard
- Increased flexibility for runtime arguments and command-line formatting
- Defined exit codes to indicate various application outcomes
- Link between application descriptions and data specification versions
- Extensible definition which will scale with the BIDS standards as new entities
  are added

### Deprecated features

- Position arguments are no longer supported.

### Suggested migration process
