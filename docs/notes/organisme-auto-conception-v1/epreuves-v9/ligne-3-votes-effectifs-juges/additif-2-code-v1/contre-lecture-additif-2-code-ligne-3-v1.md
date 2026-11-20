# Contre-lecture de l'additif 2 (code) de la ligne 3 — v1

Pièce de travail (classe C), 2026-11-20. Contre-lecteur neuf pour cette pièce : je n'ai pas écrit l'additif (j'ai vérifié le code v3). Rien écrit dans le dépôt, rien sous `/root/.claude/`, aucun lancement du banc, aucun calcul de l'étage 1, aucun refus d'outil. Python 3.13.18, numpy 2.5.3 chez moi.

## Verdict : **Conforme après corrections** (deux corrections de texte, aucune ne touche un calcul ni un critère gelé)

Pièces lues : l'additif (`65609405…`, égal à son compagnon, 175 lignes, en entier), le rapport du rédacteur (`54ace9f1…`, égal à son compagnon, en entier), le banc et le chronomètre v3 (plages : en-têtes, graines, `verifier_autorisation`, `generateurs`, `Contexte`, `commit_du_depot`, `construire_manifeste`, `main`), le texte v7 et l'additif 1 v2 relus sur `origin/main` (`git show` redirigé ; empreintes `4e3680d9…` et `e1c1ee84…` égales).

## 1. Commit et empreintes
- `git rev-parse 380db356…` rend l'identifiant donné ; `git merge-base --is-ancestor` : `380db356` est ancêtre de `lot/compte-organisme-v1` ; `4bbd3676` (additif 1) est ancêtre de `origin/main`.
- Recalculé sur disque : banc `09bfe0db…`, chronomètre `8cb61afb…`, essais `28ad0e89…`, contrôle `b4078e71…`, comparaison `4209748a…` et sa sortie `17ebe555…`, rapports de défauts `343f0f77…` et `586e6f45…`, rapport du développeur `ae1fa1da…`, vérification `bd2773e2…`, quatre journaux et quatre différentiels : **les 18 empreintes du § 3 sont égales**, entières.
- Recalculé sur le commit (`git show 380db356:… ` redirigé) : banc, chronomètre, essais et contrôle ont les mêmes sha256 que sur disque. Les octets du disque sont ceux du commit.

## 2. Commandes de lancement
Les deux commandes recopient mot pour mot l'en-tête « Usage » du banc (`--decisif --autorisation-additif CHEMIN --empreinte-additif HEX --sortie DOSSIER_NEUF`) et du chronomètre (`--autorisation-additif CHEMIN --empreinte-additif HEX --manifeste DOSSIER`). Les `argparse` des deux programmes (banc 1726-1737, chronomètre 120-129) portent bien ces options ; `--decisif`, `--autorisation-additif`, `--empreinte-additif`, `--sortie` sont requis au banc ; au chronomètre l'autorisation est exigée hors `--essai` (refus par `verifier_autorisation` sinon). Dossiers déjà présents refusés dans les deux. Conforme.
**Réserve (correction A)** : `CHEMIN` est donné « tel que la mère l'a scellé » et les commandes se lancent « depuis le dossier du code » ; or `verifier_autorisation` ouvre le chemin par rapport au dossier courant. Un chemin relatif au dépôt échouerait (« additif absent »), un autre chemin relatif au dossier du code donnerait une autre écriture au manifeste. Voir correction A.

## 3. Racines
- Code : 2026111930 essais (seule sans autorisation) ; 2026111931 chronométrage (`MODES`, `main` du chronomètre) ; 2026111932 tirages et 2026111933 rééchantillonnage dans le mode `decisif` (`MODES`) ; 2026111934 à 2026111937 refusées avant toute dérivation par `generateurs` (ligne 152) ; `RACINES_SOUS_AUTORISATION` = 31, 32, 33, chacune soumise à `verifier_autorisation` à chaque dérivation. L'additif dit la même chose (§ 4).
- Texte v7, « Graines (règle R9), ordre des gestes » (ligne 303) : 2026111930, 31, 32, 33 aux mêmes rôles ; 34 composition de la banque, 35 ordre des appels, 36 rééchantillonnage de l'étage 2, 37 plis de l'audit : égal. Additif 1 (choix 18, « Ordre des gestes, complété ») : l'autorisation de 31 à 33 est l'additif de code, par chemin et empreinte ; ordre : additif de code scellé, chronométrage, étage 1 une fois : égal. Le texte (en-tête, geste 3) demande l'additif « scellé par la mère avant tout tirage de l'étage 1 » : l'additif § 4 le reprend. Rien n'est changé. La limite dite au § 4 (le code ne lit pas le contenu du fichier d'autorisation) est exacte.

## 4. `comptes_du_melange_plante`
La configuration décisive de l'alarme est `{"m": [10, 20, 40], "suites": 2000}` (banc 1425) ; `change = idx < R // 2`, `effet = idx < R // 4` : suites qui changent 1 000, à effet 500, sans effet 1 000 − 500 = 500, sans changement 1 000. **Les valeurs 1 000 / 500 / 500 / 1 000 sont exactes**, et l'ordre donné par l'additif (changent, à effet, sans effet, sans changement) est celui des quatre clés. Le rôle décrit (dénominateurs de P6) est celui du code (`criteres_alarme_p6`). L'additif 1 dit « 2 000 suites » (ligne 63) : égal. Conforme.

## 5. Règle de lancement et champ `depot`
- § 7.1 : exact — `commit_du_depot` lance `git -C DOSSIER_DU_BANC rev-parse HEAD` et `status --porcelain -- DOSSIER_DU_BANC` (banc 1689-1700, inchangé depuis le v2) ; dossier pris dans `__file__`, donc indépendant du dossier courant.
- § 7.2 : comparaison de `programme_sha256` et `programme_chronometrage_sha256` : ces deux champs existent (banc 1707 ; chronomètre 155). Le chronomètre charge le banc voisin : exact tant que `BANC_LIGNE_3_CHEMIN` n'est pas posée (celle-ci est lue par les essais et le contrôle, non par le programme du chronomètre décisif que j'ai lu : le point est sans conséquence).
- § 7.3 : exact, la tête du dépôt est celle du lancement. **Omission (correction B)** : le champ `depot` porte aussi `dossier_du_code_propre`, qui vaut `False` si le dossier du code contient quoi que ce soit de non committé ou de non suivi, et `None` si git est introuvable ; l'additif ne dit ni ce que ce champ signifie ni ce que la mère en fait.
- § 7.4 et 7.5 : conformes à l'additif 1, point J.
- § 8 : le banc écrit bien chaque fichier avec son compagnon `.sha256` (`ecrire_json_exclusif`, banc 1657-1662).

## 6. Points ouverts du rédacteur
- **Lieu des sorties.** Sa lecture est **juste, et plus large qu'il ne le dit**. Au banc, le fichier de résultat (avec son compagnon) est écrit **avant** la construction du manifeste (`executer_etage_1`) : un `DOSSIER_NEUF` sous le dossier du code y apparaît comme chemin non suivi et le manifeste porte `dossier_du_code_propre: False`. Au chronomètre, le dossier est créé vide avant le manifeste (git ne signale pas un dossier vide) : son propre manifeste reste « propre », **mais** son manifeste, écrit ensuite, reste sous le dossier du code et rendra « non propre » le manifeste du banc lancé après. Même chose pour un `__pycache__` si `-B` est oublié. Un dossier de sortie sous le dossier du code est donc à interdire pour les deux commandes, et le dossier du code doit être strictement celui du commit au lancement.
- **Version de numpy.** Le manifeste de chaque exécution la consigne (`versions.numpy`, banc 1713) ; le texte exige numpy ≥ 1.25. Relevé chez moi : **2.5.3** (`pip show`), la même que celle que le développeur de la version 2 avait déclarée ; le rapport du développeur v3 ne la porte pas. À écrire dans l'additif comme valeur attendue du manifeste, ou comme valeur relevée sans condition : voir correction C (facultative).
- Contenu du dossier du code (aucune liste lancée) : je ne l'ai pas listé non plus ; le point ne peut se juger que par la règle de lancement, qui l'écarte déjà.

## 7. Rien de gelé ne change ; identifiants de modèle
Aucune hypothèse, prédiction, seuil, critère de lecture, règle gelée, racine ni montant n'est changé : l'additif nomme le code et déclare ses limites. Les ajouts du § 5 sont ceux de l'additif 1 plus la clé `comptes_du_melange_plante` que la vérification avait demandé de nommer. L'additif ne contient aucun identifiant de modèle (seulement les lettres de rôle « F », « L′ », « S » usitées dans le dépôt).

## Corrections demandées (texte exact)
**A. § 6, puce `CHEMIN`.** Remplacer « `CHEMIN` : le chemin de cet additif tel que la mère l'a scellé. » par : « `CHEMIN` : le chemin **absolu** du fichier de cet additif scellé, tel qu'il existe sur la machine de l'exécution (le code ouvre le chemin par rapport au dossier courant, qui est le dossier du code ; un chemin relatif au dépôt serait refusé). La mère compare le champ `autorisation.chemin_additif` du manifeste à ce chemin et `autorisation.empreinte_additif` à `HEX`. »

**B. § 7, point 1 et point 3.** Ajouter au point 1 : « **`DOSSIER` et `DOSSIER_NEUF` ne sont jamais placés sous le dossier du code** : le banc écrit son résultat avant son manifeste, et le manifeste du chronométrage resterait sous ce dossier ; dans les deux cas le champ `depot.dossier_du_code_propre` du manifeste de l'étage 1 vaudrait `false`. » Ajouter au point 3 : « Le champ `depot.dossier_du_code_propre` vaut `true` si `git status --porcelain` borné au dossier du code ne rend rien ; la mère le lit à l'exécution : `false` ou `null` rend l'exécution suspecte et se rend à la mère, sans lecture des mesures ; l'identité du code tient toujours à `programme_sha256`. »

**C (facultative). § 6, ligne « Environnement ».** Remplacer « La version de `numpy` n'est pas écrite dans les rapports ; le manifeste de chaque exécution la consigne. » par : « Version de `numpy` relevée par le contre-lecteur : 2.5.3 ; le texte exige numpy ≥ 1.25 ; le manifeste de chaque exécution la consigne (`versions.numpy`), sans qu'une valeur précise soit imposée. »

Contre-lecteur, modèle S.
