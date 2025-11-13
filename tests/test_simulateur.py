import sys
import os
import json
import pytest
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simulateur_trafic.core.simulateur import Simulateur
from simulateur_trafic.models.vehicule import Vehicule
from simulateur_trafic.models.route import Route
from tests.conftest import route_simple
from tests.conftest import vehicule_exemple
from tests.conftest import reseau_simple

def test_initialisation(tmp_path):

    config_data = {
        "routes": [
            {
                "nom": "Route A",
                "longueur": 1000,
                "limite_vitesse": 50
            }
        ],
        "vehicules": [
            {
                "id": "V1",
                "position": 0,
                "vitesse": 20,
                "route_actuelle": "Route A"
            }
        ]
    }
    
    config_file = tmp_path / "config_test.json"
    with open(config_file, 'w') as f:
        json.dump(config_data, f)
    
    simulateur = Simulateur(str(config_file))
    
    assert "Route A" in simulateur.reseau.routes
    route = simulateur.reseau.routes["Route A"]
    assert route.nom == "Route A"
    assert route.longueur == 1000
    assert route.limite_vitesse == 50
    
    assert len(route.vehicules) == 1
    vehicule = route.vehicules[0]
    assert vehicule.id == "V1"
    assert vehicule.position == 0
    assert vehicule.vitesse == 20


def test_execution_simulation(reseau_simple):
    """
    Test 4 - Objectif : tester l'intégration du simulateur complet.
    Test : Exécution d'une simulation sur plusieurs tours sans erreur.
    """
    simulateur = Simulateur()
    
    simulateur.reseau = reseau_simple
    
    with patch('simulateur_trafic.core.simulateur.exporter_vers_csv'), \
         patch('simulateur_trafic.core.simulateur.exporter_vers_json'), \
         patch('simulateur_trafic.core.simulateur.afficher_etat_reseau'):
        
        simulateur.lancer_simulation(n_tours=3, delta_t=60)
    
    assert len(simulateur.historique) == 3
    
    for i, tour_data in enumerate(simulateur.historique):
        assert "tour" in tour_data
        assert "nb_routes" in tour_data
        assert "nb_vehicules_total" in tour_data
        assert "routes" in tour_data
        assert tour_data["tour"] == i + 1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])