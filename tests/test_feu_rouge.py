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


def test_cycle_du_feu():
    # TODO : créer un feu et tester la succession des états
    feu = FeuRouge()
    assert feu.etat == 'rouge'

