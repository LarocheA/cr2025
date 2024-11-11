# Logiciel de Suivi de Cryptomonnaies et Analyse de Portefeuille

## Description du projet
Ce projet sous Python est conçu pour suivre les cours des cryptomonnaies et gérer un portefeuille d'investissement. Il permet aux utilisateurs de récupérer des données en temps réel, de gérer leurs transactions, et d'analyser la performance de leur portefeuille.

## Fonctionnalités
- Récupération des données de cryptomonnaies en temps réel
- Gestion de portefeuille (ajout/suppression de transactions)
- Analyse de performance et calculs financiers
- Interface utilisateur en ligne de commande (CLI)
- Visualisation des données et graphiques

## Introduction
 

## 1. Structure du projet
crypto_portfolio/               Fichiers racine
│
├── main.py                 --> Point d'entrée principal de l'application.
├── config.py               --> Fichier de configuration pour stocker les constantes et les paramètres globaux.
│
├── data/                       Module data
│   ├── init.py
│   ├── crypto_data.py      --> Gère la récupération et le stockage des données de cryptomonnaies.
│   └── api_client.py       --> Contient les fonctions pour interagir avec les API externes (ex: CoinGecko, Binance).
│
├── portfolio/                  Module portfolio
│   ├── init.py
│   ├── portfolio.py        --> Définit la classe Portefeuille et ses méthodes.
│   └── transaction.py      --> Gère les transactions (achats, ventes) dans le portefeuille.
│
├── ui/                         Module ui
│   ├── init.py
│   ├── cli.py              --> Implémente l'interface en ligne de commande.
│   └── gui.py              --> Implémente l'interface graphique.
│
├── analysis/                   Module analysis
│   ├── init.py
│   ├── calculations.py     --> Contient les fonctions pour les calculs financiers (ex: ROI, performance).
│   └── visualization.py    --> Gère la création de graphiques et de visualisations.
│
└── utils/                      Module utils
    ├── init.py
    └── helpers.py          --> Fonctions utilitaires utilisées dans tout le projet.

## Installation
Instructions pour installer le projet et ses dépendances.

## Utilisation
Exemples d'utilisation du logiciel.

## Développement
Instructions pour configurer l'environnement de développement et contribuer au projet.

## Licence
Informations sur la licence du projet.

## Auteur
Arthur Laroche et informations de contact.
