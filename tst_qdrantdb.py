#!/bin/python
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer('all-MiniLM-L6-v2')
documents = [
        {"name":"title1", "shortdescription1":"sd1"},
        {"name":"title2", "shortdescription2":"sd2"},
        {"name":"title3", "shortdescription3":"sd3"},
        {"name":"title4", "shortdescription4":"sd4"},
        {"name":"title5", "shortdescription5":"sd5"},
        {"name":"title6", "shortdescription6":"sd6"},
        {"name":"title7", "shortdescription7":"sd7"},
        {"name":"title8", "shortdescription8":"sd8"},
        {"name":"title9", "shortdescription9":"sd9"},
        {"name":"title10", "shortdescription10":"sd10"},
        {"name":"title11", "shortdescription11":"sd11"},
        {"name":"title12", "shortdescription12":"sd12"},
        {"name":"title13", "shortdescriptioni3":"sd13"},
        {"name":"title14", "shortdescription14":"sd14"},
        {"name":"title15", "shortdescription15":"sd15"}, ]

