"""Example Provenance Metadata

    This module provides sample json(ld) metadata for to label docker containers and
    outputs the metadata as triples to sanity check rdf generation.

Returns:
    Nothing
"""

import json
import uuid
from pyld import jsonld
from datetime import datetime
from pytz import timezone
from os import environ

doc = {}

"""
doc = {
    "http://schema.org/name": "Manu Sporny",
    "http://schema.org/url": {"@id": "http://manu.sporny.org/"},
    "http://schema.org/image": {"@id": "http://manu.sporny.org/images/manu.png"}
} """


context = {
  "xsd": "http://www.w3.org/2001/XMLSchema#",
  "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
  "prov": "http://www.w3.org/ns/prov#",
  "foaf": "http://xmlns.com/foaf/0.1/",
  "schema": "http://schema.org/",
  "frapo": "http://purl.org/cerif/frapo/",
  "agent": { "@type": "@id", "@id": "prov:Agent" },
  "person": {"@type": "@id", "@id": "prov:Person"},
  "givenName": {"@id": "schema:givenName"},
  "familyName": {"@id": "schema:familyName"},
  "honorificSuffix": {"@id": "schema:honorificSuffix"},
  "honorificPrefix": {"@id": "schema:honorificPreifx"},
  "hasFamilialSuffix": {"@id": "frapo:hasFamilialSuffix"},
  "softwareAgent": { "@type": "@id", "@id": "prov:SoftwareAgent" },
  "actedOnBehalfOf": {"@type": "@id", "@id": "prov:actedOnBehalfOf"},
  "entity": { "@type": "@id", "@id": "prov:Entity" },
  "activity": { "@type": "@id", "@id": "prov:Activity" },
  "hadPlan": { "@type": "@id", "@id": "prov:hadPlan" },
  "hadRole": { "@type": "@id", "@id": "prov:hadRole" },
  "wasAttributedTo": { "@type": "@id", "@id": "prov:wasAttributedTo" },
  "wasAssociatedWith": { "@type": "@id", "@id": "prov:wasAssociatedWith" },
  "used": { "@type": "@id", "@id": "prov:used" },
  "wasUsedBy": { "@type": "@id", "@id": "prov:wasUsedBy" },
  "wasGeneratedBy": { "@type": "@id", "@id": "prov:wasGeneratedBy" },
  "startedAtTime": { "@type": "xsd:dateTime", "@id": "prov:startedAtTime" },
  "endedAtTime": { "@type": "xsd:dateTime", "@id": "prov:endedAtTime" },
  "label": "rdfs:label",
  "comment": "rdfs:comment"
}


# Generate URI's for docker instance
#  Fronm Singularity https://singularity.lbl.gov/docs-docker
# The General URI scheme for a docker image is
#   * registry (e.g, "index.docker.io")
#   * namespace (e.g, "library")
#   * repository (e.g., "ubuntu")
#   * tag (e.g., "latest" ) OR Version (e.g., "@sha256:1234...")
# EX docker://<registry>/<namespace>/<repo_name>:<repo_tag>
# docker://index.docker.io/library/ubuntu:latest
# docker://index.docker.io/library/ubuntu@sha256:1235...

dockerEntityuuid = str(uuid.uuid4())
dockerActivityuuid = str(uuid.uuid4())
URIDockerActivity = "urn:sc:"+dockerActivityuuid+"#dockerActivity"
URIDockerEntity = "docker://index.docker.io/library/ubuntu:latest"
### WARNING WARNING this needs to be generated and stored in the config.
dockerUseruuid = str(uuid.uuid4())

chuckORID = "http://orcid.org/000-0003-4901-6059/"
chuck = "https://w3id.org/people/cvardeman#me"

provActivity = {
    '@id': URIDockerActivity,
    '@type': 'activity',
    'startedAtTime': datetime.now(timezone('Europe/London')).isoformat(),
    'label': 'Execute Docker Command',
    'comment': 'Executing Docker Command: Docker Run Container'
}

provEntity = {
    '@id': URIDockerEntity,
    '@type': 'entity',
    'wasGeneratedBy': URIDockerActivity,
    'label': 'Cats'
}

provAgent = []

provAgent.append({
    '@id': chuck,
    '@type': 'person',
    'givenName': 'Charles',
    'familyName': 'Vardeman',
    'honorificSuffix': 'PhD',
    'hasFamilialSuffix': 'II'
})

provAgent.append({
    '@id': 'https://sc.org/sc#sc',
    '@type': 'softwareAgent',
    'label': 'SmartContainers',
    'comment': "SmartContainers Provenance Tool",
    'actedOnBehalfOf': chuck
 })

provAgent.append({
     '@id': 'https://sc.org/sc#docker',
     '@type': 'softwareAgnet',
     'label': 'Docker',
     'comment': "Docker Command Line Tool",
     'actedOnBehalfOf': 'https://sc.org/sc#sc'
 })

def main():

    provActivity['endedAtTime'] = datetime.now(timezone('Europe/London')).isoformat()
    prov = {
    '@context': context,
    '@graph': [provActivity] + [provEntity] + provAgent
    }
    print(json.dumps(prov, indent=2))

    data_nor = jsonld.normalize(prov, {'format': 'application/nquads'})
    print("\n N-Quads data")
    print(data_nor)

if __name__ == "__main__":
    main()


def get_json_ld():
#    return ds.serialize(format='json-ld', context=context, indent=4)
    pass

def get_commit_data():
   # return ds.serialize(format='json-ld', context=context, indent=4)
   pass

def get_commit_label():
    # return ds.serialize(format='json-ld', context=context, indent=4)
    pass
