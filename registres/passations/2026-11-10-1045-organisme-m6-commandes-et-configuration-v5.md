# Organisme, plus petite course réelle de la boucle : pièce M6 faite (commandes v6 versées, configuration v5) — 10 novembre 2026

Session `session_01QPDgKgcLdggoVJfGC5cBw8` (session-dépôt), en autonomie. Numéro de registre à attribuer à la fusion dans
`main`.

- **Mot direct de Lazar dans cette session, verbatim** : « M6 oui, M0 oui ; […] : go ». Demande d'origine : session
  « attaquant informé » (`session_01QPDgKjN3jeeUyZP2mnkDNK`), message de 10:18 UTC, qui renvoie au préenregistrement en
  brouillon de la course (`docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon1.md`,
  `736e3fd6…`, branche `claude/compassionate-meitner-d4ryyk`, section 12 : M6 et M0 « session de dépôt »).
- **Autorisation de dépense de la course** : GO-2026-11-08-02 sur `main` (45 USD : 40 pour les modèles, 5 pour la machine ;
  échéance 30 novembre ; « après le code v65 contre-lu, la machine à bac à sable `bwrap` et le préenregistrement scellé »).

## M6, fait

1. **Commandes v6 versées dans l'arbre**, telles quelles, depuis `outils/commandes-tour-ferme-v1` (tête `12f9e0e3`, R-1129 :
   contre-lecture v6 « scellable telle quelle ») : 90 fichiers sous `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`,
   tous des ajouts par rapport à `main` ; 45 compagnons vérifiés conformes (35 + 5 + 5). Les deux commandes sont celles que
   nomme la configuration v4 : `commande_kimi_v6.py` (`889309…`) et `commande_argon_v56_nuit_v6.py` (`5eae1a…`).
2. **Configuration v5** : `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/configuration-tour-ferme-v5.json`, scellée.
   Copie de la v4 (`15b34adf…`) écrite par programme ; différences, vérifiées clé par clé : `budget.plafond_usd` 50 → 40 ;
   `--plafond-cumule-usd` des deux commandes 50 → 40 (garde cumulée des deux fournisseurs sur le même registre : les parts
   Kimi 33 et Argon 7 sont un plan, comme les parts 44 et 6 de la v4) ; texte de présentation. Toutes les autres clés sont
   identiques.
3. **Laissé au préenregistrement de la course et au code v65** (signalé dans la configuration) : la racine des graines
   (20261102, reprise de la v4), les chemins sur la machine jetable (ceux de la v5 sont ceux de ce conteneur), les montants par
   étape (repris de la v4).

## M0, en attente

Machine jetable avec `bwrap` ≥ 0.9 et utilisateur dédié, essai à blanc `--bac reel` rejoué dessus, 5 USD sous
GO-2026-11-08-02 : **seulement après le code v65 contre-lu**, comme l'autorisation l'exige. Ce conteneur n'a aucun outil de
location de machine : le fournisseur et l'accès sont à préciser avant l'exécution.

## Instances actives

Aucune. Aucune dépense.
