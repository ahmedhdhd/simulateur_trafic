# Documentation du Simulateur de Trafic

## Table des matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Configuration](#configuration)
- [API](#api)

## Introduction

Le Simulateur de Trafic est une application Python qui modélise le mouvement des véhicules sur un réseau routier. Il permet de simuler différents scénarios de trafic, de collecter des statistiques et d'analyser les résultats.

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip

### Installation depuis les sources
```bash
git clone https://github.com/votre-utilisateur/simulateur-trafic.git
cd simulateur-trafic
pip install -r requirements.txt
```

### Installation en mode développement
```bash
pip install -e .
```

## Utilisation

### Exécution de la simulation
```bash
python -m simulateur_trafic.main
```

ou

```bash
simulateur-trafic
```

### Personnalisation
Vous pouvez modifier le fichier de configuration `simulateur_trafic/data/config_reseau.json` pour définir vos propres routes et véhicules.

## Architecture

L'application est structurée en plusieurs modules:

### Modèles (models/)
- `Vehicule`: Représente un véhicule avec sa position, vitesse et route actuelle
- `Route`: Représente une route avec sa longueur, limite de vitesse et véhicules
- `ReseauRoutier`: Gère un ensemble de routes interconnectées

### Cœur (core/)
- `Simulateur`: Gère l'ensemble de la simulation
- `Analyseur`: Analyse les résultats de la simulation

### Sortie (output/)
- `affichage.py`: Fonctions d'affichage des statistiques
- `export.py`: Fonctions d'export des données

## Configuration

Le fichier `simulateur_trafic/data/config_reseau.json` permet de configurer le réseau routier initial:

```json
{
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
```

## API

### Vehicule
- `Vehicule(id, position=0, vitesse=0, route_actuelle=None)`: Constructeur
- `avancer(delta_t)`: Fait avancer le véhicule
- `changer_de_route(nouvelle_route)`: Change la route du véhicule

### Route
- `Route(nom, longueur, limite_vitesse)`: Constructeur
- `ajouter_vehicule(vehicule)`: Ajoute un véhicule à la route
- `retirer_vehicule(vehicule)`: Retire un véhicule de la route
- `mettre_a_jour_vehicules(delta_t)`: Met à jour tous les véhicules sur la route

### ReseauRoutier
- `ReseauRoutier()`: Constructeur
- `ajouter_route(route)`: Ajoute une route au réseau
- `retirer_route(nom_route)`: Retire une route du réseau
- `obtenir_route(nom)`: Retourne une route par son nom
- `mettre_a_jour(delta_t)`: Met à jour toutes les routes du réseau
- `obtenir_statistiques()`: Retourne les statistiques du réseau

### Simulateur
- `Simulateur(fichier_config=None)`: Constructeur
- `charger_configuration(chemin_fichier)`: Charge la configuration depuis un fichier
- `lancer_simulation(n_tours, delta_t)`: Lance la simulation