from fastapi import FastAPI
from dnslookup.resolver import lookup

app = FastAPI()

@app.get("/dns/{domain}")
def get_dns(domain: str):
    return lookup(domain)