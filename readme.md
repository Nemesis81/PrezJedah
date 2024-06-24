# Projet final Bootcamp Jedah - IPS et résultats des établissement scolaire en France.
    Ce dépot contient les éléments utiliser pour notre présentation de fin de bootcamp [Jedah-Fullstack data Analysis](https://www.jedha.co/formations/data-analysis-fullstack) . Les analyses nécessiteraient plus de recherche pour être completement étayer. L'objectifs ici était de dérouler une méthode.
## Problématique :


l'idée est de donnée une vue global de l'indice de position social des établissement scolaires afin de permettre au personnes qui emmenage dans une ville de selectionner les quartiers qui les interessent. dans un autre temps ceci peux également servir au agence immobilières ou au entreprise d'aider leurs salariés à mieux cibler les quartiers.

# organisation du dépot

- **data** : donnée brut extraites de data.gouv.fr et de data.education.gouv.fr
- **data_cleaned** : données nettoyées et filtrées comme suit :
    -  période de dispo des IPS (2016-2023)
    -  suppression des colonnes non utilisées.
    -  split des "rentré scolaire" en "année de rentrée & "année de diplome".
    -  établissement fermé filtré dans un fichier
    -  suppresion des établissement fermés dans les autres dataset.
- **Dashboard**  : contient le dashboard power-BI
- les divers notebook utilisent les fichier du dépot excepté [cleaning_cal_fonciere.ipynb](cleaningscripte\cleaning_val_fonciere.ipynb) qui point directement sur data.gouv . il est tout a fait possible d'utiliser la même méthode pour l'ensemble des donnée sources.


#### Sources
- [Valeur fonciere](https://www.data.gouv.fr/fr/datasets/r/78348f03-a11c-4a6b-b8db-2acf4fee81b1)
- [effectifs Ecole](https://www.data.gouv.fr/fr/datasets/effectifs-deleves-par-niveau-et-nombre-de-classes-par-ecole-date-dobservation-au-debut-du-mois-doctobre-chaque-annee/)
- [Enseignement Professionnel](https://www.data.gouv.fr/fr/datasets/r/35f7bef7-48fc-48d5-9c0f-ed59be504e05-)
- [Enseignement Général et Technologique](https://www.data.gouv.fr/fr/datasets/r/7580d6d2-a7bb-4cbb-a78f-5dbaa1891cc4)
- [source 2016-2021 ips colleges](https://www.data.gouv.fr/fr/datasets/r/b63bd365-c589-48e4-b7d8-9e4f5db133c5)
- [source 2022](https://www.data.gouv.fr/fr/datasets/r/28e511a7-af0d-48c7-a8bb-2f38ec003f49)
- [IPS écoles](https://www.data.gouv.fr/fr/datasets/indices-de-position-sociale-dans-les-ecoles-a-partir-de-2022/")