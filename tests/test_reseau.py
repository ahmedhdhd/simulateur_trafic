import sys
import os
import pytest
from unittest.mock import Mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simulateur_trafic.models.reseau import ReseauRoutier
from simulateur_trafic.models.route import Route
from simulateur_trafic.models.vehicule import Vehicule
from tests.conftest import route_simple
from tests.conftest import vehicule_exemple
from tests.conftest import reseau_simple


def test_ajout_routes():

    reseau = ReseauRoutier()
    assert len(reseau.routes) == 0
    
    route_a = Route("Route A", longueur=1000, limite_vitesse=50)
    route_b = Route("Route B", longueur=1500, limite_vitesse=60)
    
    reseau.ajouter_route(route_a)
    reseau.ajouter_route(route_b)
    
    assert len(reseau.routes) == 2
    assert "Route A" in reseau.routes
    assert "Route B" in reseau.routes
    assert reseau.routes["Route A"] == route_a
    assert reseau.routes["Route B"] == route_b


def test_mise_a_jour(reseau_simple):

    reseau = reseau_simple
    
    route_a = None
    for route in reseau.routes.values():
        if len(route.vehicules) > 0:
            route_a = route
            break
    
    if route_a and len(route_a.vehicules) > 0:
        vehicule = route_a.vehicules[0]
        position_initiale = vehicule.position
        vitesse = vehicule.vitesse
        
        delta_t = 5
        reseau.mettre_a_jour(delta_t)
        
        position_attendue = position_initiale + (vitesse * delta_t)
        assert vehicule.position == position_attendue


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])