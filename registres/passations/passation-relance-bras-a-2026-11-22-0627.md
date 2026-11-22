# Passation — relance du bras A des organismes discrets — 2026-11-22T06:27:39Z

Session fille de la mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1` (qui passe la main à une nouvelle mère sur un nouveau compte). Branche **`claude/pensive-bardeen-1fv7hw`**. Suit `passation-relance-bras-a-2026-11-21-2335.md`. Le journal `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` fait foi jusqu'à OD-351.

## 1. Fait depuis la passation de 23:35Z
- **Livraison 10** (`_v9`) : refus si `outputTokenLimit` est absent ; GO de l'exemption lu au registre. Vérifiée conforme (573 mutants tués sur 573), OD-344.
- **Exemption de la sonde** : GO-2026-11-22-03 (Lazar), remplace GO-88 (refusé : colonne « par », majuscule).
- **Limites de mots du juge** (lecteur habilité, R-4748) : 300 et 300 mots, 5,1 jetons par mot. Lecture de la mère retenue ; le lecteur avait dit « ne tient pas » faute de limite en mots (OD-342).
- **GO-2026-11-22-02** (aucun versement chez Google, la recharge couvre) et **GO-2026-11-22-16** (« oui, seuils levés »).
- **Avenant 3 v2** : seuils de crédit de Google levés. Écrit par Opus, relu par Fable par l'API (1,70 USD), accepté (R-4765), 4b331d9a….
- **Livraison 11** (`_v10`) : seuils levés, refus pour crédit épuisé. Contre-lue par un Opus neuf (OD-351) : **C-1 bloquant**, un 429 de débit de Google est indiscernable d'un crédit épuisé ; C-2, la garde 8 n'exige ni l'avenant 3 ni GO-16 ; C-3, levée trop large.

## 2. En cours à l'écriture
**Livraison 12** (`_v11`), chez l'agent Opus du code de cette session : fichiers `_v11` et mutations v7 présents, **non suivis, non scellés**. Règle retenue :
- un 429 suit le devis (attente, une seule reprise) ;
- un second 429 sur le même appel arrête la ligne ;
- un 402 l'arrête aussitôt ;
- le faux fournisseur rend un 429 à la forme réelle de Google ;
- la garde 8 exige l'avenant 3 (4b331d9a…) et GO-16 ;
- levée sous GO-02 seulement.

**Si cette session s'arrête avant son rendu, la session suivante ne reprend pas ces fichiers :** elle relance la livraison 12 sur les `_v10` scellés, consigne d'OD-351.

## 3. Reste
1. Livraison 12 : rendu, essais rejoués, scellement, vérification par l'Opus neuf de la livraison 11 (ou un autre neuf).
2. **Constat de Google neuf** (forme de la note v11) : soldes vus de Lazar, ou, à défaut, les captures de 2026-11-21T16:24Z (11,93 € et 15,59 €, recharge activée, 0 € d'autres crédits), citées avec leur heure. Taux de la Banque centrale européenne : **le fixage du 20 novembre expire pour 96 heures le 24 novembre vers 14:00Z** ; relever le fixage du lundi 23.
3. **Trois lignes courtes au registre** : vérification de la clé 1, vérification de la clé 2, file du juge. Elles citent l'avenant 2 v3, l'avenant 3 v2, GO-16 et les empreintes du devis. Puis la configuration définitive, depuis le gabarit v11.
4. **Lancements** : vérification de la clé 1, de la clé 2, puis la file du juge (8 lectures, partage par rang), et application des règles.
5. **Brouillon final du texte** (Fable par l'API, effort `high`, plafond 6 USD sous la mère) : Mistral admis, le juge, les trois pièces habilitées ; puis la contre-lecture 10, le scellement, la course.

## 4. Ce qui attend Lazar
- Ses **soldes Google vus**, avec page et heure, et le lien entre chaque clé et chaque projet (sinon, les captures d'hier).
- Rien d'autre ne bloque de son côté.

## 5. Réserves
- Liste locale des interdits **hors dépôt** (`/home/user/hors-depot/essais-admission-bras-a-v1/interdits-v1.txt`) : à refaire dans tout conteneur neuf avant une ligne.
- Fichier de 10 octets `/file-mistral.pid` à la racine.
- Les verrous `runs/essais-admission-*.verrou` sont exclus localement (`.git/info/exclude`).

## 6. Ce qui tourne ; instances
L'agent Opus du code (livraison 12) seulement. Aucune instance de calcul, aucun appel payant en cours.
