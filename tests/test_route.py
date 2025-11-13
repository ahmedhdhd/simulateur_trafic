import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from tests.conftest import route_simple
from tests.conftest import vehicule_exemple
from tests.conftest import reseau_simple


def test_ajout_vehicule(route_simple):

    route = route_simple
    assert len(route.vehicules) == 0
    
    vehicule = Vehicule("V1", position=0, vitesse=10)
    route.ajouter_vehicule(vehicule)
    
    assert len(route.vehicules) == 1
    assert vehicule in route.vehicules


def test_mise_a_jour_avance_vehicules(route_simple, vehicule_exemple):

    route = route_simple
    vehicule = vehicule_exemple
    
    route.ajouter_vehicule(vehicule)
    
    position_initiale = vehicule.position
    delta_t = 5
    route.mettre_a_jour_vehicules(delta_t)
    
    position_attendue = position_initiale + (vehicule.vitesse * delta_t)
    assert vehicule.position == position_attendue


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])