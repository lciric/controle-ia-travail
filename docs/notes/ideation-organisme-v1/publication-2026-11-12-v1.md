# Publication du 12 novembre 2026 sur `lciric/ideation-organism` (boucle réelle v65 à v67, texte v2, courses v66) — v1

Agent de la session mère, sur le mot de Lazar consigné en R-2433 (option 2, point 2). Heures UTC.

## Droits vérifiés avant tout

API `GET /repos/lciric/ideation-organism` avec `CONTROLE_IA_GITHUB_TOKEN` (champ `permissions` seul lu) : `push: true`
(`admin`, `maintain` aussi). Jeton passé à git par l'environnement (programme `GIT_ASKPASS` qui lit la variable par son nom),
jamais affiché ni écrit.

## Méthode suivie (celle des envois précédents)

- Historique public lu : `main` à `ef4e202b` ; `claude/new-session-7qxayx` à `94bfd92` (R-1715) ; `prep/organisme-v65-boucle-reelle`
  à `c2c39794` (v65 inachevée, autre que `cef5ea60`). Envois antérieurs (R-1771, R-1972, R-2162, R-2286) : avance rapide sur
  `main`, sans forcer ; textes scellés copiés octet pour octet avec leur compagnon ; page d'état en anglais sous `resultats/` ;
  garde des secrets à 0 ; registres, dépenses et journaux bruts gardés privés.
- Paquets récupérés par refspec et vérifiés contre leur compagnon : v65 (`4660197e…`, branche `prep/organisme-v65-v1`, tête
  `cef5ea60`), v66 (`84ab119f…`, tête `7e415cba`), v67 (`8bfcd593…`, tête `ab53b7f4`) ; `git bundle verify` dans l'ordre, sur
  un clone jetable du dépôt public.

## Raccord de l'historique : fusion

`main` public (`ef4e202`) et la chaîne v65 → v67 (issue de `94bfd92`) divergent depuis `faff48b`. **Fusion ordinaire** de
`ab53b7f4` dans `main` (`--no-ff`, aucun conflit), puis un commit neuf par-dessus. Raison : les commits nommés par les textes
scellés et par les rapports de course (`cef5ea60`, `7e415cba`, `ab53b7f4`) deviennent joignables sur `main` avec leurs
empreintes d'origine ; c'est l'absence publique de `cef5ea60` qui avait arrêté une tentative (R-2405). Un commit neuf portant
l'arbre aurait donné d'autres identifiants. La fusion amène aussi `08ad8f3`, `291e917`, `94bfd92`, publics depuis le 7 novembre
sur `claude/new-session-7qxayx`.

## Commits publics (avance rapide `ef4e202..83c456d`, sans forcer)

| commit | contenu |
|---|---|
| `b10ce7a` | fusion (parents `ef4e202`, `ab53b7f4`) : 26 fichiers neufs de v65 à v67 sous `orchestrator/` (dont `exemples/configuration-boucle-reelle-v8.json` `eb626289…`) ; 6 fichiers déjà publics de la branche `7qxayx` |
| `83c456d5dba247411d751cf040a52c3005f9a2fd` | texte v2 scellé `orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v2.md` (`80fe4f03…`, octets égaux, relu en ligne) et compagnon ; `resultats/boucle-reelle-v66/` ; `README.md` ; `MANIFEST.md` |

Sous `resultats/boucle-reelle-v66/` (branche `donnees/course-organisme-v66-poste-local-v1`, octets égaux, compagnons vérifiés) :
rapports `rapport-course-v66-poste-local-v1.md` (`83fd674b…`) et `-v2.md` (`89b97faf…`) ; par course, relevé du lanceur
`boucle-reelle-v66.json` (`c9c6212b…`, `5a7fc27c…`) et lecture gelée `lecture-course-reelle.json` (`7de89198…`, `edae8c4f…`),
issue C5 « non jugeable (arrêt) » toutes deux ; page d'état en anglais `README.md` (`9bcead9c…`). Page principale
(`dbfc0c29…`) : état au 12 novembre, ligne de la boucle dans la table des preuves, note datée sous la figure 1. `MANIFEST.md`
(`c4b64c0e…`) : section « Added on 12 November 2026 ».

## Exclus, et pourquoi

- Journaux bruts des relais (`journal-kimi.jsonl`, `relais-*.sortie`) et consoles des machines : journaux de fournisseurs (R-2389).
- Manifestes de course, registres de dépense cumulée, fiches des serveurs : pièces de travail.
- `rapport-arret-operateur-course-v66-v1.md` : porte l'adresse IP d'une machine détruite. `rapport-arret-poste-local-course-v66-v1.md` :
  nomme des chemins du dépôt de travail hors du périmètre (dont une note d'une autre course) ; résumé seulement sur la page.
- Les 50 mondes plantés neufs (GO-2026-11-12-05) : privés ; rien d'eux dans la chaîne publiée (vérifié par la liste des fichiers).
  Le jeu planté de la course (`exemples/jeu-plante-boucle-reelle-v65.md`) est publié : il est écrit dans le texte scellé v1, public
  depuis `ef4e202` (116 de ses 118 lignes distinctes non vides se retrouvent dans le texte v1 ; les 2 autres sont son en-tête) ; il n'est jamais servi aux proposeurs (garde 23).
- Aucun fichier lu sous `diag/`, `runs/`, bras d'attaque, mode tenu à l'écart, 7a ou 7b.

## Garde des secrets

Motif de la consigne (clés Anthropic, de forme « sk- » longue, GitHub, Hugging Face, AWS, Google) sur chaque objet neuf poussé (109 objets de `ef4e202..83c456d`, blobs et
messages) : **0**. Aucune archive (zip, tar, paquet) dans l'arbre publié. Adresses électroniques neuves : 0 ; adresses IP :
`127.0.0.1` seulement.

## Contrôles

`git ls-remote` : `main` = `83c456d5…`. Essais de la v67 et de la lecture v66 rejoués sur l'arbre publié (après la poussée,
arbre identique) : 108 passés, 1 sauté, 134 sous-essais passés.

## Points douteux

1. Les deux rapports publiés portent des noms de serveurs loués et détruits (`organisme-v66-course`) et, dans le v1, celui
   d'un serveur d'une autre session (`lean-outillage-d1a`) ; gardés pour l'égalité des octets (non personnels, mais « noms de
   machines » au sens large). Retrait possible par une copie expurgée sous un nom neuf, si Lazar le veut.
2. Les rapports citent mot pour mot Lazar (autorisation de reprise sans texte neuf) ; publié comme écart déclaré (R-2433 :
   « tout doit être visible »), alors que la section 7 du README public disait ces mots gardés privés.
3. `README.md` public portait déjà l'adresse électronique de Lazar (section 10) : non touchée, rien d'ajouté.
4. Aucun verdict R13 des courses v66 n'existe encore : la page dit « frozen reading », pas « verdict ». La troisième tentative
   (v67) est dite « autorisée », sans aucun résultat.
5. Session et chemins du dépôt de travail (`/home/user/controle-ia-travail`, identifiants de session dans les messages des
   commits v65 à v67) partent tels quels : déjà présents dans l'historique public.
