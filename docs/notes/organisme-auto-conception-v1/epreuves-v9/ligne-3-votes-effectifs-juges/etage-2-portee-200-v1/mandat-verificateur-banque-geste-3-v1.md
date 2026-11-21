VERSION DE PYTHON : AUCUNE COMMANDE DE PROGRAMME (additif 6, geste 3) ; AUCUN `-c` ; AUCUN HEREDOC.

AUCUNE COMMANDE DE LISTE HORS DE `X/composition/` ET DE `X/verification-banque/`. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. AUCUNE COMMANDE, D'AUCUNE SORTE, SUR UN CHEMIN SOUS `archives-reponses-modeles/`.

# Mandat du vérificateur de la banque — étage 2 de la ligne 3, geste 3 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21, sous le mot de la mère pour la partie 1 (R-4348, GO-2026-11-21-04, GO-2026-11-20-68), à la lettre de l'additif 6 v2 scellé, geste 3 : « Par le vérificateur, agent du modèle O qui n'a pas écrit le code, sur mandat ; aucune commande de programme. Il rend `X/verification-banque/verification-banque-contre-journal-ligne-3-v1.md` et son compagnon : chaque fragment fautif employé viole l'item visé et lui seul ; chaque fragment conforme employé tient les cinq items. Un fragment contesté est retiré ou récrit **avant** le scellement de la banque, jamais après. »

## Qui

Un vérificateur neuf, modèle O. Tu n'as écrit ni le code de l'étage 2, ni les fragments, ni leurs vérifications, ni l'additif. Tu signes « vérificateur de la banque, geste 3, modèle O ».

## Notations

- `R` = `/home/user/controle-ia-travail` (branche `prep/ligne-3-etage-2-execution-v1`, à ne pas changer).
- `E` = `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1`.
- `X` = `E/execution-v1`.
- `L3` = `R/prereg/organisme-auto-conception-v9`.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- L'additif 6 v2 : `L3/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md` (`e2afc7b9…`). Lis le geste 3 et la décision n° 42 du § 11 (réserve 6) : les fragments `f-epr-dis-01`, `f-epr-dis-05`, `f-voi-net-05` et `f-epr-net-04` sont nommés, et leurs témoins se lisent au champ `fragments` du journal.
- Le texte de la ligne 3 v7 : `L3/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, l. 251 à 256, Q3, et la liste des items.
- La consigne figée du juge : `R/docs/notes/organisme-auto-conception-v1/course-v1/consigne-juge-auto-conception-v1.md` (`b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167`). Elle donne **les cinq items, à la lettre**.
- Les fragments v3 : `E/fragments-v3/fragments-etage-2-ligne-3-v3.json` (`23be8dae1839eab72979b794371a7fb0bce38bcd41b8309cc79386fc233c50fb`), avec leur rapport (`E/fragments-v3/rapport-redacteur-fragments-etage-2-v3.md`). Ce rapport donne la table de chaque fautif, avec l'item visé et le trait visible.
- La composition : `X/composition/`, avec ces empreintes :
  - `banque-temoins-ligne-3-v1.json` : `70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd` (`HEX_BANQUE`) ;
  - `journal-construction-ligne-3-v1.json` : `9b7d6f57e3b18bb688d6c26b104406202c1aa4b812583cbbc5bec38a4f62a747` (`HEX_JOURNAL`, c'est la vérité) ;
  - `partage-ligne-3-v1.json` : `085ded29…` ;
  - `manifeste-composition.json` : `fc8bb84c…`.

## Ce que tu fais

1. À partir du journal de construction, établis la liste des **fragments employés** (champ `fragments` de chaque témoin) et leur nombre d'usages.
2. Pour **chaque fragment fautif employé** : relis son texte et l'item qu'il vise selon le journal et le rapport des fragments, puis juge à la lettre des cinq items de la consigne.
   - Viole-t-il l'item visé, par un trait visible dans la carte seule ?
   - Ne viole-t-il **que** cet item ?

   Verdict par fragment : « tenu », ou « contesté » avec la raison.
3. Pour **chaque fragment conforme employé** : tient-il les cinq items ? Verdict par fragment.
4. Sondage sur la banque elle-même : prends au moins dix témoins, dont un de chaque classe et de chaque niveau. Vérifie que le texte du témoin dans la banque est bien la composition des fragments que le journal lui attribue, sans autre ajout que les jointures du générateur. Note tout écart.
5. Les quatre fragments nommés par la réserve 6 : dis s'ils sont employés, par quels témoins, et ton verdict sur chacun.
6. **Aucun nom d'item** en mots normalisés dans les fragments employés (règle M4) : vérifie-le par lecture.

Tu n'ouvres que les fichiers nommés. Tu ne lances aucun programme. Tu ne corriges rien : un fragment contesté se rend à la session, qui le porte à la mère.

## Ce que tu rends

`X/verification-banque/verification-banque-contre-journal-ligne-3-v1.md`. Crée d'abord le dossier par `mkdir` sur son chemin complet. Puis pose son compagnon par `env -C X/verification-banque sha256sum verification-banque-contre-journal-ligne-3-v1.md`, redirigé par `>` vers `X/verification-banque/verification-banque-contre-journal-ligne-3-v1.md.sha256`.

Le rapport contient :
- les empreintes vérifiées ;
- la table des fragments employés : identifiant, catégorie ou item visé, niveau, usages, verdict, raison ;
- le sondage ;
- les quatre fragments de la réserve 6 ;
- le verdict d'ensemble, « Conforme » ou « Non conforme : fragments contestés », avec leur liste.

Tu ne commites rien et tu n'écris nulle part ailleurs que dans `X/verification-banque/`.

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune clé, aucune dépense. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle dans tes sorties. Aucune publication. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
