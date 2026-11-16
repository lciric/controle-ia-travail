# Vérification neuve (modèle C) de la section 15 jouée pour la mère après la phase B — v1

- **Statut** : vérificateur neuf (R2), n'a rien écrit de ce qui est vérifié ; fichier neuf, scellé, non commité. Écrit à partir du 2026-11-16T21:18:12Z (`date -u`).
- **Déclaration** : de 7b, je n'ai rien ouvert hors le booléen de l'audit R4 de la base (A), rejoué par `lecture_audit_r4_base_a_mere_v1.py` (`2e486465…`) sur une extraction par `git show` dans un dossier neuf, effacé ensuite par son chemin exact ; des sorties de la pièce, seulement des empreintes, objets et tailles. Aucun fichier de la liste interdite, rien de B bis lu hors les lignes du registre des décisions et de la liste citées ci-dessous. Aucun refus de permission.

## Verdict : conforme

Les six points tiennent. Trois réserves de forme ou de portée, aucune ne bloque la remise (§ 7).

## 1. Bloc V rejoué (empreintes, objets, tailles ; aucun contenu)
Texte du bloc V de la section 15 (point 1) de `commande-compte-3-phase-b-v3.md` (`7090cdf0…`), variables de tête remplies avec le rendu de l'hôte, joué à 2026-11-16T21:16:19Z : **code 0**. Parenté `034ba39f` → `eacc5cae` ; `034ba39f` ancêtre de `origin/verdict/t06-mots-et-cout-compte-3-v1` ; `eacc5cae` ancêtre de `origin/main` ; 8 fichiers, tous ajoutés, tous des sorties de la pièce ; chacun égal à son compagnon ; les quatre lignes égales à celles du rendu de l'hôte à l'octet (`a2113f9a…` 81820 ; `1b84d7c4…` 8098 ; `f299b654…` 1056569 ; `4ca1f993…` 18943). Tête de la branche relue : `8b6b0303736fd3a9bf029832244a159a92a04bf7`, égale au rendu. Le rendu de l'exécutant (bloc V à 21:00:48Z, mêmes quatre lignes) est identique.

## 2. Lignes de `registres/scellements-v1.md`
Sur `origin/main` : `LECTURE-T08-BASE-A` (2026-11-16T21:01:43Z, ligne 18) puis `ISSUE-MOTS-ET-COUT-T06` (21:02:42Z, ligne 19), dans cet ordre, **dernières lignes du fichier**. Chemins et empreintes égaux au rendu (`a2113f9a…`, `1b84d7c4…`). Chaque commit (`ccf3936a`, `3f979eb2`) n'ajoute qu'une ligne, au seul fichier du registre. Aucune autre ligne ajoutée, aucune clé de verdict.

## 3. Ligne dédiée de BA-L2 (R-3018, R-2991)
Une seule ligne `R-3018` (numéro = plus grand `R-` précédent, R-3017, plus un). Chaînes exclusives : « BA-L2 » présent (1) ; « ne s'applique pas » présent à l'apostrophe droite (1) ; « mot de Lazar » absent (0) ; les sept fragments de `INTERDITS_CONTENU_B` de la commande phase C v4 (l. 168) : 0. La ligne cite la commande v4 (`f4bcf406…`), le programme (`6d63e9d6…`, empreinte relue égale), la branche et la tête `8b6b0303…`. Bloc M daté 21:03:05Z, strictement après `LECTURE-T08-BASE-A` (21:01:43Z). Commit `065e37c4` : ce seul fichier (`registres/decisions.md`).

## 4. Ordre de l'audit R4
Rejoué : « audit R4 de la base (A) : non déclenché », code 0, sur le fichier et son compagnon extraits de `034ba39f` (empreinte `a2113f9a…`). L'ordre « lu après la première ligne, avant la seconde » repose sur les heures du système : première ligne 21:01:43Z (commit 21:02:09), seconde 21:02:42Z (commit 21:02:42, dont le message nomme l'audit), et la déclaration de l'exécutant ; **je n'ai pas de trace horaire propre de la lecture elle-même** (le journal provisoire n'est pas lu). Aucune contradiction ; le non-déclenchement rend la relecture par un lecteur neuf sans objet (GO-2026-11-16-07, point 3).

## 5. Pièces préparées pour la phase C
- Liste `registres/qui-a-lu-quoi-v3.md` : `3188e8af…` = compagnon. Attestation v3 (`a20f137c…`) rejouée par moi sur le fichier versé, avec la `CELLULE_HOTE` de la commande v4 (l. 162) : « CONFORME … lignes de l'hôte admises : 1 », code 0. Essai versé (`1a68f36b…`) : cas sain code 0, quatre artefacts code 2 ; script `c19348f1…`. Lignes de tableau 1 à 165 : identiques au brouillon 1 (`c973c8bf…`) sauf la ligne 134, dont seules les colonnes « a lu », « rôle » et « source » changent ; « exclu de » = `CELLULE_HOTE` exacte. Lignes 166 à 186 neuves (21 lignes). L'en-tête cite la commande v4 (`f4bcf406…`).
- R-3019 (faits de la phase B, sans valeur, correction de R-2778 : le texte porte bien « après l'étape B »), R-3020 (R-V1), R-3021 (R-V2, cite la consigne `1fa37cbc…`, empreinte relue égale, et la commande v4 `f4bcf406…`, relue égale) : présentes une fois ; numéros uniques.
- `remise-phase-c-v4-pieces-v1.md` (`f02b4508…`, compagnon égal) : huit marqueurs conformes au `1fa37cbc…` et à la liste ; brouillons R-V4 et R-V5 adaptés à la v4 (non inscrits, dit) ; brouillon du message à Lazar sans nom de modèle (« <nom, jamais écrit dans un fichier> ») ; liste de ce qui manque honnête.

## 6. Étanchéité, identifiants de modèle, poussée
- Aucun identifiant de modèle (aucun nom de modèle, relevé par recherche insensible à la casse) dans la liste, la remise, l'essai ni son script ; seules les lettres « modèle A, B, C » figurent.
- Les six commits (`ccf3936a`, `3f979eb2`, `065e37c4`, `bcdbbc27`, `8917d28b`, `6808dea1`) ne touchent que les registres, la liste, l'essai et la remise ; R-3018 à R-3021 sans mot de B bis. Les mentions de B bis dans la remise sont les deux marqueurs que la commande exige (`REGISTRE_BBIS`, `CLE_PLAN_BBIS`), une déclaration de non-lecture et le brouillon R-V5. Rien du contenu de B bis.
- `origin/main` = `HEAD` = `6808dea1` : les six commits sont poussés.

## 7. Réserves (aucune bloquante)
1. **Liste v3 sans vérification courte par un agent neuf** (réserve 9 de la liste, déclarée). Je ne l'ai faite que pour les points ci-dessus (recopie, ligne 134, attestation) ; je n'ai pas relu la véracité de chaque ligne 166 à 186. Une version 4 changerait `EMPREINTE_LISTE`.
2. **Lignes 180 à 184 de la liste** décrivent des agents de l'étape B bis (incident déclaré de la ligne 181, machines louées de la ligne 184) d'après le registre des décisions : des faits d'exécution, aucun résultat, sans équivalent dans R-3018 à R-3021. La liste n'est pas dans le bordereau du lecteur B ; l'exclusion « au sens large » est à confirmer par la mère (réserve 4 de la liste).
3. **Durée de la phase B non rendue** (déclarée à R-3019) ; le point (a) de R-V5 (R-2714, R-2716, R-2740) n'est pas revérifié (dit par l'exécutant) ; `verifier-arbre` rend des problèmes préexistants hors de ces fichiers (non rejoué).

Fin : 2026-11-16T21:18:12Z (`date -u`).
