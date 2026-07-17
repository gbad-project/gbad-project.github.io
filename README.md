# Graph-Based Archival Description

Welcome to the official GitHub page of the Graph-Based Archival Description project. The project is brought to you by a team from the Archives of Ontario and University of Toronto and co-funded from a [Canadian federal grant](https://sshrc-crsh.canada.ca/en/competition-results/award-recipients/2024/partnership-engage-grants-sep.aspx).

The grant was completed in December 2025. Its deliverable is DrawRDF – a Draw\.io plugin that adds an option to export diagrams to Resource Description Framework (RDF) graphs. It is available publicly and for free here: <https://gbad-project.github.io/drawio/src/main/webapp/?p=rdf>

A 5-minute video demo of basic functionality is available on YouTube: <https://www.youtube.com/watch?v=LaUAY8NCPqY>

Additional documentation for DrawRDF is available here: <https://drawrdf.readthedocs.io/>

A whitepaper is currently being prepared for publication. We will post a notification here as soon as it is available.

Please feel free to [contact us](mailto:p.zhelnov@mail.utoronto.ca) if you have any questions.

Thank you for your interest in our project!

## Association of Canadian Archivists (ACA) Conference 2025

Download the slide deck PDF here: <https://github.com/gbad-project/.github/raw/refs/heads/main/Graph-Based_Archival_Description_-_ACA_Presentation_-_2025-06-10.pdf>

## Implementation Toolkit

April 2025 Update: To allow archivists, librarians and others to replicate this work within their own institutions, Bachelor of Information students Thomas Fox, Harrison Huang and Russell Luchin created a toolkit for the Graph-Based Archival Description used at the Archives of Ontario.

Download the Toolkit PDF here:
<https://github.com/gbad-project/.github/raw/refs/heads/main/GBAD_Toolkit_Fox_Huang_Luchin_2025-04-10.pdf>

License: [CC BY 4.0 International](https://creativecommons.org/licenses/by/4.0/)

Note: As of June 2, 2025, the Toolkit [was found](https://github.com/gbad-project/records_in_contexts_draw_io_parser/tree/99cdb78637abbe14e2a0cad3f63b0ca7d1df0c30/reproduce_gbad_toolkit) to require additional Python programming to be reproduced. Please [open an issue](https://github.com/gbad-project/records_in_contexts_draw_io_parser/issues/new) if you are reading this and need help, or reach out using the contacts indicated on the
project’s GitHub page at: <https://github.com/gbad-project>

## Project Summary

The Archives of Ontario, the GLAM Incubator and Profs. Anastasia Kuzminykh and Shion Guha at the University of Toronto have collaborated to create a proof of concept that explores the possibilities and potential benefits of a graph-based data model for archival description, using the International Council on Archives’ new Records in Contexts (RiC) standard and Linked Open Data (RDF data format) ([Introductory YouTube video](https://youtu.be/TLHU_0QKOWQ)). The traditional archival finding aid, with its static and inflexible hierarchies, fails to represent the complexity and nuanced reality of record creation, accumulation, use and re-use over time.

Recent efforts to overcome this limitation have turned to entity-relationship based models developed by the graph theory of knowledge representation, with its infinitely flexible and extensible subject-predicate-object expressions of data (semantic triples). The overall objective of this project is to develop a data model, to select and model a small-scale sample of data drawn from the Archives of Ontario’s datasets, and to thereby test the possibilities and potential benefits for internal staff and public end-users. This work represents a paradigm shift for archival description: it promises a vastly improved ability to represent the reality of record creation, to manage the complexity of digital metadata, to allow machine-readable encoding of meaning that enables complex logical inferences and search capabilities, and to connect currently siloed datasets with related data across the world. In short, this proposed project will break new ground in the Canadian archival sector.

Source: <https://glam.ischool.utoronto.ca/?project=graph-based-archival-description-at-the-archives-of-ontario>

# Meet Our Team

Feature Article. <https://ischool.utoronto.ca/news/a-glam-makeover-for-the-archives-of-ontario/>

YouTube Video. <https://youtu.be/3ZtTppHhyN0>

## Resources

This page is in development. Here are the main repositories you can access through this GitHub page:

Our fork of Richard Williamson’s Draw.io parser with added support for modelling RML graphs. <https://github.com/gbad-project/records_in_contexts_draw_io_parser>

Our fork of Draw.io itself, with a custom plugin for RDF export. <https://github.com/gbad-project/drawio/blob/gbad/src/main/webapp/plugins/rdfexport/README.md>

Sparnatural fork and demo. <https://github.com/gbad-project/gbad-project.github.io>

Our fork of a Visual Studio Code Turtle RDF code autocomplete extension. <https://github.com/gbad-project/turtle-vocab-autocomplete>

For a simple and lightweight URI dereferencer, supported by a Python/Oxigraph-backed YASGUI instance and suitable for ultralightweight VPS deployments (under 2 GB RAM!), reach out using our contact email.

<!--- Our fork of Trifid, a lightweight RDF server written in Node.js and built on top of an Oxigraph quadstore instance. REMOVED for security reasons. There wasn't much was added on our side, though. Please explore the original repo if you are interested: <https://github.com/zazuko/trifid/> --->

<!---
[GitHub repo]({{ site.gh-repo }}) \| This is a fork of [Démonstrateur Sparnatural des Archives nationales de France](https://sparna-git.github.io/sparnatural-demonstrateur-an/) \| [Original GitHub repo](https://github.com/sparna-git/sparnatural-demonstrateur-an) \| SPARQL endpoint to use: <http://51.159.140.210/graphdb/repositories/sparnatural-demo-anf> \| [Our fork of draw.io](https://gbad-project.github.io/drawio/src/main/webapp/index.html)

{% if page.url == "/" %}

## Graph-Based Archival Description at the Archives of Ontario

> The Archives of Ontario, the GLAM Incubator and Profs. Anastasia Kuzminykh and Shion Guha at the University of Toronto will collaborate to create a proof of concept that explores the possibilities and potential benefits of a graph-based data model for archival description, using the International Council on Archives’ new Records in Contexts (RiC) standard and Linked Open Data (RDF data format). The traditional archival finding aid, with its static and inflexible hierarchies, fails to represent the complexity and nuanced reality of record creation, accumulation, use and re-use over time.Recent efforts to overcome this limitation have turned to entity-relationship based models developed by the graph theory of knowledge representation, with its infinitely flexible and extensible subject-predicate-object expressions of data (semantic triples). The overall objective of this project is to develop a data model, to select and model a small-scale sample of data drawn from the Archives of Ontario’s datasets, and to thereby test the possibilities and potential benefits for internal staff and public end-users. This work represents a paradigm shift for archival description: it promises a vastly improved ability to represent the reality of record creation, to manage the complexity of digital metadata, to allow machine-readable encoding of meaning that enables complex logical inferences and search capabilities, and to connect currently siloed datasets with related data across the world. In short, this proposed project will break new ground in the Canadian archival sector.

Source: <https://glam.ischool.utoronto.ca/?project=graph-based-archival-description-at-the-archives-of-ontario>

{% endif %}

## d3sparql.js

[Live demo](http://biohackathon.org/d3sparql/) \| JavaScript library for executing SPARQL query and transforming resulted JSON for visualization in D3.js. \| [GitHub repo](https://github.com/ktym/d3sparql)

--->

## Original Page Content
