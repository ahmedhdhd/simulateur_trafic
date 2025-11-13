from binascii import a2b_qp
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from tests.conftest import route_simple
from tests.conftest import vehicule_exemple
from tests.conftest import reseau_simple


def test_avancer_position_modifiee(vehicule_exemple):
  
    vehicule = vehicule_exemple
    
    position_initiale = vehicule.position
    vitesse = vehicule.vitesse
    delta_t= 5
    vehicule.avancer(delta_t)
    position_attendue = position_initiale + (vitesse * delta_t)
    assert vehicule.position == position_attendue


def test_avancer_ne_depasse_pas_longueur_route():
    route = Route("Route A", longueur=100, limite_vitesse=50)
    vehicule = Vehicule("V1", position=90, vitesse=50, route_actuelle=route)
    vehicule.avancer(5)
    
    assert vehicule.position == 100


def test_changer_de_route(vehicule_exemple):

    vehicule = vehicule_exemple
    route_initiale = vehicule.route_actuelle
    
    nouvelle_route = Route("Route B", longueur=500, limite_vitesse=30)
    
    vehicule.changer_de_route(nouvelle_route)
    
    assert vehicule.route_actuelle == nouvelle_route
    assert vehicule not in route_initiale.vehicules
    assert vehicule in nouvelle_route.vehicules
    assert vehicule.position == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])