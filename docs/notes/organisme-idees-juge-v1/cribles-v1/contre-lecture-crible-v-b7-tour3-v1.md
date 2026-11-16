# Contre-lecture du crible (v), brouillon 9 (tour 3 de la boucle B7) — lecteur C

Lecteur : modèle C, neuf (n'a écrit aucune pièce). Pièce : `crible-v-brouillon9.md`, empreinte `c574e39d700aaff64c59efd0319aaf565c906ff2518304c6c2f2a752dcd5da23` (égale à son compagnon). Précédente : `crible-v-brouillon8.md`, `8047040ba7b8268ac26e20a41406a71fa72e474ca303e9e60e1c686a55153d82` (égale à son compagnon). Rapport corrigé : `contre-lecture-crible-v-b7-tour2-v1.md`, `b41f7124a48ed8815907a984e8c07c0466924f56fe75f2e85be210a284904206` (égale). Lecture du 2026-11-16, 15:31Z à 15:33Z (`date -u`). Rien lu sous `diag/`, `runs/`, `donnees/` ; aucun appel, aucune dépense, aucun fichier existant modifié.

## Verdict : **scellable**. Aucune correction exigée ; aucune remarque facultative nouvelle.

## 1. Application des corrections du tour 2 : fidèle
- `diff brouillon8 brouillon9` : 8 zones, toutes expliquées : titre, entrée d'en-tête « Brouillon 9 », statut, ligne du validateur, phrase de la section « Taille » (C8-02), ligne d'arrêt « fournisseur abandonné » (C8-01), tête de la section « Contre-lecture » (tours 1 à 8), entrée « Contre-lecture 8 » (C8-03). Rien d'autre.
- Les deux couples C8-01 et C8-02, extraits par programme du rapport : chaque « ancien » présent une fois dans le brouillon 8 et absent du brouillon 9, chaque « nouveau » absent du brouillon 8 et présent une fois dans le brouillon 9. Mot pour mot.
- C8-03 : l'entrée « Contre-lecture 8 » porte les deux empreintes entières, exactes (rapport du tour 2, brouillon 8), les heures 15:25Z à 15:30Z du lecteur précédent, le verdict et les comptes ; titre, en-tête, statut (« contre-lu huit fois ») et tête de section mis à jour.
- Programme `appliquer-corrections-crible-v-brouillon9.py` : empreinte égale à son compagnon.
- `controle_ia.prereg.problemes` sur le brouillon 9 : liste vide. Aucun identifiant de modèle (seules les clés de configuration gelées `opus55` et `fable52` de la table de prix, déjà déclarées dans la pièce).

## 2. Vérifications refaites sur les passages touchés
- Ligne d'arrêt « fournisseur abandonné » : essai sain (panne de relais d'un appel d'un fournisseur ayant déjà répondu, minimum encore possible : on continue) et artefact (premier appel sans réponse ; ou panne simulée au monde 3 rendant le minimum impossible : arrêt) sont maintenant justes sous la règle du pilote et la définition du monde complet ; chacun tire. R5 tenue. La seule autre occurrence de l'ancien artefact est dans l'entrée historique « Contre-lecture 8 » (citation de l'ancien texte), sans effet.
- Phrase de la section « Taille » : dit que la grille suppose des appels indépendants et ne compte pas l'abandon ; la probabilité d'aller au terme est dite plus basse, non chiffrée. Cohérente avec l'annexe A, point 11 (0,75 à 0,9985 inchangés).
- Rien de touché aux critères, seuils, graines, devis (204,67 USD au pire, inchangé), durée ni décisions de R-2992.

## 3. Points déjà tenus (non rejoués)
R1 complet, R3, N-058 borné, partie A descriptive, devis et part sur crédits, durée par monde (code et configuration neufs, ce qui fixe la date de lancement), graines par `SeedSequence`, antériorités à chercher : inchangés depuis le tour précédent, rien dérangé.

## 4. Remarques facultatives (déjà transmises, ouvertes)
F-B8-1 (ligne « fournisseur sans aucun appel répondu après les trois premiers mondes ») et F-B7-1 à F-B7-6 : restent ouvertes, au choix de la mère ; elles ne bloquent pas le scellement.

## 5. Incidents
Aucun. Pas de `pytest`, aucun fichier existant modifié ; une première exécution de `problemes` a imprimé par erreur le contenu de la pièce dans ma sortie (aucun effet).

## 6. Points pour la mère
1. Règle d'abandon du pilote (une panne passagère au premier appel d'une voie termine le crible à l'étage 1) : une règle plus tolérante demanderait un mot avant scellement ; non inventée ici.
2. Enveloppe : 204,67 USD au pire pour ce crible ; cumul des cinq à refaire avant toute ligne « calcul » (R-2992 point 3, GO-2026-11-15-06, 1 275 USD).
3. Les corrections de ce tour ayant été appliquées sans écart, la pièce peut être scellée telle quelle ; le lancement reste conditionné au code et à la configuration neufs de la concurrence des relais et à un GO.
