# Consigne — contre-lecture du lanceur et de la conception de l'organisme d'idéation sur les bassins étroits — v1

Écrite par la session mère le 13 novembre 2026 à 13:30 UTC (`date -u`). Tu es un **contre-lecteur neuf, d'un autre modèle que
l'auteur** (auteur : Claude Opus 5.5 ; toi : Claude Fable 5.2) ; tu n'as rien écrit de ce que tu relis (R2, N-052).
**Aucune dépense, aucun appel de modèle, aucun réseau.** Langue : français.

## 0. Interdits (à lire d'abord)
Lis en entier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) et applique-le,
avec ces ajouts : jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`,
`registres/index-bras-attaque*`, `anteriorite-bras-informe*` ; aucun `diag/` ni `runs/` de 7a ou 7b ; jamais une valeur de clé,
jamais `env`, `printenv`, `set` sans argument ; heures par `date -u` ; aucune recherche récursive à la racine ; aucune
opération git dans le dépôt de travail ; tu ne lis pas `docs/notes/bassins-etroits-idees-v1/` ; aucune fiche ni contenu de la
course du « pilier attaque » ; **tu ne modifies ni `.claude/settings.json` ni `.claude/hooks/`** (tu peux les lire pour juger
la règle proposée) ; aucun contournement d'une garde ni d'un bac à sable ; un refus se rapporte tel quel. `ulimit -v 6000000`,
un seul processus de calcul à la fois. Tu ne corriges rien : tu constates, tu prouves, tu proposes.

## 1. Pièces (toutes scellées ; vérifie chaque compagnon)
Sous `docs/notes/organisme-bassins-etroits-v1/` : `conception-trois-generations-v1.md` (`4c90a3a5…`), `question-organisme-bassins-etroits-v1.md`
(`c188fa9a…`), `temoins-bassins-etroits-v1.json` (`748f391e…`), `mesurer-consignes-g1-gabarit-40000-v1.json`,
`devis-organisme-bassins-etroits-v1.md` (`1b311242…`), `rapport-preparateur-v1.md` (`b7b57add…`) ;
`scripts/lancer_course_ideation_bassins_etroits_v1.py` (`a10420cc…`) et `tests/test_lancer_course_ideation_bassins_etroits_v1.py`
(`8fa7ae32…`) ; pour comparaison : `scripts/lancer_course_ideation_pilier_attaque_v2_v3.py`, sa contre-lecture
`docs/notes/ideation-organisme-v1/contre-lecture-lanceur-course-pilier-attaque-v2-v2-v1.md` et sa vérification
`verification-lanceur-course-pilier-attaque-v2-v3-v1.md` ; la question du collisionneur
`docs/notes/collisionneur-bassins-etroits-v1/question-v1.md` (`935f4e5b…`) ; la ligne GO-2026-11-13-03 de `registres/go.md`
(par `grep -n` sur ce seul fichier) ; `docs/decisions/decision-N-053-v1.md`, `decision-N-065-v1.md` ; le clone en lecture de
l'orchestrateur `/home/user/lciric/ideation-organism` (n'y écris rien) : la chaîne de lancement nommée par le lanceur.

## 2. Ce que tu vérifies
1. **Le lanceur** : différentiel contre le v3 (ce qui est repris, changé, ajouté) ; lecture de la ligne de GO et de son plafond ;
   argument unique fermé (1, 2, 3) ; **garde de cumul à 60 USD** (cas limites : dépense illisible, génération rejouée, bras sans
   course) ; refus de la génération g+1 sans manifeste de fin scellé de g ; pas de relance après dépense ; drapeaux interdits ;
   clés par leur nom, environnement bâti par filtrage ; sorties hors dépôt ; chaque garde a un cas sain et un artefact (R5) ;
   **cinq mutations de ton choix** sur les gardes les plus fragiles, suite des essais rejouée (77 essais).
2. **La forme de la commande du bras du juge** que le préparateur n'a pas pu exécuter (refus du classifieur, rapporté) : par
   lecture du code de l'orchestrateur, et par l'analyseur d'arguments seul si cela se fait sans rien lancer ; si un refus
   survient, rapporte-le.
3. **Le plancher de la commande d'Argon** (constat du préparateur : ≈ 0,51 USD ; le contrôle externe du v3 aurait été refusé).
4. **La conception** : règle de passage d'une génération à l'autre (écrite d'avance ? déterministe ? aucun score, rang ni
   auteur servi ?) ; lecture d'N-053 et d'N-065 (le classement des juges de l'atelier sert à choisir ce qui passe ; rien n'est
   servi aux proposeurs que des fiches en ordre neutre) : tient-elle ? ; juges et proposeurs de même lignée (Argon proposeur et
   juge) : ce que cela interdit de conclure ; témoins plantés : les quatre classes éprouvent-elles vraiment les juges ? ;
   attestation de lecture entre la course et le bras : qui, quoi, où.
5. **La question et les témoins** : fidélité à la question du collisionneur ; rien qui souffle une réponse ; aucun secret du
   programme (graine, loi plantée, paramètre de monde).
6. **Le devis** : attendu, pire cas, borne ; cohérence avec les plafonds du lanceur.
7. **La règle de permission et l'épingle proposées** : portent-elles sur la seule commande exacte ; l'épingle bloque-t-elle un
   fichier modifié ; rien de plus large que ce que Lazar a accordé (« go règle de permission », R-2530).

## 3. Livrable
`docs/notes/organisme-bassins-etroits-v1/contre-lecture-lanceur-bassins-etroits-v1.md`, scellé : verdict (« autorisable », « autorisable après corrections », « non
autorisable ») ; constats numérotés bloquants, majeurs, mineurs (fichier, ligne, preuve, correction proposée) ; ce que tu n'as pas
vérifié. Rapport final court à la mère : verdict, comptes, trois constats les plus graves, chemin et empreinte, heure, modèle.
