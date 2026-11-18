# Différences du brouillon 4 au brouillon 5 — ordre exploratoire et devis du saboteur à budget (ii-b) — v1

- **Statut** : brouillon, scellé comme brouillon, non contre-lu. Écrit le 2026-11-18 vers 21:30 UTC (`date -u`) par le rédacteur neuf du brouillon 5 (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, mandat `docs/notes/barreau8-iib-v1/mandat-redacteur-ordre-exploratoire-iib-v1.md`, `55b1e348…f98d`).
- **Fabrication** : `appliquer-brouillon5-ii-b-v1.py` (ce dossier, scellé). Chaque « avant » ci-dessous est présent exactement une fois dans le texte au moment de son application ; tout le reste est recopié à l'octet. **Contrôle de recopie** : chaque « après » est présent exactement une fois dans le texte final, et l'application inverse, dans l'ordre inverse, rend le brouillon 4 à l'octet (vérifié par le script avant écriture).
- **Pièces** :
  - ordre : brouillon 4 `ordre-exploratoire-ii-b-v1-brouillon4.md` (`91a592ff776efd4a9cf2293cfee2a837a25b4bee6d33fcff087662cbf2f715c8`) → brouillon 5 `ordre-exploratoire-ii-b-v1-brouillon5.md` (`73bc2781d79e69d33d0a0949c01f3861a74ff2e0c3ac6d74ac0dcee88068b223`) ;
  - devis : brouillon 4 `devis-ii-b-v1-brouillon4.md` (`08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`) → brouillon 5 `devis-ii-b-v1-brouillon5.md` (`8ee9ead15fb5feadbffc41ffb3cd8d9abe8a8fc1d82b588f2957de93405e7e32`).
- **Accords appliqués** (ces seules lignes lues) : `registres/go.md`, `GO-2026-11-18-55` (activité interne, branche B) et `GO-2026-11-18-56`, points 3 (nœuds 2 (a), 3 (a), 4 (B), 5 (a), 6 (b) de `noeuds-ii-b-pour-lazar-v2.md`, `be431ed5…7207`) et 4 (portage de la base textuelle : recommandations de `docs/notes/barreau8-iib-v1/releve-code-des-deux-bases-v1.md`, `601bbc84…2034`) ; registre des décisions, `R-3435`.
- **Compléments du contrôle court** (`docs/notes/barreau8-iib-v1/controle-court-code-iib-v3-v1.md`, `02962a4a…c3a2`, § 4 et § 6) : ordre, changements O14, O22, O29, O30, O31, O33.
- **Devis** : aucun chiffre ne change ; calcul v3 rejoué, sortie identique à l'octet ; aucun calcul sous nom neuf.
- **Marqueurs** : comptés par `compter-marqueurs-ii-b-v1.py` (ne cherche que le motif `<<[A-Z0-9_]+>>`), sortie `sortie-compter-marqueurs-ii-b-v1.txt`, scellés dans ce dossier. Ordre brouillon 4 : 18 distincts ; ordre brouillon 5 : 16 distincts (retirés : `MOT_LAZAR_ACTIVITE_INTERNE_IIB`, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB` ; ajouté : `FORMAT_ACTIONS_PORTAGE_IIB`). Devis brouillon 4 : 9 distincts ; devis brouillon 5 : 8 (retiré : `MOT_LAZAR_ACTIVITE_INTERNE_IIB`, rempli dans la ligne d'engagement).
- **Points ouverts portés à la mère** : (1) la forme de la ligne de création de 7b (contrôle court, § 6, point 3) ; (2) CC-02 à CC-05, souhaitables avant la course ; (3) si les essais du jetoniseur réel deviennent des arrêts joués par l'amorce (le nœud 3 ne le dit pas) ; (4) l'issue de la vérification du format des actions pour le portage (marqueur neuf) ; (5) le nombre de tirages et de permutations de la lecture (2), indéterminé d'après le relevé ; (6) l'inscription de la branche `prep/iib-code-v2` au registre « qui a lu quoi » et son exclusion de la copie publique ; (7) la question de la copie publique sur `donnees/*-iib-*` (§ 7, inchangée).

## Devis (`devis-ii-b-v1-brouillon5.md`) : 13 changements

| changement | où | raison |
|---|---|---|
| D1 | titre | version du texte |
| D2 | statut | version du texte (R12) |
| D3 | statut, auteur du brouillon 4 | distinguer l'auteur du brouillon 4 de celui du brouillon 5 |
| D4 | statut, brouillon 5 | fabrication et arithmétique du brouillon 5 |
| D5 | § 0 | branche B tranchée par Lazar ; nœuds de la note v2 tranchés |
| D6 | § 6 | nœud 4 tranché (B) |
| D7 | § 7, ligne « création » | nœud 2 tranché (a) |
| D8 | § 8.1, titre | branche B retenue |
| D9 | § 8.1, ligne « lettre de la ligne » | mot exprès donné |
| D10 | § 8.1, après la table | la colonne A n'est plus qu'un rappel |
| D11 | § 8.2, passe préalable des épreuves | nœud 3 tranché (a) |
| D12 | § 8.3 (neuf) | la passe de recalcul décrite comme une course à part |
| D13 | § 9, ligne d'engagement | branche connue ; passe hors de la ligne |

### D1 — titre

Avant :

~~~text
# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 4
~~~

Après :

~~~text
# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 5
~~~

### D2 — statut

Avant :

~~~text
- **Statut** : **brouillon 4**, scellé comme brouillon, non contre-lu. Brouillon 3 (`devis-ii-b-v1-brouillon3.md`, `016979ba01926f08be8ac243df75b716cf49ea63ea01e16dedd4302e61f991d4`) intact (R12).
~~~

Après :

~~~text
- **Statut** : **brouillon 5**, scellé comme brouillon, non contre-lu. Brouillon 4 (`devis-ii-b-v1-brouillon4.md`, `08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`) et brouillon 3 (`devis-ii-b-v1-brouillon3.md`, `016979ba01926f08be8ac243df75b716cf49ea63ea01e16dedd4302e61f991d4`) intacts (R12).
~~~

### D3 — statut, auteur du brouillon 4

Avant :

~~~text
- **Écrit** le 2026-11-18 vers 20:05 UTC (`date -u`) par le même rédacteur neuf que le brouillon 3
~~~

Après :

~~~text
- **Brouillon 4 écrit** le 2026-11-18 vers 20:05 UTC (`date -u`) par le même rédacteur neuf que le brouillon 3
~~~

### D4 — statut, brouillon 5

Avant :

~~~text
## Traitement des remarques de la contre-lecture
~~~

Après :

~~~text
- **Brouillon 5** : écrit le 2026-11-18 vers 21:30 UTC (`date -u`) par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, même mandat), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons 1 à 4, et n'a pas ouvert la consigne privée. Fabriqué par programme depuis le brouillon 4 (`appliquer-brouillon5-ii-b-v1.py`, scellé dans ce dossier), recopié à l'octet hors des changements listés dans `differences-brouillon4-vers-5-v1.md`. Il porte les choix de Lazar du 2026-11-18 (`registres/go.md`, lignes `GO-2026-11-18-55` et `GO-2026-11-18-56`, points 3 et 4 ; registre des décisions, ligne `R-3435` ; ces seules lignes lues). **Aucun chiffre ne change** : le calcul v3 a été rejoué (`.venv/bin/python -I -B calcul-devis-ii-b-v3.py`), sortie identique à l'octet à `sortie-calcul-devis-ii-b-v3.txt` (`8eecd277…8bd8`) ; aucun calcul sous nom neuf.

## Traitement des remarques de la contre-lecture
~~~

### D5 — § 0

Avant :

~~~text
Les deux branches sont chiffrées au § 8 ; le choix est à Lazar, par un mot exprès (note des nœuds, point 1).
~~~

Après :

~~~text
Les deux branches sont chiffrées au § 8.1. **Lazar a choisi la branche B** (« garder de quoi recalculer ») par son mot exprès : `registres/go.md`, ligne `GO-2026-11-18-55`, confirmée au registre des décisions, ligne `R-3435`, verbatim : « Ou veux-tu la recalculer plus tard sur une location à part (branche B : aucun code ne change, environ 4,2 à 4,7 dollars plus tard, résultat égal aux arrondis près) go ». La course n'enregistre rien ; on garde les textes exacts des actions et les deux adaptateurs ; l'activité se recalcule plus tard par une passe à part, avec son devis et sa ligne à part (§ 8.3). Les autres points de la note `noeuds-ii-b-pour-lazar-v2.md` (`be431ed5…7207`) sont tranchés par `GO-2026-11-18-56`, point 3 : nœuds 2 (a), 3 (a), 4 (B), 5 (a), 6 (b).
~~~

### D6 — § 6

Avant :

~~~text
**La ligne inscrite correspond à la variante B.** Recommandation du rédacteur : B, confiance haute (note des nœuds, point 4 ; sans mot de Lazar, rien ne change).
~~~

Après :

~~~text
**La ligne inscrite correspond à la variante B.** **Variante B retenue** : nœud 4 (B) de la note v2, tranché par Lazar (`GO-2026-11-18-56`, point 3).
~~~

### D7 — § 7, ligne « création »

Avant :

~~~text
| création | **jamais avant la création de 7b** (ligne du registre exigée par le code) | code v3 |
~~~

Après :

~~~text
| création | **jamais avant la création de 7b** (ligne du registre exigée par le code) ; si 7b n'est pas créée le 25, la course ne part pas sous cette ligne : on laisse passer le 27, une ligne neuve sera à demander à Lazar (nœud 2 (a), `GO-2026-11-18-56`, point 3) | code v3 ; nœud 2 |
~~~

### D8 — § 8.1, titre

Avant :

~~~text
### 8.1 L'activité interne : deux branches (ordres de grandeur, non mesurés ; choix à Lazar)
~~~

Après :

~~~text
### 8.1 L'activité interne : deux branches (ordres de grandeur, non mesurés) ; **branche B retenue** (`GO-2026-11-18-55`, confirmée `R-3435`)
~~~

### D9 — § 8.1, ligne « lettre de la ligne »

Avant :

~~~text
| lettre de la ligne | tenue | non tenue à la lettre : mot exprès de Lazar |
~~~

Après :

~~~text
| lettre de la ligne | tenue | non tenue à la lettre : mot exprès de Lazar, donné (`GO-2026-11-18-55`, `R-3435`) |
~~~

### D10 — § 8.1, après la table

Avant :

~~~text
### 8.2 Autres
~~~

Après :

~~~text
La colonne A est gardée pour mémoire : elle n'est pas chiffrée dans cette course. Si Lazar voulait la branche A, il le dit, la ligne `GO-2026-11-18-55` est remplacée, et l'ordre et ce devis passent en version nouvelle.

### 8.2 Autres
~~~

### D11 — § 8.2, passe préalable des épreuves

Avant :

~~~text
- Passe préalable des épreuves sur une location à part (si le directeur le choisit) : ≈ 5,6 USD au central, plus une seconde création.
~~~

Après :

~~~text
- Passe préalable des épreuves sur une location à part : **non retenue** (nœud 3 (a), `GO-2026-11-18-56`, point 3 : épreuves au début de la course, même carte, arrêt au premier échec) ; 0 USD.
~~~

### D12 — § 8.3 (neuf)

Avant :

~~~text
## 9. Ligne d'engagement
~~~

Après :

~~~text
### 8.3 La passe de recalcul de l'activité interne : une course à part (branche B)

- **Hors de ce devis et hors de la ligne `GO-2026-11-10-08`** (« 0 USD de plus dans GO-2026-11-10-08 », ligne `GO-2026-11-18-55`) : elle a son devis écrit, sa ligne au registre des accords et son préenregistrement scellé, à part (ordre brouillon 5, § 13). **Aucune dépense n'en est engagée ici.**
- Ordre de grandeur (§ 8.1, non mesuré ; repris dans `GO-2026-11-18-55`) : 1,1 à 1,6 h de carte, ≈ 4,2 à 4,7 USD attendus ; 2,2 à 3,2 h, ≈ 8,9 à 10,4 USD au pire.
- Ce qu'elle consomme de la course : les identifiants et textes exacts des actions (par phase et combinés), les deux adaptateurs, la configuration et le manifeste (commit de lancement, versions) ; le modèle de base à sa révision figée, que le programme ne garde pas.
- Ce qu'elle rend : l'activité interne, égale aux arrondis du calcul près, pas au bit près.

## 9. Ligne d'engagement
~~~

### D13 — § 9, ligne d'engagement

Avant :

~~~text
branche de l'activité interne `<<MOT_LAZAR_ACTIVITE_INTERNE_IIB>>` ;
~~~

Après :

~~~text
branche de l'activité interne B (`GO-2026-11-18-55`, confirmée `R-3435`), passe de recalcul hors de cette ligne ;
~~~

## Ordre (`ordre-exploratoire-ii-b-v1-brouillon5.md`) : 41 changements

| changement | où | raison |
|---|---|---|
| O1 | titre | version du texte |
| O2 | avertissement de tête | mot exprès de Lazar donné, branche B |
| O3 | statut | version du texte, fabrication, auteur (R12) |
| O4 | en-tête, accords du 2026-11-18 | lignes d'accord citées par la tâche |
| O5 | en-tête, pièces citées : devis | devis brouillon 5 |
| O6 | en-tête, pièces citées : notes | pièces lues pour le brouillon 5 |
| O7 | en-tête, code lu | état du code pris du contrôle court |
| O8 | traitement des remarques, ligne B1 | B1 fermé |
| O9 | section neuve avant le § 0 | résumé des changements du brouillon 5 |
| O10 | § 0, ce qui en sort | branche B |
| O11 | § 0 bis | branche B tranchée ; suite A retirée |
| O12 | § 1, conception, consigne, devis | devis brouillon 5 |
| O13 | § 1, code | commit des corrections du relais et de la poussée, d'après le contrôle court |
| O14 | § 1, calendrier | aucune création après 2026-11-25T23:00Z |
| O15 | § 1, préalable | nœud 2 tranché (a) |
| O16 | § 1, pièces interdites | nœud 6 tranché (b) |
| O17 | § 2, réglages de la lecture (2) | portage de la base textuelle : recommandations du relevé du code des deux bases |
| O18 | § 3, titre | état des artefacts à la tête a31b8970 |
| O19 | § 3, aucune activation | branche B |
| O20 | § 4 étape 1 | points à trancher : tranchés |
| O21 | § 4 étape 2 | code : état à a31b8970, CC-01, nœud 5 (a), portage |
| O22 | § 4 étape 6 | clonage réduit joué à blanc d'abord |
| O23 | § 4 bis, place | nœud 3 tranché (a) |
| O24 | § 4 bis point 6, état du code | correction du relais constatée à a31b8970 |
| O25 | § 4 bis point 6, forme de la ligne | forme rejouée par le contrôle court |
| O26 | § 4 ter, choix | le nœud 3 ne tranche pas les essais du jetoniseur |
| O27 | § 4 quater, titre | tête des corrections connue |
| O28 | § 4 quater, état constaté | état à a31b8970 d'après le contrôle court |
| O29 | § 5 étape 1, extractions réduites | jouées à blanc d'abord |
| O30 | § 5 étape 2, fenêtre | aucune création après 2026-11-25T23:00Z |
| O31 | § 5 étape 5, rapatriement | compléments du contrôle court (§ 4, points 2 et 3) |
| O32 | § 5 étape 6 | destruction après rapatriement sans écart ou mot de la mère |
| O33 | § 7 | liste des fichiers par phase avec leurs sceaux ; aucune activation |
| O34 | § 8, exclus | le rédacteur du brouillon 5 est exclu |
| O35 | § 9 et 10, devis | devis brouillon 5 ; branche B |
| O36 | § 11, introduction | cinq marqueurs propres |
| O37 | § 11, devis | devis brouillon 5 |
| O38 | § 11, commit du code revu | après CC-01 |
| O39 | § 11, marqueurs propres | trois remplis, un neuf |
| O40 | § 11, comptes | comptes du brouillon 5 |
| O41 | § 13 (neuf) | la passe de recalcul décrite comme une course à part |

### O1 — titre

Avant :

~~~text
instance à part — v1, brouillon 4
~~~

Après :

~~~text
instance à part — v1, brouillon 5
~~~

### O2 — avertissement de tête

Avant :

~~~text
> **Cet ordre n'est ni scellé ni remis tant que Lazar n'a pas donné son mot exprès sur l'activité interne (§ 0 bis, marqueur `<<MOT_LAZAR_ACTIVITE_INTERNE_IIB>>`).** Aucun défaut de 48 heures ne vaut sur ce point : c'est une condition écrite dans la ligne de dépense.
~~~

Après :

~~~text
> **Mot exprès de Lazar sur l'activité interne : donné, branche B** (`registres/go.md`, ligne `GO-2026-11-18-55` ; confirmé au registre des décisions, ligne `R-3435`) : rien n'est enregistré pendant la course ; on garde les textes exacts des actions et les deux adaptateurs ; l'activité se recalcule plus tard par une passe à part, avec son devis et sa ligne à part (§ 0 bis, § 13). Cet ordre reste un brouillon : il n'est ni scellé comme ordre ni remis tant que les marqueurs en attente (§ 11) ne sont pas remplis.
~~~

### O3 — statut

Avant :

~~~text
- **Statut** : **brouillon 4**, scellé comme brouillon, non contre-lu. Brouillon 3 (`ordre-exploratoire-ii-b-v1-brouillon3.md`, `eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`) intact (R12). Écrit le 2026-11-18 vers 20:10 UTC (`date -u`) par le même rédacteur neuf
~~~

Après :

~~~text
- **Statut** : **brouillon 5**, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon5-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 4 (`ordre-exploratoire-ii-b-v1-brouillon4.md`, `91a592ff776efd4a9cf2293cfee2a837a25b4bee6d33fcff087662cbf2f715c8`, intact, R12), recopié à l'octet hors des changements listés dans `differences-brouillon4-vers-5-v1.md`. Écrit le 2026-11-18 vers 21:30 UTC (`date -u`) par un rédacteur neuf (sous-agent de la session mère, même mandat), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons 1 à 4, qui n'a pas ouvert la consigne privée et qui n'a lu, du côté des moniteurs, que les deux relevés cités au § 2. Brouillon 3 (`ordre-exploratoire-ii-b-v1-brouillon3.md`, `eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`) intact (R12). Le brouillon 4 a été écrit le 2026-11-18 vers 20:10 UTC (`date -u`) par le rédacteur neuf
~~~

### O4 — en-tête, accords du 2026-11-18

Avant :

~~~text
- **Pièces citées** (non modifiées) : conception
~~~

Après :

~~~text
- **Accords du 2026-11-18** (ces seules lignes lues) : `registres/go.md`, ligne `GO-2026-11-18-55` (activité interne, branche B ; « 0 USD de plus dans GO-2026-11-10-08 ») ; ligne `GO-2026-11-18-56`, point 3 (nœuds 2 (a), 3 (a), 4 (B), 5 (a), 6 (b) de la note v2) et point 4 (portage de la base textuelle selon les recommandations du relevé du code des deux bases) ; registre des décisions, ligne `R-3435` (confirmation de la branche B, mot direct de Lazar). Ces lignes renvoient à `R-3434`, non lue par le rédacteur.
- **Pièces citées** (non modifiées) : conception
~~~

### O5 — en-tête, pièces citées : devis

Avant :

~~~text
devis `devis-ii-b-v1-brouillon4.md` (`08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`)
~~~

Après :

~~~text
devis `devis-ii-b-v1-brouillon5.md` (`8ee9ead15fb5feadbffc41ffb3cd8d9abe8a8fc1d82b588f2957de93405e7e32` ; brouillon 4 `08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`, remplacé)
~~~

### O6 — en-tête, pièces citées : notes

Avant :

~~~text
note des points à trancher `noeuds-ii-b-pour-lazar-v2.md`.
~~~

Après :

~~~text
note des points à trancher `noeuds-ii-b-pour-lazar-v2.md` (`be431ed56a20657d924a5b5546dd78bb465afd0e2bf39cfb91a6d0a260d25207`) ; contrôle court du code après corrections, tête `a31b8970`, `docs/notes/barreau8-iib-v1/controle-court-code-iib-v3-v1.md` (`02962a4a4951eeb424450d598221c6136ae09158a1ed8f33dfa84f79dc14c3a2`) ; relevé du code des deux bases, `docs/notes/barreau8-iib-v1/releve-code-des-deux-bases-v1.md` (`601bbc84ae6bf0a31ffba36e20bf554df5da15d60882c92907f8b5e9ef942034`) ; relevé des réglages de la base textuelle, `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md` (`98284ec7f6ac6bafbae0400234945d2b769db51fe7304b1ae5b181247ddde692`).
~~~

### O7 — en-tête, code lu

Avant :

~~~text
tête `d88e3d947ec4f05958834e2746a800c854271a8f` (inchangée depuis le brouillon 3).
~~~

Après :

~~~text
tête `d88e3d947ec4f05958834e2746a800c854271a8f` (inchangée depuis le brouillon 3). Au brouillon 5, le code n'est pas relu : l'état de la tête `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` est pris du contrôle court (`02962a4a…c3a2`).
~~~

### O8 — traitement des remarques, ligne B1

Avant :

~~~text
| **B1** condition de la ligne non tenue, défaut de 48 h | **reste ouvert** (le rédacteur ne choisit pas) : l'ordre écrit les deux suites et un marqueur nommé qui attend le mot exprès de Lazar ; aucun défaut | § 0 bis ; § 4 étape 1 ; § 11 |
~~~

Après :

~~~text
| **B1** condition de la ligne non tenue, défaut de 48 h | **fermé au brouillon 5** : mot exprès de Lazar, branche B (`GO-2026-11-18-55`, confirmée `R-3435`) ; au brouillon 4, restait ouvert | § 0 bis ; § 4 étape 1 ; § 11 ; § 13 |
~~~

### O9 — section neuve avant le § 0

Avant :

~~~text
## 0. Ce que ce run est, et n'est pas
~~~

Après :

~~~text
## Ce que le brouillon 5 change (détail : `differences-brouillon4-vers-5-v1.md`)

- **Activité interne** : branche B, par mot exprès de Lazar ; la suite A est retirée (§ 0 bis) ; la passe de recalcul est décrite comme une course à part (§ 13).
- **Points à trancher de la note v2** : tranchés (§ 4 étape 1 ; § 1 ; § 4 bis).
- **Portage de la base textuelle** : recommandations du relevé du code des deux bases (§ 2).
- **Compléments demandés par le contrôle court** (§ 4 et § 6 de ce contrôle) : liste des fichiers par phase avec leurs sceaux (§ 7) ; tout fichier listé absent ou sans compagnon conforme est un écart rapporté, destruction retenue jusqu'au mot de la session mère, au plus tard 2026-11-27T22:00:00Z (§ 5 étape 5, § 7) ; aucune création après 2026-11-25T23:00Z (§ 1, § 5 étape 2) ; clonage réduit de l'étape 1 joué à blanc d'abord (§ 4 étape 6, § 5 étape 1) ; au rapatriement, instance arrêtée, liste des empreintes du résumé comparée à l'arbre de la branche du run avant toute destruction (§ 5 étape 5).
- **Code** : état de la tête `a31b8970` pris du contrôle court (§ 3, § 4 quater) ; le commit de lancement reste un marqueur.

## 0. Ce que ce run est, et n'est pas
~~~

### O10 — § 0, ce qui en sort

Avant :

~~~text
selon la branche du § 0 bis, l'activité interne enregistrée ou de quoi la recalculer ;
~~~

Après :

~~~text
**aucune activité interne** (branche B, § 0 bis) : les identifiants et textes exacts des actions et les deux adaptateurs sont de quoi la recalculer plus tard (§ 13) ;
~~~

### O11 — § 0 bis

Avant :

~~~text
## 0 bis. L'activité interne : deux suites possibles (B1, ouvert)

La ligne d'accord dit « avec l'activité interne enregistrée ». La conception (§ 0, 6.3, 7) et le code v3 n'enregistrent rien : toute clé qui nomme une activation arrête la course, tout fichier `activations*` est refusé, l'étape des morceaux de l'amorce est vide. Lazar choisit, par un **mot exprès consigné au registre des décisions** : `<<MOT_LAZAR_ACTIVITE_INTERNE_IIB>>` (valeur : « A » ou « B », et la référence de la ligne du registre où la mère a consigné le mot). Coûts des deux branches : devis brouillon 4, § 8.1.

- **Suite B — garder de quoi recalculer.** Cet ordre s'applique tel qu'il est écrit. La course garde les identifiants de toutes les actions et les deux adaptateurs ; l'activité se recalcule plus tard, par une passe sur une location à part, sous préenregistrement scellé à part, devis et GO à part ; elle sera **égale aux arrondis du calcul près, pas au bit près**. La mère consigne que la ligne est lue ainsi, sur le mot de Lazar.
- **Suite A — enregistrer pendant la course.** Cet ordre **n'est pas scellé** dans cette version. Il faut d'abord : une décision du côté des moniteurs sur quoi enregistrer (couches, jetons, précision) ; le code changé (gardes, capture ou passe finale, étape des morceaux, configuration, essais sain et artefact), contre-lu ; la conception et cet ordre en version nouvelle (§ 0, 2, 3, 6, 7, 8) ; les fichiers d'activations scellés à part et non lus avant le préenregistrement et le verdict du test de transfert. Le calendrier du 25 en dépend.
~~~

Après :

~~~text
## 0 bis. L'activité interne : branche B, tranchée par Lazar

La ligne d'accord dit « avec l'activité interne enregistrée ». La conception (§ 0, 6.3, 7) et le code v3 n'enregistrent rien : toute clé qui nomme une activation arrête la course, tout fichier `activations*` est refusé, l'étape des morceaux de l'amorce est vide. **Lazar a choisi la branche B par son mot exprès** : `registres/go.md`, ligne `GO-2026-11-18-55` (verbatim dans la ligne : « Activité interne du saboteur à budget go now, go autres recos ») ; confirmée au registre des décisions, ligne `R-3435`, verbatim : « Ou veux-tu la recalculer plus tard sur une location à part (branche B : aucun code ne change, environ 4,2 à 4,7 dollars plus tard, résultat égal aux arrondis près) go ». Marqueur `MOT_LAZAR_ACTIVITE_INTERNE_IIB` : **B — `GO-2026-11-18-55`, confirmée `R-3435`**.

- **Ce que la course fait** : elle n'enregistre rien de l'activité interne ; aucun code ne change pour ce point. Elle garde les textes exacts des actions (identifiants de jetons et textes, par phase et combinés, § 7) et les deux adaptateurs.
- **Ce qui vient plus tard** : l'activité se recalcule par une passe sur une location à part, **course à part** (§ 13), sous son préenregistrement scellé, son devis et sa ligne d'accord à part ; elle sera **égale aux arrondis du calcul près, pas au bit près**. Ordre de grandeur : devis brouillon 5, § 8.3.
- **Suite A** (enregistrer pendant la course) : **non retenue**. Si Lazar la voulait, il le dit, la ligne `GO-2026-11-18-55` est remplacée, et cet ordre passe en version nouvelle (ce qu'elle demanderait : devis brouillon 5, § 8.1).
~~~

### O12 — § 1, conception, consigne, devis

Avant :

~~~text
`brouillons/ii-b-saboteur-budget-v1/devis-ii-b-v1-brouillon4.md` (`08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580`) |
~~~

Après :

~~~text
`brouillons/ii-b-saboteur-budget-v1/devis-ii-b-v1-brouillon5.md` (`8ee9ead15fb5feadbffc41ffb3cd8d9abe8a8fc1d82b588f2957de93405e7e32`) |
~~~

### O13 — § 1, code

Avant :

~~~text
au commit `<<COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB>>` (égal au commit du code revu ou ancêtre de lui) ;
~~~

Après :

~~~text
au commit `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (contrôle court `02962a4a…c3a2` ; le commit du code revu doit en descendre, sur la même branche ; sinon ce marqueur retombe en attente) ;
~~~

### O14 — § 1, calendrier

Avant :

~~~text
**dernière commande `creation` à 23:00 UTC le 2026-11-25**
~~~

Après :

~~~text
**aucune création après 2026-11-25T23:00Z** (dernière commande `creation` à 23:00 UTC le 2026-11-25)
~~~

### O15 — § 1, préalable

Avant :

~~~text
si 7b n'est pas créée le 25 : note des nœuds, point 2 |
~~~

Après :

~~~text
si 7b n'est pas créée le 25 : la course ne part pas sous cette ligne ; on laisse passer le 27 et une ligne neuve sera à demander à Lazar (nœud 2 (a), `GO-2026-11-18-56`, point 3) |
~~~

### O16 — § 1, pièces interdites

Avant :

~~~text
| Pièces interdites | celles du brouillon 3, § 1 (dont la branche `prep/iib-code-v2`) |
~~~

Après :

~~~text
| Pièces interdites | celles du brouillon 3, § 1 (dont la branche `prep/iib-code-v2`) ; la branche `prep/iib-code-v2` reste gelée sur le distant, exclue de la copie publique, inscrite au registre « qui a lu quoi », interdite au lecteur des sondes (nœud 6 (b), `GO-2026-11-18-56`, point 3 ; inscription à faire par la mère) |
~~~

### O17 — § 2, réglages de la lecture (2)

Avant :

~~~text
Réglages de la lecture (2) : `<<REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB>>` (relevé à part, `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md`), fixés avant le commit du code revu.
~~~

Après :

~~~text
Réglages de la lecture (2), portage de la base textuelle : **les recommandations du relevé du code des deux bases**, `docs/notes/barreau8-iib-v1/releve-code-des-deux-bases-v1.md` (`601bbc84ae6bf0a31ffba36e20bf554df5da15d60882c92907f8b5e9ef942034`), retenues par Lazar (`GO-2026-11-18-56`, point 4). Le relevé des réglages (`docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md`, `98284ec7…d692`) est cité pour mémoire ; le relevé du code ne trouve aucun écart entre le code et les réglages que le texte scellé de la base (A) fixe. Marqueur `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB` :

1. **Chemin d'appel** : la lecture (2) appelle les six fonctions du contrat de la pièce (`centres`, `apprendre_a`, `noter_a`, `etat_a`, `apprendre_b`, `noter_b`) de `scripts/mots_et_cout_t06_v3.py` au commit `da06bb57610f840152e4e9a8c449b036577cc582` (`9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674`), chargée par son chemin, après la vérification des modules gelés à leurs empreintes et avec les fils de calcul fixés à 1 ; elle reprend les gardes de l'enveloppe de T0.8 (champs interdits, plis mêlés, lecture de transfert). Aucun réglage de la pièce n'est touché.
2. **Champs de coût et de forme** : vérifier d'abord le format des actions du barreau 8 ; s'il est le même, la fonction gelée `t06.cout.cout_action` appliquée au texte, et les jetons comptés par les identifiants générés ; sinon, un adaptateur déclaré qui met le champ de coût sous la forme attendue, éprouvé sur un cas sain et sur un artefact. Issue de la vérification : `<<FORMAT_ACTIONS_PORTAGE_IIB>>` (« même format » ou « adaptateur déclaré », avec la référence de la vérification).
3. **Centres de tâche** : sur toutes les actions de la lecture, toutes conditions confondues, seuil de 10 coûts lisibles tel que codé.
4. **Règle de lecture** : l'état par unité de lecture (maximum des deux bases, seuil 0,70, plancher), sans les issues M1 à M4.

Le sous-point « gradient lu après le dernier pas » est fixé par le code à la tête `a31b8970` (contrôle court, CC-08), conforme au texte scellé (« au point rendu »). Restent indéterminés d'après le relevé (§ 4), sans choix ici : le nombre de tirages et de permutations de la lecture (2) ; les versions de `numpy` et `scipy` (consignées au manifeste). Ces réglages sont écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage, avant le commit du code revu.
~~~

### O18 — § 3, titre

Avant :

~~~text
à `d88e3d94`, deux artefacts manquent : consigne invisible à l'évaluation, forme de la ligne de 7b)
~~~

Après :

~~~text
à `d88e3d94`, deux artefacts manquent : consigne invisible à l'évaluation, forme de la ligne de 7b ; à `a31b8970`, d'après le contrôle court : l'artefact de la ligne de 7b est fait, sa forme reste à fixer ; celui de la consigne invisible à l'évaluation ne voit pas les contextes, CC-04 ; l'essai du relais de la ligne des épreuves ne lit pas la ligne réelle du lanceur, CC-01, majeur)
~~~

### O19 — § 3, aucune activation

Avant :

~~~text
- **Aucune sonde, aucune activation** (suite B ; en suite A, version nouvelle).
~~~

Après :

~~~text
- **Aucune sonde, aucune activation** (branche B, retenue : § 0 bis).
~~~

### O20 — § 4 étape 1

Avant :

~~~text
1. **Points à trancher par Lazar** (note `noeuds-ii-b-pour-lazar-v2.md`). L'activité interne (point 1) et la place des épreuves (point 3) le sont **par un mot exprès de Lazar consigné au registre des décisions, jamais par un défaut de 48 heures** : ils portent sur les conditions de la ligne de dépense. Le point 1 remplit `<<MOT_LAZAR_ACTIVITE_INTERNE_IIB>>` ; en suite A, arrêt ici (§ 0 bis).
~~~

Après :

~~~text
1. **Points à trancher par Lazar** (note `noeuds-ii-b-pour-lazar-v2.md`) : **tranchés**, par mot direct de Lazar, sans défaut de 48 heures. Point 1, activité interne : **branche B** (`GO-2026-11-18-55` ; confirmée `R-3435`). Points 2 à 6 (« go autres recos », `registres/go.md`, `GO-2026-11-18-56`, point 3) : **2 (a)** attendre 7b ; si elle n'est pas créée le 25, laisser passer le 27, une ligne neuve sera à demander ; **3 (a)** épreuves au début de la course, même carte, arrêt au premier échec, la mère consigne « six épreuves passées » au vu de la ligne de progrès, la course continue sans interruption ; **4 (B)** 60 USD, coupure à 55, A100 seule ; **5 (a)** avant la course, toutes les corrections et tous les essais manquants sauf les deux améliorations d'essais, qui passent après la course et avant toute lecture des résultats ; **6 (b)** branche `prep/iib-code-v2` gardée gelée (§ 1).
~~~

### O21 — § 4 étape 2

Avant :

~~~text
2. **Code** : corrections de la vérification courte (VC3-01 à VC3-07), du relais et de la poussée (§ 4 quater), réglages de la lecture (2) (`<<REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB>>`) écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage ; selon le nœud 5, les deux améliorations d'essais ; contrôle court par un lecteur qui n'est pas le développeur ;
~~~

Après :

~~~text
2. **Code** : corrections de la vérification courte (VC3-01 à VC3-07), du relais et de la poussée (§ 4 quater), faites à `a31b8970` d'après le contrôle court ; correction de **CC-01** (essai du relais sur la ligne réelle du lanceur, majeur), exigée avant la course ; mineurs CC-02 à CC-05, souhaitables avant la course selon le contrôle court (à trancher par la mère) ; forme de la ligne de création de 7b fixée, motif et artefact alignés (contrôle court, § 6, point 3) ; réglages de la lecture (2) (§ 2, issue `<<FORMAT_ACTIONS_PORTAGE_IIB>>` comprise) écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage ; les deux améliorations d'essais **après** la course et avant toute lecture des résultats (nœud 5 (a)) ; contrôle court par un lecteur qui n'est pas le développeur ;
~~~

### O22 — § 4 étape 6

Avant :

~~~text
les extractions réduites de l'étape 1 sont jouées à blanc (O-M5).
~~~

Après :

~~~text
les extractions réduites de l'étape 1 sont **jouées à blanc d'abord**, sans dépense, par la mère, avant le scellement de l'ordre ; issue consignée (codes de sortie, place prise, fichiers extraits) ; tout écart → forme corrigée et ordre en version nouvelle (O-M5 ; contrôle court, § 4, point 1).
~~~

### O23 — § 4 bis, place

Avant :

~~~text
Place proposée (nœud 3, **mot exprès de Lazar**, pas de défaut) : sur la carte de la course, avant tout épisode du maître.
~~~

Après :

~~~text
Place retenue (nœud 3 (a), `GO-2026-11-18-56`, point 3) : sur la carte de la course, avant tout épisode du maître ; arrêt au premier échec ; la mère consigne « six épreuves passées » au vu de la ligne de progrès ; la course continue sans interruption.
~~~

### O24 — § 4 bis point 6, état du code

Avant :

~~~text
n'atteint jamais la surveillance** (O-M1). Donc :
~~~

Après :

~~~text
n'atteint jamais la surveillance** (O-M1). À `a31b8970`, le code est corrigé : les lignes réellement émises `etat=passees epreuve=aucune` et `etat=arret epreuve=<identifiant>` sont relayées (contrôle court, CC-01 ; son essai reste à corriger). Donc :
~~~

### O25 — § 4 bis point 6, forme de la ligne

Avant :

~~~text
   - **avec le code corrigé** (`<<COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB>>`) : ligne `PROGRES … etape=epreuves etat=passees` (forme exacte : celle du code corrigé, relue à la vérification courte de l'ordre) ;
~~~

Après :

~~~text
   - **avec le code corrigé** (`a31b8970`, ou le commit du code revu qui en descend) : ligne `PROGRES … etape=epreuves etat=passees epreuve=aucune` (forme rejouée par le contrôle court sur la fonction de progrès réelle ; relue à la vérification courte de l'ordre) ;
~~~

### O26 — § 4 ter, choix

Avant :

~~~text
(+ 0,1 h environ ; devis § 8.2). Choix : nœud 3.
~~~

Après :

~~~text
(+ 0,1 h environ ; devis § 8.2). Le nœud 3, tranché (a), fixe la place des épreuves ; il ne dit pas si ces essais deviennent des arrêts joués par l'amorce : point ouvert, porté à la mère.
~~~

### O27 — § 4 quater, titre

Avant :

~~~text
## 4 quater. Ce que le code corrigé devra faire (session de développement ; tête : `<<COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB>>`)
~~~

Après :

~~~text
## 4 quater. Ce que le code corrigé devra faire (session de développement ; tête : `a31b8970fedb745c993fe23df18bba4a2d9e3cf4`, contrôlée)
~~~

### O28 — § 4 quater, état constaté

Avant :

~~~text
## 5. Étapes de l'exécutante
~~~

Après :

~~~text
**État à `a31b8970`, d'après le contrôle court** (`docs/notes/barreau8-iib-v1/controle-court-code-iib-v3-v1.md` (`02962a4a4951eeb424450d598221c6136ae09158a1ed8f33dfa84f79dc14c3a2`), verdict « autorisable après corrections » : 0 bloquant, 1 majeur, 8 mineurs) : relais corrigé, essai sans portée (CC-01, majeur, à corriger avant la course ; le commit qui en sortira sera celui de `COMMIT_CODE_IIB`) ; poussée par phase et contrôle de fin par `--ignored` corrigés et éprouvés sur les trois chemins de consignation ; le contrôle par `--ignored` ne joue qu'en fin de run (CC-09) : le rapatriement le couvre (§ 5 étape 5) ; deux lignes du `.gitignore` hors des points (CC-07), à déclarer ou à retirer.

## 5. Étapes de l'exécutante
~~~

### O29 — § 5 étape 1, extractions réduites

Avant :

~~~text
**Extractions réduites (forme non éprouvée ; jouée à blanc à l'étape 6 du § 4)** :
~~~

Après :

~~~text
**Extractions réduites (jouées à blanc d'abord, à l'étape 6 du § 4, avant le scellement de l'ordre ; employées ici seulement après une issue conforme consignée)** :
~~~

### O30 — § 5 étape 2, fenêtre

Avant :

~~~text
**aucune commande `creation` après 23:00 UTC le 2026-11-25** ;
~~~

Après :

~~~text
**aucune création après 2026-11-25T23:00Z : aucune commande `creation` après 23:00 UTC le 2026-11-25** ;
~~~

### O31 — § 5 étape 5, rapatriement

Avant :

~~~text
5. **Rapatriement** : `git -C "$W/depot" fetch origin refs/heads/essai/iib-explo-v1:refs/remotes/origin/essai/iib-explo-v1` ; `diag/<run>`, `runs/<run>/manifeste.json`, `donnees/<run>`, `traces/iib-*` ; compagnons vérifiés (`PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .`) ; liste des fichiers de `donnees/<run>` comparée à `empreintes` de `resume.json` (ou `sorties_ecrites` de `arret.json`). **Tout fichier listé et absent de la branche, ou présent sans compagnon conforme (interruption pendant une écriture comprise), est un écart, rapporté à la mère ; la destruction (étape 6) attend son mot**, au plus tard jusqu'à 2026-11-27T22:00:00Z.
~~~

Après :

~~~text
5. **Rapatriement, instance arrêtée, avant toute destruction** (contrôle court, § 4, points 2 et 3) :
   - l'instance est à l'état « stopped » (fin normale ou anormale) ; sinon l'exécutante l'arrête d'abord par son identifiant (R10) ;
   - `git -C "$W/depot" fetch origin refs/heads/essai/iib-explo-v1:refs/remotes/origin/essai/iib-explo-v1` ; `diag/<run>`, `runs/<run>/manifeste.json`, `donnees/<run>`, `traces/iib-*` ;
   - **liste des empreintes du résumé comparée à l'arbre de la branche du run** : la liste `resultat.empreintes` de `diag/<run>/resume.json` (ou `sorties_ecrites` de `diag/<run>/arret.json` si le run s'est arrêté) contre `git -C "$W/depot" ls-tree -r --name-only refs/remotes/origin/essai/iib-explo-v1` ; puis contre la liste du § 7 pour les phases jouées ;
   - chaque compagnon vérifié (`PYTHONPATH=src python -m controle_ia.scellement verifier <fichier>`, puis `verifier-arbre .`) ;
   - relevés dans le journal et les traces : `ERREUR DE CHAÎNE`, `FIN ANORMALE`, `iib-fichiers-trop-gros.txt`, `progres-retenues.txt` ;
   - **tout fichier listé (au résumé, à l'arrêt ou au § 7) absent de la branche, ou présent sans compagnon conforme (interruption pendant une écriture comprise), est un écart, rapporté à la mère ; la destruction (étape 6) est retenue jusqu'au mot de la session mère, au plus tard jusqu'à 2026-11-27T22:00:00Z.** Sur ce mot seulement : relancer l'instance arrêtée (un second démarrage pousse d'abord les commits en attente) ou lire son disque, puis rapatrier de nouveau. Le contrôle de fin par `--ignored` ne jouant qu'en fin de run (CC-09), cette comparaison est le seul contrôle sur l'arrêt consigné, la minuterie et un second démarrage.
~~~

### O32 — § 5 étape 6

Avant :

~~~text
du seul identifiant créé, après le rapatriement vérifié,
~~~

Après :

~~~text
du seul identifiant créé, après le rapatriement vérifié (étape 5 sans écart, ou mot de la mère sur les écarts),
~~~

### O33 — § 7

Avant :

~~~text
Table du brouillon 3, § 7, inchangée, avec la colonne « poussé par l'amorce » : **oui pour tous les fichiers par phase et par tour au commit `<<COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB>>`** ; à `d88e3d94`, non (défaut R-A). Suite A seulement : fichiers d'activations, scellés à part, non lus avant le préenregistrement et le verdict du test de transfert (version nouvelle de l'ordre).
~~~

Après :

~~~text
Table du brouillon 3, § 7, inchangée, avec la colonne « poussé par l'amorce » : **oui pour tous les fichiers par phase et par tour au commit `a31b8970` (contrôle court, § 4) et au commit du code revu qui en descend** ; à `d88e3d94`, non (défaut R-A). Aucun fichier d'activations (branche B).

**Fichiers attendus sous `donnees/<run>/`, par phase, avec leurs sceaux** (contrôle court, § 4, point 1), en plus des fichiers combinés (`oracle-iib.json`, `ids-actions-iib.npz`, `textes-actions-iib.jsonl`, chacun avec son `.sha256`) et des deux adaptateurs avec leurs sceaux (noms : table du brouillon 3, § 7) :

| phase | fichiers, chacun avec son compagnon `.sha256` | attendue |
|---|---|---|
| `etalonnage` | `oracle-iib-etalonnage.json`, `ids-actions-iib-etalonnage.npz`, `textes-actions-iib-etalonnage.jsonl` | toujours ; écrits même si une épreuve échoue |
| `tour1` … `tour<r>` | `oracle-iib-tour<k>.json`, `ids-actions-iib-tour<k>.npz`, `textes-actions-iib-tour<k>.jsonl`, pour k = 1 … r, r le dernier tour joué (au plus 12) | pour chaque tour joué |
| `evaluation` | `oracle-iib-evaluation.json`, `ids-actions-iib-evaluation.npz`, `textes-actions-iib-evaluation.jsonl` | si l'évaluation est jouée |

Les identifiants et textes exacts des actions et les deux adaptateurs sont ce que la passe de recalcul (§ 13) consomme. **Tout fichier listé absent de la branche, ou sans compagnon conforme, est un écart rapporté à la mère ; la destruction est retenue jusqu'au mot de la session mère, au plus tard 2026-11-27T22:00:00Z** (§ 5 étape 5).
~~~

### O34 — § 8, exclus

Avant :

~~~text
**Exclus de toute lecture des sondes du barreau 8** : le rédacteur de cet ordre ;
~~~

Après :

~~~text
**Exclus de toute lecture des sondes du barreau 8** : le rédacteur de cet ordre (brouillons 3 et 4) ; le rédacteur du brouillon 5 ;
~~~

### O35 — § 9 et 10, devis

Avant :

~~~text
Devis : `devis-ii-b-v1-brouillon4.md` : attendu ≈ 12 à 20 USD (central ≈ 16) ; pire cas ≈ 52,5 USD ; au plus 59,8 tenus par les gardes ; activité interne : suite A ≈ 0 à 0,9 USD de plus dans la ligne (1,7 au pire), suite B 0 USD dans la ligne et ≈ 4,2 à 4,7 USD plus tard (≈ 8,9 à 10,4 au pire), ordres de grandeur non mesurés.
~~~

Après :

~~~text
Devis : `devis-ii-b-v1-brouillon5.md` (chiffres inchangés depuis le brouillon 4) : attendu ≈ 12 à 20 USD (central ≈ 16) ; pire cas ≈ 52,5 USD ; au plus 59,8 tenus par les gardes ; activité interne, branche B retenue : 0 USD dans la ligne ; la passe de recalcul, course à part (§ 13), ≈ 4,2 à 4,7 USD (≈ 8,9 à 10,4 au pire), ordres de grandeur non mesurés, sous son devis et sa ligne à part.
~~~

### O36 — § 11, introduction

Avant :

~~~text
30 marqueurs de `configuration_v1.MARQUEURS`, plus quatre marqueurs nommés propres à l'ordre (hors de la configuration).
~~~

Après :

~~~text
30 marqueurs de `configuration_v1.MARQUEURS`, plus cinq marqueurs nommés propres à l'ordre (hors de la configuration ; le cinquième, `FORMAT_ACTIONS_PORTAGE_IIB`, est neuf au brouillon 5).
~~~

### O37 — § 11, devis

Avant :

~~~text
| `CHEMIN_DEVIS_IIB`, `EMPREINTE_DEVIS_IIB` | remplis (proposés, sous réserve de la contre-lecture du devis) | `devis-ii-b-v1-brouillon4.md`, `08107e07…a580` |
~~~

Après :

~~~text
| `CHEMIN_DEVIS_IIB`, `EMPREINTE_DEVIS_IIB` | remplis (proposés, sous réserve de la contre-lecture du devis) | `devis-ii-b-v1-brouillon5.md`, `8ee9ead1…7e32` |
~~~

### O38 — § 11, commit du code revu

Avant :

~~~text
| `COMMIT_CODE_IIB`, `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR` | en attente | commit du code revu (§ 4 étape 2) |
~~~

Après :

~~~text
| `COMMIT_CODE_IIB`, `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR` | en attente | commit du code revu (§ 4 étape 2), après la correction de CC-01 |
~~~

### O39 — § 11, marqueurs propres

Avant :

~~~text
| `MOT_LAZAR_ACTIVITE_INTERNE_IIB` (propre) | en attente | **mot exprès de Lazar**, « A » ou « B », et la ligne du registre (§ 0 bis) ; aucun défaut |
| `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (propre) | en attente | tête de la session de développement qui porte les corrections du § 4 quater |
| `COMMIT_LANCEMENT_IIB` (propre) | en attente | § 4 étape 5 |
| `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB` (propre) | en attente | relevé à part et décision (§ 2) |
~~~

Après :

~~~text
| `MOT_LAZAR_ACTIVITE_INTERNE_IIB` (propre) | rempli | **B** — `GO-2026-11-18-55`, confirmée `R-3435` (§ 0 bis) |
| `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (propre) | rempli, sous réserve | `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (contrôle court) ; retombe en attente si le commit du code revu n'en descend pas |
| `COMMIT_LANCEMENT_IIB` (propre) | en attente | § 4 étape 5 ; reste un marqueur : le développeur corrige encore un défaut majeur du code (CC-01) |
| `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB` (propre) | rempli (décision) | recommandations du relevé du code des deux bases, `GO-2026-11-18-56`, point 4 (§ 2) ; écrits au code avant le commit du code revu |
| `FORMAT_ACTIONS_PORTAGE_IIB` (propre, neuf) | en attente | vérification du format des actions du barreau 8 (§ 2, point 2), avant le commit du code revu |
~~~

### O40 — § 11, comptes

Avant :

~~~text
Comptes : sur les 30, **14 remplis, 14 en attente, 2 hors de ce texte** ; plus 4 propres, en attente. Compté par programme (script du rédacteur, au bloc-notes, qui ne cherche que le motif des marqueurs) : **18 marqueurs distincts restent dans ce texte** = les 14 en attente des 30 + les 4 propres ; aucun marqueur rempli n'y reste.
~~~

Après :

~~~text
Comptes : sur les 30, **14 remplis, 14 en attente, 2 hors de ce texte** (inchangés depuis le brouillon 4) ; plus 5 propres : **3 remplis** (`MOT_LAZAR_ACTIVITE_INTERNE_IIB`, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`), **2 en attente** (`COMMIT_LANCEMENT_IIB`, `FORMAT_ACTIONS_PORTAGE_IIB`). Compté par programme (`compter-marqueurs-ii-b-v1.py`, scellé dans ce dossier, qui ne cherche que le motif des marqueurs ; sortie `sortie-compter-marqueurs-ii-b-v1.txt`) : **16 marqueurs distincts restent dans ce texte** = les 14 en attente des 30 + les 2 propres en attente ; aucun marqueur rempli n'y reste.
~~~

### O41 — § 13 (neuf)

Avant :

~~~text
R1 entière pour toute confirmation et toute lecture de sonde.
~~~

Après :

~~~text
R1 entière pour toute confirmation et toute lecture de sonde.

## 13. La passe de recalcul de l'activité interne : une course à part (branche B)

- **Ce qu'elle est** : une course distincte de celle-ci, sur une location à part, après celle-ci ; elle recalcule l'activité interne de l'agent sur les textes exacts des actions que cette course garde. **Cet ordre ne la lance pas, ne la chiffre pas dans sa ligne et ne l'autorise pas.**
- **Ce qu'elle exige avant de partir** : son préenregistrement scellé et contre-lu (quoi enregistrer : couches, jetons, précision ; choix du côté des moniteurs) ; son code (passe, essais sain et artefact, contre-lecture) ; son devis écrit ; sa ligne au registre des accords, sur le mot de Lazar. Ordre de grandeur : devis brouillon 5, § 8.3 (≈ 4,2 à 4,7 USD attendus, ≈ 8,9 à 10,4 au pire, non mesurés).
- **Ce qu'elle consomme de cette course** : les identifiants et textes exacts des actions, par phase et combinés, et les deux adaptateurs (§ 7) ; la configuration et le manifeste (commit de lancement, versions) ; le modèle de base à sa révision figée, que le programme ne garde pas (mise à disposition publique). Les contextes sont rebâtis par le code du commit de lancement ; pour les épisodes du maître, la passe relit la consigne privée par programme (contre-lecture de l'ordre, § 5.2) : qui la conduit suit les exclusions du § 8.
- **Ce qu'elle rend** : l'activité interne, égale aux arrondis du calcul près, pas au bit près ; fichiers scellés à part, non lus avant le préenregistrement de la lecture des sondes et le verdict du test de transfert.
- **Ce qui n'en dépend pas** : cette course-ci ; aucun code ne change pour la branche B.
~~~
