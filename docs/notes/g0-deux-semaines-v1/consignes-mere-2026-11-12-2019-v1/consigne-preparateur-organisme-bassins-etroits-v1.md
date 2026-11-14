# Consigne — préparateur de l'organisme d'idéation sur les bassins étroits, trois générations — v1

Écrite par la session mère le 13 novembre 2026 à 13:02 UTC (`date -u`). Tu es un sous-agent neuf (Claude Opus 5.5), concepteur et
développeur. **Aucune dépense, aucun appel de modèle, aucun réseau hors le clone en lecture nommé ci-dessous.** Langue : français.

## 0. Interdits (à lire d'abord, sans exception)
Lis en entier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) et applique-le,
avec ces ajouts : jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`,
`registres/index-bras-attaque*`, `anteriorite-bras-informe*` ; aucun `diag/` ni `runs/` de 7a ou 7b ; jamais une valeur de clé,
jamais `env`, `printenv`, `set` sans argument ; heures par `date -u` ; aucune recherche récursive à la racine du dépôt ;
aucune opération git dans le dépôt de travail (la mère commite) ; tu ne lis pas `docs/notes/bassins-etroits-idees-v1/` ;
**tu ne lis aucune fiche ni aucun contenu de la course du « pilier attaque »** (seulement sa mécanique : lanceur, devis, essais,
contre-lectures) ; **tu ne modifies ni `.claude/settings.json` ni `.claude/hooks/`** (tu proposes le texte exact de la règle,
la mère l'écrit) ; aucun contournement d'un bac à sable ni d'une garde ; un refus se rapporte tel quel. Mémoire limitée :
`ulimit -v 6000000`, un seul processus de calcul à la fois.
Écart écrit : clone en lecture du dépôt public de l'organisme, une seule fois :
`GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/lciric/ideation-organism /home/user/lciric/ideation-organism`
(s'il existe déjà, vérifie son origine et sers-t'en ; n'y écris rien).

## 1. Pourquoi
Mots directs de Lazar (R-2523, R-2528, R-2530) : « je veux aussi lancer l'organisme dessus, trois generations » ; forme (c) ;
« go 60 USD , go règle de permission ». Ligne **GO-2026-11-13-03** (`registres/go.md`) : organisme d'idéation, atelier d'idées
(N-065, rôle 2 : les fiches sont du matériau, jamais une preuve), sur la question des bassins d'idées étroits et profonds ;
trois courses enchaînées ; 60 USD ; conditions : devis écrit avant le lancement, lanceur neuf contre-lu, témoins plantés, bac à
sable actif, règle de permission pour la seule commande exacte du lanceur.

## 2. Pièces à lire
- La question scellée du tour du collisionneur : `docs/notes/collisionneur-bassins-etroits-v1/question-v1.md` (`935f4e5b…`) et
  ses faits `faits-v1.md` (`d19b5400…`).
- La mécanique de la course des 8 et 9 novembre : `scripts/lancer_course_ideation_pilier_attaque_v2_v3.py` et son essai
  `tests/test_lancer_course_ideation_pilier_attaque_v2_v3.py` ; `docs/notes/ideation-pilier-attaque-v1/organisme-v1/` : les
  deux devis, `mesurer-consignes-*.json`, **la forme** de `temoins-pilier-attaque-v1.json` (structure seulement) ;
  `docs/notes/ideation-organisme-v1/contre-lecture-lanceur-course-pilier-attaque-v2-v2-v1.md` et
  `verification-lanceur-course-pilier-attaque-v2-v3-v1.md` ; dans `registres/decisions.md`, les lignes R-1860 à R-1865 et
  R-1978 à R-1994 (par `grep -n` sur ce seul fichier) : comment la course a été autorisée, où elle a tourné, ce qui a bloqué.
- Le dépôt de l'organisme cloné : `demonstrations/ideation_v8.py` (ou la version la plus récente de la même chaîne), son aide,
  `pole/ideation_v2.py`, `pole/adaptateurs.py` (sonde du bac à sable), `pole/relais.py`.
- `docs/decisions/decision-N-065-v1.md`, `decision-N-053-v1.md`, `decision-N-064-v1.md`.

## 3. À produire, sous `docs/notes/organisme-bassins-etroits-v1/` (chaque pièce scellée dès qu'elle est finie :
`PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`)
1. **Conception** (`conception-trois-generations-v1.md`) : trois courses enchaînées **sans changer l'orchestrateur** ; ce que
   chaque génération reçoit (génération 1 : le recoupement des méthodes, que la mère fournira — prévois son emplacement et sa
   taille maximale ; générations 2 et 3 : les fiches retenues de la précédente) ; **règle écrite d'avance** de passage d'une
   génération à l'autre (combien de fiches, sur quel classement, départage) ; proposeurs et juges (familles ; un juge d'une
   autre lignée que les proposeurs quand c'est possible ; Fable 5.2 ou 5.1 : dis ce que le code permet) ; témoins plantés ;
   ce qui est mesuré d'une génération à l'autre (au moins : part de fiches qui raffinent une fiche reçue, part qui ouvrent une
   idée neuve — par quel moyen sans juge de plus, ou dit « non mesuré ») ; limites (juges à modèles : matériau, pas preuve).
2. **Question de la course** (`question-organisme-bassins-etroits-v1.md`) : la question du collisionneur, reprise mot pour mot
   dans son cœur, mise à la forme que l'orchestrateur attend ; et **les témoins plantés** de cette question
   (`temoins-bassins-etroits-v1.json`, même structure que ceux du 8 novembre : fiches volontairement bonnes et volontairement
   mauvaises, écrites par toi, pour vérifier que les juges les rangent comme attendu).
3. **Bac à sable** : dis, par la sonde de l'orchestrateur lancée telle quelle, s'il est actif dans ce conteneur ; s'il ne l'est
   pas, dis exactement ce qui manque et où la course peut tourner sans contournement (ce qui s'est fait le 9 novembre ; une
   session neuve ; la machine jetable prévue par GO-2026-11-13-02 n'est **pas** payée par cette ligne).
4. **Lanceur neuf** `scripts/lancer_course_ideation_bassins_etroits_v1.py` (dérivé du v3, nom neuf, R12) et son essai
   `tests/test_lancer_course_ideation_bassins_etroits_v1.py` (faux orchestrateur, aucun modèle) : mêmes gardes que le v3 ;
   ligne GO-2026-11-13-03 lue et exigée ; un argument unique et fermé pour la génération (1, 2 ou 3) ; **garde de cumul** :
   la dépense relevée des générations déjà jouées plus le plafond de la suivante ne dépasse jamais 60 USD ; générations 2 et 3
   refusées si la précédente n'a pas son manifeste de fin scellé. Mesure des consignes sans appel. Propose le **texte exact de
   la règle de permission** et de l'épingle d'empreinte, sans les écrire.
5. **Devis** (`devis-organisme-bassins-etroits-v1.md`) : par génération, attendu et pire cas, part Claude (crédits, clé nommée
   `RR_ANTHROPIC_API_KEY_RIGAUD`) et part hors Claude ; total au pire ≤ 60 USD ; durée.
6. **Rapport** (`rapport-preparateur-v1.md`) : ce qui est prêt, ce qui bloque, questions ouvertes pour la mère ou pour Lazar.

## 4. Rapport final à la mère (court)
Verdict (prêt à contre-lire, ou bloqué par quoi) ; chemins et empreintes ; bac à sable actif ou non ; devis en trois chiffres ;
questions ouvertes ; heure de fin (`date -u`) ; ton modèle.
