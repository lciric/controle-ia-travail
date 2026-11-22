# Différences : texte de relance courte de 61875617, brouillon 4 vers brouillon 5 ; script v3 vers v4 (une ligne par correction)

- A1 : la liste du contenu de l'archive est lue par l'entrée standard (`cat … | tar -tvf -`), avec son code ; le nombre d'entrées doit égaler celui des chemins (`find`).
- A2 : plus de tâche de fond ni de `sleep 1` ; l'empreinte de l'archive entière est calculée sur le réassemblage, et le réassemblage est comparé octet par octet aux sources (`tar --compare`, seules les différences de date et de propriétaire admises).
- L1 : l'état est relu après `lister` ; machine en marche → arrêt par l'identifiant, code 1 ; état illisible → mot de la mère.
- L2 : une commande `execute` en échec est rejouée une seule fois.
- E1 : `archiver` ne prend que les traces ajoutées par la relance (lues dans `diff-name-status.txt`).
- N9 : le texte dit qu'aucun moyen sûr n'existe (refus de la mère consigné) et énumère ce qui reste à trancher par Lazar.
- Branche cloisonnée : nom confirmé par la mère.
- Essais : tous rejoués sur le script v4 (`essais-blanc-relance-courte-v4-rejeu2.txt`) ; deux rejeux intermédiaires en échec sont conservés.
