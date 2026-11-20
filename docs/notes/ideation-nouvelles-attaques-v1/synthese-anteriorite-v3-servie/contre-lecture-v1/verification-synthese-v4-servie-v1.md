# Vérification — synthèse d'antériorité servie v4 — v1

Pièce de travail (classe C), écrite le 2026-11-20 par le même contre-lecteur que la contre-lecture de la v3 (`contre-lecture-synthese-v3-servie-v1.md`, `a9cdf12c…`), sur le message du coordinateur. Mêmes interdits que le mandat `a317b9ef…`. Processeur seul ; aucune écriture dans le dépôt ; aucun refus de permission, de classifieur ni de garde (un refus de l'outil de remplacement sur mon propre fichier d'essai, voir § 6).

## 0. Verdict

**À corriger**, sur deux points légers, qui suivent la décision de la mère de retirer la provenance des refus. Les décisions de la mère (C1 « plusieurs », C2, section 8.1 et table retirées) sont appliquées exactement, sans rien toucher d'autre. Deux traces restent : « Zero refus » à la ligne 4, et une numérotation qui saute de 8 à 8.2. Les trois remplacements du § 4 appliqués : conforme, à sceller.

## 1. Pièces

- `synthese-anteriorite-pilier-attaque-v4-servie.md` (`939aa84a3f66647e6fe3f08bf80134e3d08f9b1408ac0e61d12ddd3fecb3830b`), `remplacements-synthese-v3-v4-servie-v1.json` (`07cbff7401b215313b05b1271ac78070c0173cc07403829562d23485020b74ab`) et le journal de l'outil : « OK » contre leurs compagnons.
- Différentiel (`c5eea6fa…`), relevé (`e273d5f6…`), rapport (`193fdf1d…`) : **non vérifiés**. Le message ne donne pas leurs noms, et la consigne interdit de lister le dossier. J'ai refait le différentiel moi-même (§ 2).

## 2. Rejeu

L'outil (`391db990…`), lancé sur la v3 (`7aa7750d…`) avec le JSON : « FAIT : 4 remplacement(s) », sortie `939aa84a…`. `cmp` avec la v4 : identiques. Le JSON, relu en entier, ne contient que C1 (neuf « de plusieurs fabricants differents »), C2, le retrait de la section 8.1 (titre, deux paragraphes et ligne vide qui suit) et le retrait du séparateur, du titre et de la table des corrections. Mon `diff -u` v3 → v4 ne montre que ces quatre changements.

## 3. Relevé et lecture

- **Mon programme** (`releve_contre_lecture_v3_servie_v1.py`, inchangé, `70abe49a…`), relancé sur la v4 : sortie `sortie-releve-contre-lecture-v4-servie-v1.txt`. Le programme écrit « v3 » dans ses en-têtes : ces en-têtes désignent ici la v4.
  - Motifs du mandat : **0**.
  - Noms d'espèces et de fournisseurs : **0**.
  - Noms de règles, identifiants, accents graves, http, extensions de fichiers, courriels : **0**.
  - « v2b », « entretien », « directeur », « registre » : **0**.
  - Caractères non ASCII : guillemets et un « é ». Tous les mots à majuscule initiale sont neutres ou publics.
  - Les lignes 118 à 151 (références) et 159 à 176 (combinaison) n'ont pas changé.
- **Lecture entière par le sens** (286 lignes) :
  - C1 se lit bien, et « plusieurs » ne contredit pas « quatre lignees » de la ligne 5. C2 se lit bien.
  - Restent seulement « session mere » (ligne 284, l'avertissement, déjà « sans suite »), ainsi que « T100 », « G1 », « W2 » et les autres termes des cellules.
  - Plus aucun « refus », « classifieur », « pre-vol » ni plafond, hors de « Zero refus » (ligne 4). Les « refusent de chiffrer » des lignes 224 et 246 sont du fond.
- **Bornes des deux retraits** :
  - La section 7 se termine par « --- », vient ensuite « ## 8. … », une ligne vide, puis « ### 8.2 » : la coupe est propre.
  - Le fichier finit à l'avertissement, par un seul saut de ligne. Il ne reste ni séparateur orphelin ni ligne vide en trop.
  - Aucun renvoi aux sections 8.1, 8.2 ou 8.3 ailleurs dans le texte, vérifié par `grep -n -F -e "8."` sur ce seul fichier.

## 4. Corrections (Ancien → Neuf, texte exact de la v4)

Chaque ancre est comptée à 1 par `grep -c -F -e`. L'essai par l'outil sur une copie dans mon dossier rend « FAIT : 3 remplacement(s) », sortie `f74c6064…`.

- **D1 (l. 4)** — Ancien : ` Zero refus.` (avec l'espace qui précède) — Neuf : (vide). Ce mot est de la même nature que la section 8.1 retirée : la provenance des refus des espèces. Il ne sert pas à éprouver une antériorité. Le garder montre que les refus sont suivis.
- **D2 (l. 256)** — Ancien : `### 8.2 Passage de trois a cinq especes` — Neuf : `### 8.1 Passage de trois a cinq especes`.
- **D3 (l. 268)** — Ancien : `### 8.3 Changements de fond` — Neuf : `### 8.2 Changements de fond`.

D2 et D3 se justifient ainsi : une section 8 qui commence à 8.2 laisse voir qu'une partie a été coupée. Aucun renvoi interne ne dépend de ces numéros. Le titre « ## 8. » et la section 2 citée en 8.2 point 3 restent tels quels.

## 5. Ce qui ne change pas

Aucune idée, antériorité ni référence publique ne change de sens, ni de la v3 à la v4, ni par D1 à D3.

## 6. Écarts

- Le différentiel, le relevé et le rapport de la mère ne sont pas vérifiés par leurs empreintes : leurs noms ne sont pas donnés, et la consigne interdit de lister le dossier.
- Mon premier fichier d'essai (`corrections-proposees-v4-servie-v1.json`) a été refusé par l'outil de remplacement, sur sa propre règle 5 : le texte neuf était contenu dans l'ancien. Ce n'est pas un refus de permission, de classifieur ni de garde. Je l'ai remplacé par `corrections-proposees-v4-servie-v2.json` (D1 en suppression), accepté. Le v1 reste dans mon dossier, sans usage.

— contre-lecteur neuf, modèle O
