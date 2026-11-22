# Journal des lectures du rédacteur successeur des critères de la porte G1 (brouillon 8) — v1

- **Classe C** (note de travail). Tenu par le rédacteur, pour la liste « qui a lu quoi » de la mère et pour le contre-lecteur.
- **Session** : `session_013QMaymRJueV6awv1kDtfbP`, fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Modèle : celui que j'ai déclaré à la mère dans mon message d'inscription (lu par l'outil de description de la session à 19:19, identique pour le modèle configuré, réglé et servi) et qu'elle a inscrit à la version 21 de la liste « qui a lu quoi » ; effort maximal. État au 22 novembre 2026, 19:55 ; toute suite prendra un nom neuf (R12).
- **Accords** : GO-2026-11-22-119 (remplacement du rédacteur) ; GO-2026-11-22-120 (plafond de G1 relevé à environ 7 600 USD, choix de l'énoncé laissé à Lazar seul).
- **Règle tenue** : aveugle aux issues de P3-bis, des étapes B et B bis de T0.7, des barreaux 5 et 6 et de toute course ; aucune recommandation sur le choix A, B ou C de l'énoncé du contraste.
- Heures en UTC, relevées par `date -u` ou par l'horodatage des messages.

## 1. Avant l'inscription (22 novembre 2026, 19:13 à 19:21)

| pièce | empreinte ou repère | étendue |
|---|---|---|
| `CLAUDE.md` | `605db83acc28c7fcc6d8d12de8edb41bcdb6ea7b37b717967d6fde29f5301960`, commit `37a5afed2838b69aad63333a5f79c7443080c6af` | en entier (chargé d'office) |
| message de lancement de la mère | reçu à l'ouverture de la session | en entier |
| complément d'interdits de la mère | mis en file à 19:16, lu à 19:20 | en entier |

Commandes sans contenu de fichier : empreinte de `CLAUDE.md`, identifiant du commit, description de ma propre session.
Inscription envoyée à 19:19, mise à jour à 19:21 ; accusé de la mère mis en file à 19:21:13 (version 21 de la liste).

## 2. Routine de reprise, partie mécanique (aucun contenu lu)

- Empreintes des trois documents de lancement : conformes (mode muet).
- Vérification de l'arbre scellé au commit `37a5afed` : code de sortie 1, 96 problèmes (95 « empreinte compagnon absente » sous `docs/notes/`, 1 « nom … au lieu de … » sous `registres/passations/`). Sortie gardée dans le bloc-notes, noms non lus ; empreinte de la sortie : `96ecefdde422f886835c4e0fb7c1917c496a5f801eebaa3e6541fc8f8a2e507e`. La passation du prédécesseur en comptait 91 au commit `fc11cf2eb0`.
- Tests : premier passage non concluant, environnement non installé (174 erreurs de collecte par modules absents, 89 tests sautés). Environnement installé selon `CLAUDE.md` (`.venv`, ignoré par git) ; second passage lancé à 19:52, issue à consigner ci-dessous.
- Aucun défaut échu prononcé, aucune instance inventoriée ni arrêtée (session fille).

## 3. Après l'accusé de la mère

Lu au commit `1ba23df80ff019f8c7c299bd33d8365a899faef1` de la branche `prep/g1-brouillon7-fable-v1` (la tête, `3ff33e6f`, porte un commit de plus : rien n'en a été lu) :

| pièce | sha256 | étendue |
|---|---|---|
| `registres/passations/g1-brouillon7--2026-11-22-1855.md` | `a6357b4251f7debadb01f3fc42da0dfdf9005dcb01a0fa08a1f63928b9489504` | en entier |
| `docs/notes/g1-brouillon7-fable-v1/points-ouverts-pour-lazar-brouillon7-v2-sans-recommandation.md` | `977af2c4cf8bd529c63469d72f5f03c7f77cfe251cb77289e49ccab62d4f4117` | en entier |
| `…/sas/rapport-sas-decisions-tardives-v1.md` | `65da53709d210c66…` (seize premiers signes relevés ; égale au début de l'empreinte donnée par la passation) | en entier |
| `…/sas/rapport-sas-notes-tardives-v1.md` | `4337ef2dd03bc2f2…` | en entier |
| `…/sas/rapport-sas-notes-tardives-v1-complement-1.md` | `c6d7cc17be696816…` | en entier |
| `…/sas/rapport-sas-registres-et-marqueurs-v1.md` | `3fd9eee279c0d23d…` | en entier |

Lu au commit `bf5f5458` de `main` : les deux lignes GO-2026-11-22-119 et GO-2026-11-22-120 de `registres/go.md`, par leur identifiant seulement.

Lu dans l'arbre de travail (commit `37a5afed`) :

| pièce | sha256 | étendue |
|---|---|---|
| `docs/programme-controle-ia-v2.md` | conforme à `docs/sha256sums-lancement-v2.txt` | en entier |
| `docs/brief-claude-code-programme-complet-v2.md` | conforme à `docs/sha256sums-lancement-v2.txt` | en entier |
| `docs/etat-de-l-art-controle-ia-v1.md` | conforme à `docs/sha256sums-lancement-v2.txt` | en entier |
| `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | en entier |
| `docs/decisions/decision-N-054-v1.md` | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` | en entier |
| `docs/decisions/decision-N-055-v1.md` | `371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6` | en entier |
| `docs/decisions/decision-N-056-v1.md` | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` | en entier |
| `docs/decisions/decision-N-057-v1.md` | `42180088efb2e1016251fa329421fc08ebcb13039266d278c1a6f37ced60af99` | en entier |
| `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | en entier |
| `docs/decisions/decision-N-059-v1.md` | `41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687` | en entier |
| `docs/decisions/decision-N-061-v1.md` | `b2ae441720665ed49f131e18fb7612d0d1c2a4e0cc7a0e18a301178fe5b2df54` | en entier |
| `docs/decisions/decision-N-063-v2.md` | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` | en entier |
| `docs/decisions/decision-N-066-v1.md` | `21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351` | en entier |
| `docs/decisions/decision-N-034-v1.md` | `97e33e971a8fd01cdb8ff233f25dd9c0f1fd169e9889fca9a343ecd2aa3d5993` | en entier |
| `docs/decisions/decision-N-029-v1.md` | `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4` | en entier |
| `docs/decisions/decision-N-026-v1.md` | `85bd40235f3668c66adffc2ff18139ff1a0c402f3aaa24cca70db0217f755bf0` | en entier |
| `docs/decisions/decision-N-015-v1.md` | `462785b333101c20e5a923b2155bfd5964dd4172aa896440c51e8baca3602b7b` | en entier |
| `docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` | en entier |
| `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` | en entier |
| `src/controle_ia/prereg.py` | (code du validateur) | en entier |

Vérifiés sans être ouverts (empreinte et taille seulement) : `brouillons/G1-preenregistrement-v1-brouillon6.md` (début d'empreinte `939b56e540fa49ea`, 426 lignes) ; les décisions de la liste blanche trouvées par nom exact et non lues (N-019, N-023, N-035, N-044, N-045 v2, N-047, N-049, N-050, N-052, N-060 v4, N-062, N-064, N-065).

## 4. Expositions déclarées

1. `CLAUDE.md`, résumé de N-077 : « contre un saboteur qui répond au mieux, aucune des trois interventions ne garde de marge ». La mère la porte dans la cellule « a lu » sans la compter comme exposition aux issues interdites.
2. Note des 21 points v2 : l'issue en un mot de l'étude par simulation de la formulation (« non tranché ») et les avis du rédacteur de N-074 et de son contre-lecteur sur les trois énoncés. Je n'en tiens pas compte ; aucune recommandation de ma part sur A, B ou C.
3. Rapport du sas des registres : existence d'un second cycle sur l'accumulation « après le verdict du barreau 6 » et accord de principe du contraste à témoin apparié « après le verdict scellé du barreau 6 », sens caviardé. Une inférence est possible ; je ne la fais pas et le texte n'en tire rien.
4. Même rapport : mot de Lazar du 8 novembre, « si les sondes ne lisent pas le sabotage, on les reconçoit », à propos d'une lecture antérieure dont le sens est caviardé.
5. Premier test boîte blanche (P3) : N-026 parle du « nul » que le bras de diagnostic doit expliquer ; N-029 cite un chiffre de la lecture de P3 (ce que le coût déclaré seul y sépare) ; le sas nomme « la borne de détection du nul de P3 ». Je connais donc le sens de P3 et ce chiffre, que je ne recopie pas ici. Ce sont des pièces de la liste blanche.
6. N-054 cite un accord d'étiquetage du pilote, « fait du pilote, non un seuil » ; non recopié ici.

## 5. Non ouverts

Le brouillon 2 de N-074 et son brouillon 1 ; les huit fichiers du complément de la mère et leurs compagnons ; la note du juge sur l'exposition ; tout verdict ; toute note de lecteur ; `registres/decisions.md` ; `registres/etat.md` ; `registres/rappels.md` ; la liste « qui a lu quoi » ; le coffre ; le bras d'attaque ; les pièces du saboteur ; `docs/verdicts/`, `diag/`, `runs/` ; le journal des commits (aucun sujet de commit affiché) ; aucun dossier listé hors `…/g1-brouillon7-fable-v1/sas/` au commit nommé.
