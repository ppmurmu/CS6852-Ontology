import xml.etree.ElementTree as ET
from owlready2 import *
from rdflib import *
from collections import Counter

onto = get_ontology("financial_ontology.owl").load()

for instance in onto.individuals():
    destroy_entity(instance)


for cls in onto.classes():
    for instance in cls.instances():
        print(f"  Instance: {instance}")

# Load the data from the XML file
tree = ET.parse("data.xml")
root = tree.getroot()

# Create individuals for companies
for company in root.findall("Company"):
    company_id = company.get('id')
    # Use name mapping to get the correct class name
    company_class_name = "Company"
    #print(company_id, getattr(onto, company_class_name))
    getattr(onto, company_class_name)(company_id)


# Create individuals for actions
for action in root.findall('Action'):
    action_id = action.get('id')
    action_type = action.get('type')
    #print(action_id, action_type)
    # Create an instance of the action type
    getattr(onto, action_type)(action_id)


# Create individuals for properties
for prop in root.findall('Property'):
    prop_id = prop.get('id')
    prop_type = prop.get('type')
    getattr(onto, prop_type)(prop_id)


# Create individuals for aspects
for aspect in root.findall('Aspect'):
    aspect_id = aspect.get('id')
    aspect_type = aspect.get('type')
    # Create an instance of the aspect type
    getattr(onto, aspect_type)(aspect_id)

# Create individuals for information and link them
for info in root.findall('Information'):
    info_id = info.get('id')
    company_id = info.get('isAboutCompany')
    aspect_id = info.get('isAboutAspect')
    describes_aspect_id = info.get('describesAspect')

    # Create an instance of Information
    info_instance = onto.Information(info_id)

    # Link the information instance to the corresponding company, aspect, and describes aspect
    #print(info_instance)
    info_instance.isAboutCompany = [getattr(onto, company_id)]
    info_instance.isAboutAspect = [getattr(onto, aspect_id)]
    info_instance.describesAspect = [getattr(onto, describes_aspect_id)]

# Run the reasoner
sync_reasoner()

print("\n ---RDF triples generated successfully--- \n")

# Save the combined ontology and data
onto.save(file="rdf_triples.rdf", format="rdfxml")



inferred_graph = Graph()
#Display inferred triples
for s, p, o in default_world.as_rdflib_graph().triples((None, None, None)):
    if (s, p, o) not in onto.get_triples():
        inferred_graph.add((s, p, o))

inferred_graph.serialize(destination="inferred_triples.rdf", format="xml")



rdf_graph = Graph()

# Get all instances of PositiveInfo
positive_infos = onto.PositiveInfo.instances()

# Display positive information
print("Inferring Positive Information from the Ontology:")
for info in positive_infos:
    print(f"  {(info)}")    
    info_uri = info.iri
    rdf_graph.add((URIRef(info_uri), RDF.type, URIRef(onto.PositiveInfo.iri)))


rdf_graph.serialize(destination="postive_info.rdf", format="xml")


