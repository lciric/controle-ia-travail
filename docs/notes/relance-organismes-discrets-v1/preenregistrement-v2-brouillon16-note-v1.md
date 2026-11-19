# Note de changements — brouillon 16 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon16.md`, `bc4b0304245b29ca093816de977920d8927d3b5bab03ecb4434548370134732f` (1 741 lignes). Brouillon 15 inchangé (`a3526ec8884b4b7191e468dc0b50262d7b6e6a533468fe162742a47f8156ff58`, vérifié).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 15.
- **Objet** : remplir la case « lecteurs et juge des ancres » de 13.1 avec ce que l'essai de mesure a rendu, sans rien changer d'autre.
- **Sources, lues par programme, champs techniques seulement** : la règle de choix `runs/essai-mesure-lecteurs-bras-a-v1/regle-de-choix-claude-carbon-v1.json` (`b14b708413d716cbc505dab4be9fc953d79457d58beadbfb8bfad283fd5c8302`, égale à son compagnon) ; les trois rapports techniques — file Claude `06286c5061a9aff6d6ae20b47ec05e72a0aebc736116583ae92da491e0328cc7`, file Carbon `27f292bb7eefb8985302786a903321882f913235f83304d85e60f5f867ca99e4`, file GPT `93e1cdfc79c20194b9a73675c86991279e62171104e90e76004a2bbb87c1cfea` ; les trois manifestes de départ. **Aucune réponse d'un lecteur n'a été ouverte**, ni aucun fichier d'envoi, ni aucune clé (les manifestes ne portent que le nom des variables).
- **Heures (UTC, `date -u`)** : début 2026-11-19T14:02:39Z.
- **Interdits tenus** : aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé. Le brouillon et cette note sont scellés par leur compagnon, comme demandé.
- **Contrôles faits** : validateur — deux problèmes attendus (marque dans sept cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; sept fiches à la lettre ; table d'en-tête, 106 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 15 ; la différence avec le brouillon 15 tient en 25 lignes ajoutées et 9 retirées.

## 1. Ce qui change, du brouillon 15 au brouillon 16

| section | changement |
|---|---|
| titre, statut, en-tête | brouillon 16 ; ce qui a été ouvert de plus ; date ; commit ; note ; cinq lignes à la table des pièces (brouillon 15 ; règle de choix ; trois rapports techniques) |
| 6.11 | une phrase : projection des lectures par la règle (≈ 146,4 USD pour le lecteur 1, ≈ 97,0 USD pour le lecteur 2), à reprendre au devis de la course ; ni dépense accordée, ni résultat |
| 13.1 | case « lecteurs et juge des ancres » remplie, sauf trois points marqués |
| 14 | 14.28 neuf |

Tout le reste est le texte du brouillon 15 à l'octet près.

## 2. Ce que la case porte maintenant

- **Lecteur 1** : `claude-opus-5-5`, effort moyen (`medium`), sortie maximale 8 192 jetons, réflexion comprise ; version servie `claude-opus-5-5` ; 24 conformes sur 24.
- **Lecteur 2** : `gemini-4-carbon`, budget de réflexion 1 024, température 0 acceptée ; version servie `gemini-4-carbon` ; 24 conformes sur 24.
- **Juge des ancres** : `gpt-6.2-astra`, réglage par défaut, sans température (refusée par le service, retirée), sortie maximale 8 192 ; version servie `gpt-6.2-astra` ; 8 conformes sur 8.
- Les trois manifestes portent les empreintes des deux consignes du texte.

**Trois points laissés marqués dans cette case** :
1. **Sortie maximale du lecteur 2** : 4 096 jetons à l'essai (5 120 comptés avec le budget de réflexion) ; 8 192 selon la règle, pour le devis des lectures. Je n'ai pas choisi.
2. **Le mot de Lazar** sur ces choix : la section 3.4 dit que la règle recommande et que Lazar choisit ; aucune ligne du registre des GO ne porte ce choix (lu jusqu'à la ligne 503, commit `416a3342…` de la branche principale distante).
3. **Découpage des messages** pour `gemini-4-carbon` et `gpt-6.2-astra` : les pièces que j'ai le droit de lire ne le disent pas (il est sans doute dans la configuration de l'essai, que je n'ai pas ouverte).

## 3. Cases de 13.1

**Remplies** : familles ; consignes figées ; seuils ; consignes des moniteurs ; moniteurs à modèle de langue (instrument) ; code de la base ; réserve R-BA2 ; lecteurs et juge des ancres (sauf les trois points ci-dessus).

**Restantes** (sept lignes portent la marque) :

| case | ce qui manque | qui |
|---|---|---|
| nœuds | la fiche 7 (point 16 de la section 12) : le texte la dit sans réponse — voir le défaut 1 ci-dessous | Lazar ; rédacteur |
| lecteurs et juge des ancres | sortie maximale du lecteur 2 ; mot de Lazar ; découpage des messages de deux modèles | Lazar ; session de relance |
| lecture du juge d'une autre lignée | 2 560 ou 6 400 (posée par la session principale) | Lazar |
| entropie | l'entier racine ; et l'écart à la règle gelée R9 pour l'entropie propre de la table des identifiants (en attente du mot de Lazar) | Lazar ; session de relance |
| renvoi de la base | « vérifié » ou « non vérifié » | lecteur habilité de la session principale |
| commit du code de l'instrument et de l'analyse | commit et empreintes | session de relance |
| module des cinq moniteurs, côté habilité | épreuve par retrait et notice de la version 7 | session principale |

Hors de 13.1 : la contre-lecture 10, sur le texte aux cases remplies.

## 4. Défauts vus

1. **Le registre des GO porte une réponse que le texte ne porte pas.** La ligne GO-2026-11-19-70 (ligne 503 ; mot de Lazar « go file Claude, go recos », session de relance, 13:46:32Z) dit, « selon la lecture de la relance, partagée par la mère » : la recommandation **(b)** de la fiche 7 est retenue (un intervalle dégénéré interdit seulement de conclure « ne repère pas »), et les trois choix du brouillon 12 sont confirmés (réglages de lecture des moniteurs à modèle de langue ; précision des poids ; lecture sans raisonnement non jouée). Le brouillon 16 ne le porte pas, parce qu'on m'a demandé de ne rien changer d'autre : la section 6.9 est encore écrite sous l'option (a), la section 12 dit la fiche sans réponse, et la case « nœuds » reste marquée. **À porter au brouillon suivant** : 6.9 (règle de l'intervalle dégénéré), section 12 (point 16 tranché ; point 8 (xi) et (xii) confirmés), nœud 18, case « nœuds », et le réglage correspondant du code de l'analyse.
2. **Le rapport technique ne nomme pas le brouillon dont la forme a servi à juger la conformité.** La section 3.4 le demande (« le rapport nomme ce brouillon par son empreinte »). Les manifestes disent seulement d'où viennent les consignes (lignes 195 à 220 et 242 à 276, empreintes égales à celles du texte). Or la tolérance de forme a changé entre les brouillons 5 et 7 (champs sans emploi ignorés ; un bloc de code retiré). La conformité mesurée — 24 sur 24 pour les réglages retenus — ne dépend pas de cette tolérance si elle a été jugée à la lettre la plus stricte ; mais le « ne tient pas » de l'effort bas d'Opus (20 sur 24) et des deux réglages de Sonnet (10 et 11 sur 24) pourrait en dépendre. À dire par l'auteur du programme de conformité.
3. **Le budget de réflexion 2 048 du lecteur 2 n'a pas été mesuré en entier** : 7 lectures sur 24, puis une coupure du service (code 502). La règle retient 1 024, qui tient ; le choix ne dépend pas de 2 048. Je le signale parce que la projection de coût que la règle donne pour 2 048 repose sur ces sept lectures.
4. **Le juge des ancres tourne sans température fixée** (le service la refuse). Le texte le permettait (« température 0 si le service l'accepte ») ; c'est maintenant écrit dans la case. Sa lecture n'est donc pas plus déterministe que celle du lecteur 1.
5. **Le coordinateur m'a donné le niveau d'effort en deux langues** (« medium », « moyen ») : la règle écrit « moyen », le réglage envoyé au service est `medium`. Les deux sont dans la case.
