# Note du rédacteur — brouillon 42 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même rôle que pour les brouillons 21 à 41. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon42.md`, `c5dbd28eca7b2a244a494400ae0180bcace68b76d3861d7e35822decd68ef0de`, scellé comme brouillon. 2 479 lignes.
- **Point de départ** : le brouillon 41 (`cb6ca087d3d4c46dcd70e2a2f2f41ea765d05891f36a5fc1747f5cab2b088df4`), inchangé.
- **Heures (UTC, relevées par `date -u`)** : commencé après le mot de Lazar relevé à 10:28:55Z ; interrompu par une limite d'usage du modèle, sans qu'aucun fichier soit écrit, ce que j'ai vérifié à la reprise ; repris depuis le début (premier relevé : 2026-11-21T10:52:19Z) ; texte scellé à 10:57:42Z ; note finie vers 11:02Z.
- **Méthode** : 40 remplacements exacts, chacun sur une ancre trouvée une seule fois ; cinq d'entre eux remplacent un passage borné par deux ancres uniques, sur une même ligne. Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé.
- **Pièces traitées** :
  - le mot de Lazar « b a b go », `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604df20181e9ea0fdcf15fbd88601f98f96388ce32d23d7c0a98e5a` ;
  - la vérification du brouillon 41, `docs/notes/relance-organismes-discrets-v1/verification-brouillon41-bras-a-v1.md`, `41332e20009b7801a565433bc7037524cb804865b913ac3b8687c4b64a78cf87` ;
  - le relevé documentaire des conditions d'envoi, `docs/notes/relance-organismes-discrets-v1/conditions-envoi-textes-google-mistral-releve-v1.md`, `b959c4d0db2e7b3168fac51a0d06c117312c7a0a011d7b1bb0bdad35609aaca2`, provenance par transcription, non opposable (R7) ;
  - le registre des GO, par `git show origin/main:registres/go.md`, tête locale `761710a7`, sans appel réseau : ligne 589, GO-2026-11-20-58 ;
  - le journal de la relance, entrées OD-237 et OD-247 à OD-251.
- **Aucune fiche n'est ajoutée.**

## 1. Points traités

| point | ce que le texte écrit | où |
|---|---|---|
| **mot de Lazar, choix 1 (b) : essai d'admission du juge** | huit lectures sur les huit entrées de l'ancienne file du juge ; huit sur huit de forme conforme ; sinon nœud de Lazar. C'est un mot de Lazar, non plus une procédure de la session. La règle 2 garde ses mots ; seule sa dernière phrase change | 3.4 ; 12, marque du nœud 1 ; 13 ; 13.1 |
| **choix 2 (a) : version servie du juge qui change pendant les ancres** | arrêt de la file du juge ; aucune ancre jugée n'est lue ; nœud de Lazar. Écrit comme issue de procédure. 8.2 et la ligne A12 restent telles quelles, et le texte ne les cite plus pour le juge | 3.4 ; 13.2, case « version des modèles » |
| **choix 3 (b) : envoi des textes** | conditions constatées et datées avant le premier envoi, essais d'admission compris. Google : offre payante (projet avec un compte de facturation actif), partage des journaux désactivé, journaux du projet à 7 jours. Mistral : offre payante, refus de l'entraînement activé, point d'accès européen `api.eu.mistral.ai` s'il sert `mistral-large-4-0`, sinon global, déclaré. Lazar fait les réglages ; le constat daté est versé avant le premier envoi. Réserves du relevé reprises : durée de conservation non trouvée, aucune région chez Google, service de Large 4 sur le point d'accès européen non vérifié | 3.4 ; 13 ; 13.1 |
| **C-1** | « aucun identifiant numéroté n'a été trouvé », à la place de « n'existe » | 3.4 |
| **C-2** | le renvoi du juge à 8.2 et à A12 est retiré en 3.4 et en 13.2 ; ces lignes sont dites pour les lecteurs seulement ; l'issue du choix 2 (a) la remplace pour le juge | 3.4 ; 13.2 |
| **C-3** | levée par le choix 1 (b) ; le texte dit d'où vient chaque essai, et que celui du juge était, au brouillon 41, une procédure de la session | 3.4 ; 12, marque ; 13.1 |
| m-1 | « Après le premier envoi d'une file, la session n'y a aucune liberté » est remise à la règle 8, et le retrait du brouillon 41 est dit | 3.4 |
| m-2 | la file du juge : son seuil est fixé par Lazar ; elle ne part que sous ses conditions d'envoi constatées, son devis contre-lu, sa ligne de calcul et sa clé vérifiée | 3.4 ; 13 |
| m-3 | pour `gemini-4-neon`, « identifiant figé » se lit « nom stable au sens de Google » ; c'est Lazar qui l'a admis, par « c go », en connaissant la réserve ; ce n'est pas un constat de la session | 3.4 ; 13.1 ; 13.2 |
| m-4 | réserves reprises. Mistral : identifiant dans la seule adresse de la page ; texte « mistral-large-4+2 » non interprété ; `mistral-large-4` affiché aussi (d'après la vérification, que je n'ai pas recoupée à la recherche). Neon : sortie le 18 novembre 2026 ; absent des tables de Vertex AI | 3.4 |
| m-5 | le point d'accès européen n'est plus fixé d'avance : européen s'il sert le modèle, sinon global, déclaré ; constaté à la vérification de la clé | 3.4 ; 13.1 |
| m-6 | la configuration de l'analyse « devra citer » la version 11 | 13.1, case du module ; 14.53 |
| m-7 | la décision sur la ligne de configuration de la base est sourcée : journal, OD-237 ; la pièce du développeur écrit « Point à trancher » | 13.2, case du lanceur |
| m-8 | « que le choix 5 (a) nomme », à la place de « que Lazar a confirmé par le choix 5 (a) » | 14.53 |
| m-9 | GO-2026-11-20-58 citée d'après le registre, ligne 589, tête `761710a7` ; ce qu'elle dit du second lecteur est rapporté. Quatre mentions « selon la session principale, 13:30Z » restent, comme histoire : statut du brouillon 41, ligne des commits, marque du brouillon 41 en section 12, titre de 14.53 | en-tête ; 3.4 ; 12 ; 13.1 |
| m-10 | **54 titres**, et non 55 : la note du brouillon 41 comptait l'en-tête comme une section | cette note, partie 5 |
| **lanceur** | la version qui fait foi reste à inscrire ; ajouté : la version 2 est en vérification du côté habilité, commit `848c17649`, selon le journal (OD-247) ; nom et empreinte inconnus de la relance | 13.2, case du lanceur |

## 2. Les deux règles d'admission, telles qu'écrites en 3.4

1. **Mistral Large 4 tient** : inchangée. 24 réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, 22 de forme conforme au moins.
2. **`gemini-4-neon` tient** : inchangée dans ses conditions. Huit réponses de code 200, sans refus, sans fin par sortie maximale atteinte, les huit de forme conforme. Le seuil est désormais un mot de Lazar.
3. à 7. Inchangées.
8. Une phrase remise : après le premier envoi d'une file, la session n'y a aucune liberté.

**Vérification de la clé.** Inchangée, sauf une exception que le mot de Lazar écrit : si le point d'accès européen de Mistral ne sert pas `mistral-large-4-0`, la vérification se refait sur le point d'accès global, déclaré. Modèle inconnu sur le point d'accès global aussi : nœud de Lazar.

## 3. Sections de jugement touchées

**Aucune règle de jugement, aucun seuil, aucune issue des sections gelées, aucune prédiction ne change.**

| section | lignes changées | ce qui change |
|---|---|---|
| hypothèse, prédiction, métrique, seuil | 0 | — |
| 7.1 à 7.8 (liste d'arrêt et ligne A12 comprises) | 0 | — |
| 10 | 0 | — |
| 12 | 1 sur 172 | fiche du nœud 1 : une marque du brouillon 42 ajoutée en fin de ligne. Elle dit que GO-2026-11-20-58 est lue au registre et que la condition « s'il tient à son essai d'admission » vient du mot « b a b go ». La fiche, l'option γ et les marques des brouillons 40 et 41 restent mot pour mot |
| 6.1 à 6.12, 8.1 à 8.7, 9, 11 | 0 | 6.3 (d) et (e′), 6.11, 8.2 et 8.4 sont identiques au brouillon 41 |

Sections sans jugement qui changent : en-tête (8 lignes changées, 5 lignes neuves à la table) ; 3.4 (8 lignes changées sur 41) ; préambule de 13 (2) ; 13.1 (3 cases : familles, lecteurs et juge des ancres, module) ; 13.2 (2 cases : version des modèles, lanceur) ; 14 (3 lignes changées dans 14.53 ; 14.54, 22 lignes neuves) ; contre-lecture (2).

**L'issue du juge n'a demandé aucune section de jugement.** Elle est écrite en 3.4 et en 13.2. Je n'ai touché ni 6.3 ni 8.2.

## 4. Questions pour Lazar

**Les trois questions de la vérification du brouillon 41 sont tranchées par « b a b go ».** Il en reste une, née du choix 2 (a). Elle ne retient rien : elle peut attendre le nœud lui-même.

**Question 1 — si la version du juge change à la seconde partie des ancres, que deviennent les jugements de la première ?**
- Enjeu : le mot dit « aucune ancre jugée n'est lue ». Mais l'ordre gelé (6.3) lit les ancres de l'étape (d), par programme, pour les critères de l'étape (e), scellés avant l'étape (e′). Si l'arrêt tombe à l'étape (e′), ces jugements ont déjà servi. Le texte le dit comme une limite et ne tranche pas.
- Options :
  - (a) rien n'est écrit d'avance : c'est l'objet du nœud, le jour où il s'ouvre (le texte). Avantage : aucune règle neuve, aucune section gelée touchée. Inconvénient : la décision se prendra en connaissant les critères de l'étape (e) ;
  - (b) écrire d'avance que les critères de l'étape (e) restent scellés et rapportés, et que seule l'ancre de la seconde partie manque. Avantage : décidé à l'aveugle. Inconvénient : touche à ce que 6.3 et la section 7 font des ancres, donc à des sections gelées ;
  - (c) écrire d'avance que tout est rejugé par un juge neuf sur ton mot. Avantage : une seule version de juge pour toutes les ancres. Inconvénient : tu as écarté le rejugement au choix 2 ; coût et délai.
- **Recommandation : (a).** Confiance : moyenne. Le cas est rare : 152 appels au plus, sur un nom dit stable.
- Défaut : (a), sans délai ; rien ne l'attend.

## 5. Contrôles par programme

| contrôle | résultat |
|---|---|
| titres | **54**, identiques hors le titre de niveau 1 (le programme compte 55 blocs, l'en-tête compris) |
| sections changées | celles de la partie 3, et rien d'autre |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 41 : `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| marque des cases | 7 lignes, toutes en 13.1, 8 occurrences : les mêmes cases qu'au brouillon 41 |
| table d'en-tête | 246 lignes à empreinte entière (241, plus 5 neuves). **229 recalculées, toutes égales** (les 224 du brouillon 41 et les 5 neuves). **16 sautées, aucune empreinte prise** : les 16 du brouillon 41, reprises telles quelles ; parmi elles, la pièce sans interne, relue par `git show` seulement (`e2f246eb…`, égale). 1 absente du disque : la recherche de la session principale, vérifiée par `git show` (`f7090b5d…`, égale) |
| validateur `problemes()` | les deux problèmes attendus, les mêmes qu'au brouillon 41 |
| renvois du juge à 8.2 ou à A12 | aucun ne reste, hors les phrases qui disent que ces lignes ne le visent pas, et l'histoire (14.53) |
| « n'existe » pour l'identifiant de Neon | retiré |

## 6. Ce qui reste hors du texte

- **Réglages des deux consoles, par Lazar**, et **leur constat daté**, versé et scellé avant le premier envoi : Google (compte de facturation actif, partage des journaux désactivé, journaux à 7 jours) ; Mistral (offre payante, refus de l'entraînement activé).
- **Devis des deux essais d'admission**, comme à la note du brouillon 41 ; de plus : le tarif du point d'accès européen de Mistral, 1,1 fois le prix courant selon le relevé ; les deux adresses de point d'accès de Mistral ; le constat que la vérification de la clé laisse sur le point d'accès retenu.
- **Lignes de calcul** : une par file, une par vérification de clé ; une de plus si la vérification de Mistral se refait sur le point d'accès global.
- **Programme qui conduit les essais** : de plus, l'arrêt de la file du juge sur un nom servi différent, garde à éprouver sur un cas sain et sur un artefact (R5) ; **le programme qui conduit les ancres à la course** doit porter la même garde.
- **Registre**, par la session principale : les lignes des mots « 1a 2a 3b4c 5a » et « b a b go », qui n'existent pas à la tête `761710a7`.
- **Côté habilité** : inchangé depuis la note du brouillon 41. La version 2 du lanceur est en vérification (commit `848c17649`) ; son nom et son empreinte sont à inscrire.
- **Code arrêté en version 13 : rien à changer.**
- Rien n'est recopié de ce que les mots de Lazar décident pour l'intervalle impossible et le moniteur appris non ajustable, au-delà de ce que le brouillon 41 portait.

## 7. Réserves

1. **Vérification de la clé et « premier envoi ».** Le mot dit « avant le premier envoi, essais d'admission compris ». J'ai écrit que les réglages des comptes sont constatés avant tout envoi, vérification de la clé comprise. Mais le point d'accès de Mistral ne se constate que contre le service : il l'est par la vérification de la clé elle-même, qui n'envoie aucun texte d'essai ni de course. C'est ma lecture ; au vérificateur de dire si elle tient.
2. **Exception à la vérification de la clé.** Le brouillon 41 faisait de « modèle inconnu du service » un nœud. Le mot de Lazar prévoit le repli sur le point d'accès global. J'ai écrit cette seule exception. Elle suppose que le point d'accès européen dise clairement qu'il ne sert pas le modèle ; une panne ou un refus de clé reste « cause corrigée, vérification refaite ».
3. **La règle 2 dit plus que « huit sur huit de forme conforme »** : code 200, aucun refus, aucune fin par sortie maximale, et, par la règle 3, un seul nom servi. Ces conditions étaient au brouillon 41 ; le vérificateur les avait jugées « pas de trop ». Je ne les ai pas retirées : une réponse refusée ou coupée n'est pas de forme conforme.
4. **« Aucune ancre jugée n'est lue »** : j'ai écrit « à partir de l'arrêt », et la limite pour l'étape (e′). Voir la question 1.
5. **La marque ajoutée en section 12** est le seul changement d'une section de jugement. Elle ne change aucun mot existant. Si elle gêne, elle se retire sans autre effet : 3.4 et 13.1 portent la même chose.
6. **Le relevé des conditions d'envoi** est une transcription par un outil qui résume. Les phrases citées de Google et de Mistral en viennent, non des pages. L'exclusion de l'entraînement sur l'offre payante n'est donc pas opposable ; le texte fait reposer la condition sur les réglages constatés.
7. **`mistral-large-4` affiché sur la fiche** : je le tiens de la vérification, non de la recherche de la session principale, que je n'ai pas rouverte. Le texte le dit.
8. **« Point à trancher »**, pour la pièce du développeur : cité d'après la vérification ; je n'ai pas relu la pièce à ce brouillon, seulement repris son empreinte.
9. **Les conventions** (« le juge des deux ancres est `gemini-4-neon`, s'il tient au sien ») n'ont pas changé : la formule est juste depuis le choix 1 (b).
10. **L'identifiant de session** de la ligne « Sessions » de l'en-tête n'est toujours pas celui des pièces des mots de Lazar. Je n'y ai pas touché.
11. **Je n'ai pas relu le texte en entier.**

## 8. Fichiers ouverts, et débords

- Le brouillon 41, par passages et par programme ; sa note et sa vérification, en entier.
- La pièce scellée du mot « b a b go » et le relevé des conditions d'envoi, en entier.
- Le journal de la relance : lignes 256 (OD-237), 266 (OD-247) et 267 à 270 (OD-248 à OD-251), par numéros de lignes ; une recherche des seuls identifiants OD-248 à OD-251.
- Par `git show origin/main:`, sans appel réseau, tête `761710a7` : le registre des GO, lignes 530 et 589 en entier ; la pièce sans interne des réponses du développeur habilité, pour son empreinte seulement ; la recherche de la session principale, pour son empreinte seulement.
- `src/controle_ia/prereg.py` : signature du validateur ; validateur exécuté.
- Les scripts de construction et de contrôle du brouillon 41, restés au bloc-notes de la session.
- **Débords, déclarés** :
  - **registre des GO** : pour voir si une ligne neuve touchait le bras A, j'ai affiché les 400 premiers caractères des lignes 590 à 630. Elles portent sur d'autres chantiers. Je n'en tire rien ; aucune ne touche le bras A ni T0.8 par ce que j'en ai vu ;
  - **fichiers non nommés par la tâche, hors cloisonnement, dans le dossier de la relance** : les relevés des identifiants de Mistral et de Google et la pièce du mot « c go », relus en entier et leurs empreintes prises, pour le mineur m-4 et le mineur m-3 ; le brouillon 40, par une recherche de chaîne, pour le mineur m-1 ;
  - **franchissement, comme au brouillon 41** : la pièce sans interne est rangée sous `docs/notes/bras-a-moniteurs-v1/`. Je ne l'ai prise que par `git show`, pour son empreinte.
- **Aucun autre débord.** Aucune recherche n'a parcouru un dossier. Aucune empreinte prise sur une ligne de la table qui touche un chemin cloisonné, ni sur une ligne sautée au brouillon 41.
- **Non ouverts** : aucun module du code ; aucun interne de moniteur, aucun module habilité, rien de la branche habilitée ; rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucune réponse ni aucun envoi de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense, aucun appel réseau. Rien de committé ; `registres/`, `.claude/` et le journal non touchés.
