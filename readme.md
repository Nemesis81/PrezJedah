# Projet final Bootcamp Jedah - IPS et résultats des établissement scolaire en France.
## Problématique :
### contexte :
l'idée est de donnée une vue global de l'indice de position social des établissement scolaires afin de permettre au personnes qui emmenage dans une ville de selectionner les quartiers qui les interessent. dans un autre temps ceci peux également servir au agence immobilières pour mieux cibler les quartiers pour leurs clients.

# organisation du dépot
- data : donnée brut extraites de data.gouv.fr et de data.education.gouv.fr
- data_cleaned : données nettoyées et filtrées comme suit :
    -  période de dispo des IPS (2016-2023)
    -  suppression des colonnes non utilisées
    -  split des "rentré scolaire" en "année de rentrée & "année de diplome"
    - 
#### Sources
https://data.education.gouv.fr/explore/dataset/fr-en-ips_ecoles_v2/information/?disjunctive.academie&disjunctive.code_du_departement&disjunctive.departement&disjunctive.uai&disjunctive.code_insee_de_la_commune&disjunctive.nom_de_la_commune&disjunctive.secteur

https://data.education.gouv.fr/explore/dataset/fr-en-ecoles-effectifs-nb_classes/information/?disjunctive.rentree_scolaire&disjunctive.region_academique&disjunctive.academie&disjunctive.departement&disjunctive.commune&disjunctive.numero_ecole&disjunctive.denomination_principale&disjunctive.patronyme&disjunctive.secteur&disjunctive.code_postal&sort=tri
