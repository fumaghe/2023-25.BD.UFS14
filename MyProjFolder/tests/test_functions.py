import pytest
import requests
from mymodule import get_pubchem_cid

def test_get_pubchem_cid():
    session = requests.Session()
    ingredient_name = "Aspirin"
    cid = get_pubchem_cid(session, ingredient_name)
    assert cid == "2244", "Il CID per l'Aspirina dovrebbe essere '2244'"