# Projet final Bootcamp Jedah - IPS et résultats des établissement scolaire en France.

## Problématique :

### contexte :

l'idée est de donnée une vue global de l'indice de position social des établissement scolaires afin de permettre au personnes qui emmenage dans une ville de selectionner les quartiers qui les interessent. dans un autre temps ceci peux également servir au agence immobilières pour mieux cibler les quartiers pour leurs clients.

# organisation du dépot

- data : donnée brut extraites de data.gouv.fr et de data.education.gouv.fr
- data_cleaned : données nettoyées et filtrées comme suit : 
  - période de dispo des IPS (2016-2023)
  - suppression des colonnes non utilisées
  - split des "rentré scolaire" en "année de rentrée & "année de diplome"
  - 