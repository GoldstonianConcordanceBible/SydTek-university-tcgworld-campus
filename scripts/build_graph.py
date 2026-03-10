import json

with open("ontology/entities/angelic_beings.json") as f:
    angels = json.load(f)

with open("ontology/entities/doctrines.json") as f:
    doctrines = json.load(f)

with open("knowledge_graph/edges.json") as f:
    edges = json.load(f)

print("Entities loaded:", len(angels["entities"]) + len(doctrines["entities"]))
print("Edges loaded:", len(edges["edges"]))