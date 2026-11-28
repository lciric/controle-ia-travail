# Versement des travaux non commis de la session mère Gemini — 2026-11-28 — v1

- **Provenance** : texte transmis par Lazar dans la session Claude Code session_01QPDgKfh86KrPUDxcz8M1GQ, le 2026-11-28 vers 10:45Z (« dernieres avancees de gemini qui n'avait pas commit »). Versé tel quel (règle « récupérer ce qui est récupérable »), sans retouche.
- **Fichiers** :
  - `versement-gemini-non-commis-20261128-v1.md` : le texte entier, à l'octet près ;
  - trois extraits tirés par programme, chacun sous-chaîne exacte du versement entier :
    - `arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md` : texte intégral des trois nœuds, avec options, recommandations et arbitrages de Lazar ;
    - `G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md` : brouillon de l'additif au critère 3, partie (i), de la porte G0 (micro-course furtive) ;
    - `G1-architecture-h1-h2-v1-brouillon-gemini-1.md` : brouillon du préenregistrement de la porte G1 (H1 et H2).
- **Statut** : brouillons non scellés comme préenregistrements, ni contre-lus sous leur forme actuelle. Ils servent d'objet au pré-mortem demandé par Lazar (« contrelire le prereg et les decision »), puis d'entrée au rédacteur Fable neuf (règle « Qui conçoit »). Les textes en vigueur sous `prereg/` seront ceux que ce rédacteur écrira, après la contre-lecture à froid (R2).

## Constats mécaniques de la mère (programme, sans jugement de fond)
1. `controle_ia.prereg.problemes` rend `[]` sur les deux brouillons. Ce validateur ne contrôle que les titres, les marqueurs restants et deux empreintes par contre-lecture.
2. **Références** : sur les 42 empreintes citées, une seule est fausse. Pour la contre-épreuve, les textes citent `59a2a571c687…`, introuvable dans le dépôt ; le fichier versé par Lazar, `registres/contre-lectures/contre-epreuve-r2-volets-11-13-20261128-v1.md`, a pour empreinte `8547ee1c332b1551bcf7d0d6a0ec3791fd1b5e97fef456c6236ebd73b17bf8e6`.
   - Huit autres empreintes ne figurent que dans `src/controle_ia/versant_honnete_passe_v2.py` et `v3.py` (fichiers du modèle, poids de sondes et planchers épinglés). Elles n'ont pas été recalculées : la garde P8 interdit d'ouvrir les poids.
3. **Chemins** : les rapports sont cités sans chemin ni date (`contre-lecture-r2-etages-1-2-v1.md`, `contre-epreuve-r2-volets-11-13-v1.md`). Les fichiers du dépôt sont `registres/contre-lectures/…-20261128-v1.md`.
4. **Écart avec la ligne GO-2026-11-28-01 du registre** (texte de la passation, § 4.1) : le registre porte « arrêt si > 3/N_ep ou écart > 2/N_ep ». Le texte de Gemini porte « > 3/128 » et « > 2/128 » sur 256 épisodes par condition, soit 6 et 4 reprises en nombre. À trancher par Lazar.
5. **Doses** : le brouillon G0 inclut `gonfle_2` comme cinquième condition (12 800 actions). La ligne du registre porte « (-> gonfle_2 si inclus) ». Inclusion et plafond (8 USD, 3 h) sont à vérifier ensemble.
6. **Sections « Contre-lecture »** : elles citent la contre-lecture R2 des Livrables 1 et 2 et la contre-épreuve, c'est-à-dire des pièces amont, et non une contre-lecture de ces deux textes. La contre-lecture R2 de ces textes reste à faire.
7. **Mise en forme** : la copie depuis une vue rendue a laissé des traces (gras et chasse fixe mêlés, par exemple `R10**` ; lignes « | » isolées après certains tableaux).
