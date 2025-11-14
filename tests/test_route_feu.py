import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from tests.conftest import route_simple
from tests.conftest import vehicule_exemple
from tests.conftest import reseau_simple
from simulateur_trafic.models.feu_rouge import FeuRouge

def test_arret_au_feu_rouge():
    # TODO : créer une route, un feu et un véhicule  
    route = Route("Test Route", longueur=1000, limite_vitesse=30)
    feu = FeuRouge(cycle=10)
    route.ajouter_feu_rouge(feu, position=500)
    vehicule = Vehicule("V1", position=400, vitesse=20)
    route.ajouter_vehicule(vehicule)
    feu.etat_courant = 'rouge'
    initial_position = vehicule.position
    route.update(dt=1.0)
    assert vehicule.position <= 500
    assert vehicule.position > initial_position