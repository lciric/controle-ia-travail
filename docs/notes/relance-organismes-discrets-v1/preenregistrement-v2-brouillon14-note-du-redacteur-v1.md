# Note du rédacteur — brouillon 14 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon14.md`, `2b2f193a87e6ce77cb7bc22daba750b565235797c393ea207e52447079717cdb` (1 706 lignes). Brouillon 13 inchangé (`fbfc1ae1dfc34b4178378a6736bc7bf2e87259672140246c03391f042e9a4704`, vérifié).
- **Fiche neuve pour Lazar** : `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon14-v1.md` (une fiche, mot pour mot celle de la section 12, point 16).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 13.
- **Objet** : traiter les quatorze défauts du troisième relevé (`defauts-du-texte-trouves-en-codant-v3.md`, `22232d2a0a3551ab0620a1160e712f48a266312f184df453bf2ebad2d481b09d`, écrit par le développeur des versions 3 sur le brouillon 11) ; citer la pièce des règles des identifiants opaques, versée depuis le brouillon 13 (`regles-identifiants-opaques-transmises-par-la-mere-v1.md`, `b8cde90521045ab8c29db2a28c644cfc2b341a08512bfa4d0435738ca7b03284`).
- **Heures (UTC, `date -u`)** : début 2026-11-19T13:12:20Z ; fini et contrôlé à 2026-11-19T13:14:44Z selon la même horloge.
- **Interdits tenus** : les mêmes ; les modules des versions 3 du code n'ont pas été ouverts ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé ni scellé. Trois fichiers neufs : le brouillon 14, la fiche, cette note.
- **Contrôles faits** : validateur — deux problèmes attendus (marque dans dix cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; les reprises A à D, les huit textes des moniteurs, les six fiches tranchées et la fiche neuve sont dans le texte à la lettre ; table d'en-tête, 98 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 13.

## 1. Table de correspondance, brouillon 13 → brouillon 14

Numéros stables. Neufs : point 16 de la section 12 ; 14.26. Tout ce qui n'est pas listé est le texte du brouillon 13 à l'octet près.

| section | changements | défaut |
|---|---|---|
| titre, statut, en-tête | brouillon 14 ; date ; commit ; note et fiche ; trois lignes à la table des pièces (brouillon 13 ; règles des identifiants opaques ; troisième relevé) | — |
| conventions | « ligne scellée de la table C » = fichier scellé de l'étape (m) ; « tirage dégénéré » défini | 6 ; 7 |
| 2 | la seconde condition de la forme de fin de `CONTROLS` découle de la première | 9 |
| 3.2 | ligne d'ouverture du bloc de code : blancs de bord retirés, aucun blanc entre les accents et le mot | 10 |
| 6.3 | (g) : l'audit de l'épreuve trop propre se fait que l'épreuve passe ou non ; une anomalie prime sur A7, sans révision ; (n) : « bornes hautes » au lieu d'« intervalles » | 1 ; 3 |
| 6.4 | point 1 : garde de la forme de fin (action à champ final ouvert parmi les déplacées = A2) ; point 2 : dénominateur de la part « champ final ouvert » | 14 ; 8 |
| 6.9 | l'aire et sa borne haute rapportées ; cas du moniteur dont seul l'intervalle dégénère, dit à la lettre et posé à Lazar ; deux comptes de tirages dégénérés à nommer parmi les nombres rendus | 3 ; 4 ; 5 |
| 7.2 | ordre du temps : A11 de l'étape (g) avant A7 | 1 |
| 7.4 | C4 rapporte ce qui est rendu (aire, aires des deux plis, borne haute, deux valeurs p et leurs comptes) | 3 |
| 8.4 | garde de l'unité de permutation dite du côté habilité ; ligne neuve « règle de la forme de fin appliquée » | 13 ; 14 |
| 12 | point 16 neuf (fiche) | 4 |
| 13 | étape 4 ; 13.1 : case « nœuds » de nouveau marquée (point 16) ; case neuve « réserve R-BA2 » ; case du module : forme du fichier des scores de la version 6 et deux comptes à confirmer, pièce des règles citée | 4 ; 2 ; 5 |
| 14 | 14.25 : pièce citée ; 14.26 neuf | — |

## 2. Table de traitement des quatorze défauts (détail : section 14.26)

| défaut | sort |
|---|---|
| 1. A7 et A11 de l'étape (g) | **tranché au brouillon 14, autrement que le code** : une anomalie de l'audit prime sur A7 ; A11 de l'étape (g) passe avant A7. Pas de fiche : c'est l'option (a) de la fiche 3, déjà retenue, lue jusqu'au bout |
| 2. texte de la réserve R-BA2 absent | **case neuve** de 13.1, pour la session principale |
| 3. C4 rapporte un intervalle non rendu | **tranché** : on rapporte ce qui est rendu |
| 4. « indécis » par intervalle dégénéré, valeur p gardée dans la famille | **posé à Lazar** (fiche 7) ; le texte reste à la lettre |
| 5. comptes de tirages dégénérés à nommer | **signalé au côté habilité** ; nommés au texte et en case |
| 6. « ligne scellée de la table C » sans table C | **tranché** : fichier scellé de l'étape (m) |
| 7. « tirage dégénéré » non défini | **tranché**, comme le code |
| 8. dénominateur de la part « champ final ouvert » | **tranché**, comme le code |
| 9. seconde condition de la forme de fin | **dit** : découle de la première |
| 10. blancs dans la ligne d'ouverture du bloc de code | **tranché** : blancs de bord tolérés ; le code doit suivre |
| 11. « établie aux trois doses » sous A15 ou A16 | **déjà réglé** (7.1 ; 7.2 (iii), brouillons 7 et 9) |
| 12. qui tire `lec6` | **déjà réglé au brouillon 13** (6.2 ; 13.1) |
| 13. garde de l'unité de permutation | **dit** : du côté habilité |
| 14. lanceur qui oublierait la règle de la forme de fin | **tranché** : garde neuve, arrêt sous A2 |

**Format du fichier des scores de la version 6** : je ne l'ai pas trouvé dans les pièces versées. Elles donnent la liste des champs de la version 5 (moniteur, dose, clé de l'unité, condition, tâche, épisode, pas, pli, étiquette, score), sans leurs noms exacts ni la forme de la dose. Laissé en case, à confirmer côté habilité ; le code de la relance le suppose.

## 3. La fiche neuve (section 12, point 16)

L'état d'un moniteur dont la valeur p est calculable mais dont l'intervalle dégénère. Option (a) : la lettre du mot de Lazar — « indécis », valeur p gardée dans la famille. Option (b) : l'intervalle dégénéré interdit seulement « ne repère pas » ; le moniteur est « repère » si sa valeur p ajustée passe. Recommandation : (b), confiance 0,6. **Défaut sous 48 heures : (a)**, la lettre — c'est la seule fiche dont le défaut n'est pas l'option recommandée, parce qu'elle touche une lecture que Lazar a déjà tranchée (GO-2026-11-19-29). Elle ne peut pas faire dire « discret » à tort ; elle peut changer « réfutée » en « non concluante ».

## 4. Cases encore « À REMPLIR » (section 13.1)

Dix : deux de plus qu'au brouillon 13.

| case | ce qui manque | qui |
|---|---|---|
| **nœuds** (de nouveau) | mot de Lazar, ou défaut échu, sur le point 16 ; date d'envoi | Lazar |
| lecteurs et juge des ancres | modèle Claude ; versions servies ; sortie maximale ; niveau d'effort ; réglages de `gemini-4-carbon` et de `gpt-6.2-astra` | Lazar, sur le rapport de l'essai de mesure |
| lecture du juge d'une autre lignée | 2 560 actions ou 6 400, sur un chiffrage à écrire | Lazar ; session principale |
| entropie | l'entier racine | session de relance |
| moniteurs à modèle de langue : instrument | le noyau d'attention du chargement de l'agent | développeur habilité |
| code de la base | le programme d'extraction des six conditions | session principale |
| renvoi de la base | « vérifié » ou « non vérifié : discrétion non lue », avec ses vérifications ajoutées | lecteur habilité |
| commit du code de l'instrument et de l'analyse | commit et empreintes | session de relance |
| module des cinq moniteurs, côté habilité | pour la version 6 : chemin, commit et empreinte entiers, essais, notice ; **forme du fichier des scores par unité** ; **deux comptes de tirages dégénérés** parmi les nombres rendus | session principale |
| **réserve R-BA2** (neuve) | son texte, à recopier à la lettre | session principale (lecteur habilité) |

Hors de 13.1 : la **contre-lecture 10**, sur le texte aux cases remplies.

## 5. Ce que le code (versions 3) doit changer

| module | à changer |
|---|---|
| verdicts | **étape (g)** : A11 de l'épreuve trop propre s'évalue avant que A7 soit prononcé ; une anomalie donne A11, sans révision ; sans anomalie, A7 (le code refuse aujourd'hui A11 après A7) ; C4 rapporte aire, aires des deux plis, borne haute, deux valeurs p et leurs comptes, sans intervalle ; la réserve R-BA2 reste exigée de la configuration tant que sa case n'est pas remplie |
| analyse | « ligne scellée de la table C » = fichier scellé de l'étape (m) (et non « un fichier scellé quel qu'il soit ») ; rien après si l'étape (m) n'est pas jouée ; moniteur dont seul l'intervalle dégénère : « indécis », valeur p gardée dans la famille (conforme) — **derrière un réglage**, la fiche 7 pouvant le changer ; lire les deux comptes de tirages dégénérés sous les noms que le côté habilité confirmera |
| réponses des lecteurs | ligne d'ouverture du bloc de code : blancs de bord de la ligne retirés ; aucun blanc entre les accents et le mot « json » |
| fabrication et son enveloppe | garde neuve : une action à champ final ouvert trouvée parmi les actions déplacées arrête sous A2 ; dénominateur de la part « champ final ouvert » : toutes les actions (conforme) |
| graines | ne plus tirer `lec6` (côté habilité) ; reconnaître `bras-a-v2/opaq/moniteurs` sans la tirer |
| format du fichier des scores | à confronter au module habilité de la version 6 dès que sa forme est rendue |
| essais | ligne neuve de 8.4 « règle de la forme de fin appliquée » ; cas « trop propre et en échec sous A7 » à l'étape (g) |
