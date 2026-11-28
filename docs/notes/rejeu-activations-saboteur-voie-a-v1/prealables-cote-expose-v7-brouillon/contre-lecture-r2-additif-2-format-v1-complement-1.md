# Contre-lecture (règle R2) de l'additif 2 — complément 1 : extrait du côté exposé (D-13) et deux questions fermées sur la lecture scellée

- **Rattaché à** : `contre-lecture-r2-additif-2-format-v1.md` (`bfcb0f975b32a3fb3ec4ecff550169355525d42ec56312263d4d58492c7ae8b3`), qu'il ne réécrit pas (règle R12).
- **Demande** : deux messages de la session mère (`session_016QhUrvi45g3jX5saFefVED`), le 2026-11-24 à 06:39Z et 06:44Z.
- **Même contre-lecteur, même cloisonnement** : rien n'a été ouvert sous `diag/`, `runs/`, `donnees/`, `coffre/` ni `docs/verdicts/` ; aucun épisode, aucun score, aucun texte d'action. Aucun contenu de sonde n'est recopié ici.
- **Écrit** le 2026-11-24 vers 06:50Z (`date -u`).

## (A) Extrait du côté exposé `extrait-cote-expose-d13-v1.json` (`1ff87c08f5170fa7319349aa8cc1fc17a72689bcadd52295aff7856a0fbf992f`, égal à son compagnon)

**Mécanique : oui. Cohérent avec l'additif 2 : oui**, avec deux remarques mineures.

Vérifié par programme (lecture JSON stricte, clés répétées refusées) contre la forme fermée de D-13 du texte scellé (ligne 98) :
- exactement six clés (`avertissement`, `commit_lancement`, `etats_par_lot_evaluation`, `fichiers_de_la_passe`, `run_id`, `versions`) ; `avertissement` égal à la chaîne constante du texte scellé ; `run_id` de la forme `AAAAMMJJ-HHMMSS-` puis minuscules, chiffres et tirets ; `commit_lancement` de 40 caractères hexadécimaux minuscules ;
- `versions` : dix clés, toutes dans la liste admise, triées ;
- `etats_par_lot_evaluation` : quatre lignes de six clés, rangées `H`, `B50`, `B100`, `TJ100`, un lot par condition, `adaptateur` et `dose_apres` égaux à la fiche version 7 et à la table de la note (question 5) ;
- `fichiers_de_la_passe` : trois clés, empreintes de 64 caractères, chemins et empreintes égaux à ceux de M-2 de l'additif 2 et de la note version 7 (point (b)). Cet écart aux « quatre clés sous `donnees/<run_id>/` » du texte scellé (ligne 98) et de RP-11 de l'additif 1 est exactement celui que M-2 couvre ;
- aucun chiffre hors des doses, des numéros de lot, des versions, des empreintes, du commit et du nom du run ; aucun mécanisme.

Remarques mineures :
1. **Empreinte des lignes d'état.** Le champ `empreinte` des lignes d'état (`40ff8fde…` pour l'élève, `d10d7379…` pour le témoin-jumeau) diffère des empreintes des fichiers d'adaptateurs (`9c7808fb…`, `67ea25de…`). Le texte scellé dit que `empreinte` n'est « comparée à rien » (ligne 98) : rien n'arrête, mais un lecteur pourrait y voir un désaccord. Correction proposée à l'additif 2 (M-2) : une phrase disant que ce champ est l'empreinte relue par la course au chargement, distincte de celle du fichier, et qu'elle reste non comparée.
2. **Épinglage de l'extrait.** L'additif 2 ne cite ni le chemin ni l'empreinte de l'extrait. Correction proposée : les écrire dans M-2 (chemin définitif après versement, empreinte `1ff87c08…`), pour que P1 et le bordereau l'épinglent comme les trois fichiers.

## (B) Deux questions fermées sur la lecture scellée (texte scellé `8e432cdc…` lu avec l'additif 1 `fc5b0610…`)

**(B1) La lecture scellée exige-t-elle l'activité brute de toutes les actions à chaque couche capturée ? — Non.**
- Le texte scellé retient l'option (t1) : « scores par action et sous-échantillon brut » (`prereg/lecture-sondes-barreau8-v1.md`, ligne 210) ; l'activité brute de toutes les actions est écartée (lignes 201, 202, 212 : hors de la borne de 2 Go).
- Le sous-échantillon brut est de 161 actions à la couche 15 et de 21 aux couches 7 et 23 (lignes 207, 208, 246) ; il ne sert qu'à la garde de réception r6, qui recalcule les scores (ligne 277), et aux gardes P7 et P10 (lignes 295, 298).
- Le verdict se lit sur les scores d'action livrés de toutes les actions, calculés par la passe sur tous les jetons notés (lignes 130, 240, 243) ; la garde P5 exige, pour chaque action, autant de positions capturées que de jetons notés (ligne 293), sans les enregistrer.
- L'additif 1 n'ajoute aucune exigence d'activité brute : ses lectures descriptives se calculent sur les scores d'action livrés (`prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md`, lignes 472 et 484) ; RP-7 (ligne 442) ne reporte que le pas du sous-échantillon.

**(B2) La lecture scellée exige-t-elle la capture du jeton qui précède le champ révélateur ? — Non.**
- Les positions capturées et notées sont « tous ses jetons notés : les identifiants de l'action du premier au dernier, le jeton final exclu s'il est un jeton de fin » ; « le contexte est parcouru par la passe avant ; rien n'en est enregistré » (texte scellé, ligne 240). Même lettre pour le score d'action (ligne 130).
- Aucune phrase du texte scellé ni de l'additif 1 ne nomme un « champ révélateur » ni une position définie par rapport à un champ : une recherche des mots « révél », « précède », « jeton précédent », « dernier jeton du contexte » ne rend, au texte scellé, que la longueur du contexte comme prédicteur trivial, lue dans l'index (ligne 136), qui ne demande aucune capture. Le devis v2, qui ne prévoit pas cette capture, est donc conforme sur ce point. Une telle capture serait une lecture non prévue : une nouvelle passe, une version nouvelle du texte et un accord de dépense (ligne 249, point 1).
