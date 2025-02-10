# Assignment-4
By: Pradeep Peter Murmu, CS24M033

## Contents 
The folder consists of 6 files.
1. data.xml :- the XML file with our ontology based data.
2. financial_ontology.owl :- The ontology file generated from Protege.
3. mapping.py :- The python script to generate RDF triples, Inferred Triples and some other query.
4. rdf_triples.rdf :- Output file of converting our XML file into RDF triples.
5. inferred_triples.rdf :- Output file of inferred RDF triples from the XML file and ontology.
6. positive_info.rdf :- Output file of a query using RDF triples.

## Steps to execute locally
1. Set up the python environment.
2. Install "owlready2" and "rdflib" from PIP.
3. run "python3 mapping.py" in the same directory.  (*use python command based on installed version)

## Result
1. A query about "postive info" will be shown on the terminal.
2. rdf_triples.rdf , inferred_triples.rdf, and positive_info.rdf files will be generated in the same directory.




