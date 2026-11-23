# Consigne — contre-lecture du brouillon 11 du texte de la base boîte noire (T0.8) — v1

- **Nature** : mandat (classe C) d'une contre-lecture de classe A (R2). **Écrite** le 2026-11-22 par l'auteur du brouillon 11 (modèle B). **Pour** : un sous-agent neuf du modèle A, lancé par la session mère, qui n'a écrit ni ce texte, ni la base (A), ni le code de T0.8, ni leurs relectures.
- **Ce que tu rends** : un rapport scellé, `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon11-cl8-v1.md`, avec un verdict (« scellable après les marqueurs », « scellable après corrections », « non scellable »), tes constats numérotés (bloquant, majeur, mineur) et, pour chaque correction, le texte ancien et le texte nouveau. Tu vérifies ensuite les corrections du rédacteur.

## 1. Ce que tu lis, et rien d'autre

1. `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md` et son compagnon.
2. `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon10.md` (candidat du compte 4) et `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` (gelé ; ligne `GEL-T08`).
3. Le dossier `brouillons/t08-texte-complet-fable-v1/` : programme `faire-t08-brouillon11-v1.py`, textes neufs (`ecrire-textes-neufs-…py` et `.json`), couples, différentiel contre le gel, journal, programme de scellement, consigne de l'alignement du code.
4. `prereg/T0.8-base-A-mots-et-cout-v1.md` (scellé).
5. `registres/scellements-v1.md` : les seules lignes `GEL-T08`, `RUN-CONFIRMATION-T06`, `CODE-MOTS-ET-COUT-T06`, `LECTURE-T08-BASE-A`, `ISSUE-MOTS-ET-COUT-T06` (cherche-les par leur clé) ; `registres/validite-adaptateur-v1.md`.
6. `registres/go.md` : les lignes `GO-2026-11-10-12`, `GO-2026-11-22-79`, `GO-2026-11-22-93` ; `registres/decisions.md` : les lignes R-2265, R-2642, R-2657, R-2778, par leur clé.
7. `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json` ; de `scripts/mots_et_cout_t06_v3.py`, la partie « contrat lu par T0.8 ».
8. `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, section 2.
9. Des branches `calcul/t06-confirmation-7b-v1` et `verdict/t06-mots-et-cout-compte-3-v1` : **les six compagnons `.sha256` seulement** (cinq entrées de 7b, `base-a-t08.json`), par `git show <branche>:<chemin>.sha256`, pour contrôler les empreintes du point 1 du plan.

**Jamais** : un fichier de données, de diagnostic ou de run de 7a, de 7b, de T0.7, de P3-bis ou de la pièce « mots et coût » ; un verdict ; un score de sonde ; T0.7 ou P3-bis ; une pièce du saboteur à budget, du bras A ou du bras d'attaque ; une recherche récursive large dans le dépôt. Un refus d'outil n'est ni rejoué ni contourné : tu t'arrêtes et tu le dis. Avant de commencer, tu envoies ta ligne d'inscription à la liste « qui a lu quoi » à la session mère.

## 2. Ce que tu vérifies

1. **Rejeu.** `python3 brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon11-v1.py --verifier` reproduit le brouillon 11 à l'octet.
2. **Gel.** Par un moyen à toi, indépendant du programme : les sections « Hypothèse » à « Liste d'arrêt » du brouillon 11 sont égales au brouillon 4, hors la ligne T5-19 du point 1 du plan et les valeurs de trois marqueurs. Toute autre différence est un bloquant.
3. **Marqueurs remplis**, chacun contre sa source : la ligne du registre pour `CODE_MOTS_ET_COUT_T06` et `RUN_7B` ; les compagnons pour `EMPREINTES_ENTREES_7B` ; `registres/go.md` pour `GO_T08`. Le code de la course cherchera telles quelles, dans le texte scellé, l'identifiant du run, les cinq empreintes et l'identifiant du GO.
4. **Marqueur rouvert.** Est-il juste de ne pas citer le commit `453a71e1` tel quel ? Les deux écarts de forme dits à la section « Depuis le gel », « Code », sont-ils réels (réserves R-D15 et R-D16) ? La liste de ce que l'alignement peut toucher est-elle assez étroite ?
5. **Section « Depuis le gel du 10 novembre ».** Elle ne doit porter aucun seuil, aucune règle ni aucun critère de lecture neuf. Vérifie en particulier : la déclaration de la référence honnête contre la « Métrique » (tailles 64, 256, 32, 128 ; rang conforme ; horizon 10) et contre la lettre de N-076 ; la table des quatre gardes de code (chacune ne peut-elle vraiment produire que « non lue » ou la ligne D1 ?) ; la concordance avec le brouillon de grille.
6. **Déclaration de vue** de l'auteur du brouillon 11 : complète, sans résultat.
7. **Corrections de renvoi** vers le texte de validité scellé : ne changent rien d'autre.
8. **Calendrier** : tenable ? ce qui manque avant la course.
9. **Programme de scellement** (`finaliser-t08-scellement-v1.py`) : il refuse un texte dont une section gelée a bougé (essaie un cas sain et un artefact, sur une copie hors du dépôt) ; il n'écrase rien.
10. **R3, R4, R7** : aucune ligne ne vise un signe ; aucun chiffre de l'état de l'art.

## 3. Ce que tu ne fais pas

Tu ne proposes aucun changement dans les sections gelées : un défaut que tu y verrais se dit comme un nœud pour Lazar, sans correction. Tu ne remplis aucun marqueur.
