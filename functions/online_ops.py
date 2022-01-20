import wikipedia
from Bio import Entrez

# To contact NCBI without any issues
#Entrez.api_key = "MyAPIkey"
Entrez.email = "govind83nair@gmail.com"

# Getting the Entrez DBs here so that this operation is nor repeated
#ehan = Entrez.einfo()
#entrez_dbs = ehan.read(ehan)

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    #references = wikipedia.WikipediaPage.references(query)
    return(results)

def search_entrez(query):
    ehan = Entrez.einfo()
    entrez_dbs = ehan.read(ehan)
    db_counts = {}
    for dbn in entrez_dbs(['DbList']):
        entrez_handle = Entrez.esearch(db= dbn,term=query,retmax="40")
        entrez_record = Entrez.read(entrez_handle)
        db_counts[dbn] = entrez_record["Count"]
    return(db_counts)