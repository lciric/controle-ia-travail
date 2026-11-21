# Vérification de la pièce « lignées de modèles à exclure des deux lecteurs externes du dommage » (scellement 2 du bras d'attaque) — v1

- Classe C (travail). Écrite le 2026-11-21 entre 17:45 et 17:50 UTC (`date -u`) par un sous-agent Opus 5.5 neuf, réfutateur, qui n'a écrit ni la pièce vérifiée ni aucun moniteur.
- Pièce vérifiée : `docs/notes/scellement-2-lignees-lecteurs-v1/lignees-a-exclure-v1.md` (lue en entier, 35 lignes).
- Règle suivie : noms de famille et rôles seulement ; aucune couche, aucun seuil, aucune invite, aucun trait, aucune valeur ; aucun contenu de moniteur ni de mode. Sources lues aux seules lignes citées (et quelques lignes voisines pour le contexte).

## Verdict

**À corriger, sans changer la liste d'exclusion.** Toutes les citations chemin:ligne de la pièce tombent juste, et toutes les empreintes vérifiables concordent. La liste « Llama ; Qwen » et la lignée du juge (Qwen) sont exactes au regard de la règle écrite (N-060 v3, lignes 24-25, reprise inchangée par N-060 v4, ligne 23). Mais la table des familles oublie plusieurs bases boîte noire de G1 dont la famille n'est établie par aucune pièce, et une source est citée hors de sa portée (bras A pris pour G1). Ces écarts ne font entrer aucune famille nommée de plus ; ils ouvrent des conditions.

## Lignes vérifiées à la source

| ligne de la pièce | source citée | constat |
|---|---|---|
| 11 (agent, Llama) | `prereg/T0.6-organismes-config-7b-v1.json`:17-18 ; note des familles du bras A :16 | exact : ligne 17 nomme le modèle Llama 3.1 8B de Meta, ligne 18 son nom court ; note du bras A, ligne 16 : Llama |
| 12 (moniteur boîte noire, Llama) | `registres/decisions.md`:376 ; N-029 :20-22 ; `registres/go.md`:456 | 376 exact (D1 : même modèle que l'agent, et Llama 3.2 3B) ; N-029 20-22 exact. **Écart 1** : go.md:456 (GO-2026-11-19-23) est une décision **du bras A** des organismes discrets, non de G1 |
| 13 (sondes lisent l'agent) | N-056 :38-46 et 52-53 | exact (bases (ii) cascade et (iii) dernier état sur les mêmes sondes ; traits internes de l'agent) |
| 14 (juge d'une autre lignée, Qwen) | N-053 :33-34 ; go.md:456 ; rapprochement :239-240 | exact (N-053 point 4 : Qwen 2.5 7B en bras rapporté ; rapprochement : « c'est un moniteur, exclu de l'oracle ») ; même réserve de portée pour go.md:456 |
| 15 (prédicteur sur les traits du texte) | N-029 :23-27 | exact (sans modèle de langue) |
| 16 (juge ouvert, plafond) | N-029 :28-30 | exact (non décidé, GO à part, famille non dite) |
| 18 (borne, comparateurs) | N-060 v3 :24-25 ; note du bras A :38 ; règle du bras d'attaque :131 (branche `claude/scellement-2-familles-aveugles-v1`) | exact ; empreinte de la règle sur la branche recalculée : `88418df09c2e969c…`, concordante |
| 22 (lignée du juge) | N-053 :33-34 ; go.md:456 | exact pour N-053 ; go.md:456 confirme dans le cadre du bras A seulement (écart 1) |
| 30 (juge et second juge du bras d'attaque) | règle :324-325 et 394-395 | exact ; la règle ne nomme aucune famille de modèle (recherche des noms de famille dans tout le texte : aucune) |
| 31 (juges 8B et 3B) | decisions.md:376 ; rapprochement :68-69, 246 | exact ; le « 3B à vérifier » du rapprochement est levé par la ligne 376 elle-même, qui nomme Llama 3.2 3B |
| 32 (Claude, auteur de la famille aveugle) | pièce 1 :3-4 (même branche) ; N-060 v3 :34-35 ; rapprochement :69 | exact ; la pièce omet l'erratum 2 de la pièce 1 (écart 6) |
| 33 (Gemini) | N-057 :17 ; index des paramètres des modes du bras d'attaque :10 ; note sur Neon :11, 32 | exact (N-057 : espèce C = Argon de Google ; index, ligne 10 : le même identifiant ; note sur Neon : Neon juge les ancres du bras A) |
| 34 (juge de grande taille, Llama Scope) | N-061 :12 | exact |
| 5 (empreintes) | compagnons | les onze premières recalculées concordent, compagnons compris (N-053, N-056, N-060 v3, N-029, N-054, N-057, N-061, note du bras A, simulation des formulations de G1). **Non vérifiée par moi** : l'index du scellement 2 (`5d0479b4…`), dont la pièce ne donne pas le chemin. |

## Écarts

1. **Source hors de portée** (lignes 12, 14, 22). `registres/go.md`:456 (GO-2026-11-19-23) fixe le moniteur boîte noire et le juge Qwen **du bras A** des organismes discrets. Il ne fonde pas les familles des moniteurs de G1 ; il les recoupe seulement. À écrire « recoupement, bras A ». La source de G1 pour Qwen reste N-053 :33-34 ; pour Llama, D1 (`registres/decisions.md`:376) et N-029 :20-22.
2. **Bases boîte noire de G1 oubliées, sans famille établie.** `docs/decisions/decision-N-007-N-008-v1.md`:45-49 et 66 : la meilleure base boîte noire de G1 comprend (i) une accumulation additive sur scores boîte noire, sans modèle en propre (elle agrège les scores du juge Llama), (iv) **un modèle temporel sur un observateur séparé**, et **le juge robustifié** de la proposition P-003 (`registres/decisions.md`:381, défaut appliqué). Aucune pièce lue ne nomme la famille de l'observateur de (iv) ni celle du juge robustifié. Si l'une n'est ni Llama ni Qwen, elle s'ajoute à l'exclusion. À faire établir par la mère avant le choix des lecteurs.
3. **Plancher oublié.** N-007-N-008 :68 : « juge en une passe avec le même modèle », plancher rapporté de G1 : Llama, déjà exclu. À ajouter à la table pour qu'elle soit complète.
4. **Lecture de plus grande taille oubliée.** N-053 :36-37 : un sous-ensemble des lectures décisives à plus grande taille, changement de modèle, GO à part ; famille non dite. Même statut que le juge ouvert de N-029 point 3 (incertitude 5 de la pièce) : s'il entre, sa famille s'ajoute.
5. **Lecteurs de l'oracle du bras A non cités.** L'incertitude 4 ne parle que de Neon. Or le bras A, sous la même règle N-060, a désigné deux lecteurs : un modèle Claude et Mistral Large 4 (`registres/go.md`:589, GO-2026-11-20-58 ; note sur Neon :32). Ce choix confirme, à la lettre de N-060, que Claude et Mistral ne sont pas des familles de moniteurs évalués. Il pose aussi une question de réemploi (mêmes sièges, autre bras), comme pour Neon.
6. **Erratum 2 de la pièce 1 omis** (incertitude 3). Branche `claude/scellement-2-familles-aveugles-v1`, `piece-1-attestation-aveuglement-v1-erratum-2.md` : l'auteur Fable du mode tenu à l'écart a lu N-060 v3 et a écrit la vérité du dommage de son propre mode ; l'écart à N-060 v3 point 4 est un nœud à Lazar avant toute exécution de l'oracle, et un « monteur de l'oracle » d'une autre main est à désigner par Lazar. Ce n'est pas une exclusion de famille, mais cela renforce la recommandation « lecteur hors Claude, ou instance distincte et parenté déclarée ».
7. **Ressources publiques de N-061 incomplètes** (incertitude 5). N-061 :12 nomme aussi Liars' Bench et SHADE-Arena comme bases boîte noire de T0.8 ; ce sont des jeux, non des familles, et rien n'entre dans la liste scellée de G1 sans nœud à part (N-061 :15). Si un moniteur tiré de ces ressources y entre, sa famille s'ajoute.
8. **Affirmation non vérifiée par moi** (ligne 18) : « le préenregistrement de la porte G1 n'est pas scellé sous `prereg/` ». La règle du bras d'attaque (ligne 131) ne cite qu'un brouillon 6 de G1, ce qui va dans ce sens ; je n'ai pas listé `prereg/` (consigne).

## Familles oubliées cherchées, et ce qui en sort

| famille cherchée | constat |
|---|---|
| juge de bras rapporté | Qwen (N-053 :34) : présent dans la pièce |
| base boîte noire | juges Llama (D1) : présents ; prédicteur sans modèle : présent ; observateur de (iv) et juge robustifié : **absents, famille non établie** (écart 2) ; plancher « même modèle » : absent, Llama (écart 3) |
| référence locale | N-029 : présente (bras 1 à 3) |
| juges de l'oracle de N-060 v3 | non désignés pour le scellement 2 ; ceux du bras A (Claude, Mistral) non cités (écart 5) |
| juge des ancres du bras A | Neon, Google : présent (incertitude 4) |
| modèle de l'agent | Llama : présent |
| panel des juges du papier C | `registres/decisions.md`:377 (D2) : Llama, Qwen, Mistral 7B. Hors G1, donc hors de la règle ; mais la règle du bras d'attaque (ligne 114) vise aussi les moniteurs que lit le papier C : si les épisodes du scellement 2 servent aussi au papier C, Mistral est un juge évalué. Statut actuel de D2 non vérifié |
| concepteurs de modes | Astra (OpenAI) a été retiré de tout rôle du bras A parce qu'il conçoit des modes (`registres/go.md`:574, GO-2026-11-20-43 ; :589). Ce n'est pas une règle de G1, mais un précédent : au scellement 2, l'auteur du mode tenu à l'écart est Claude, et le collisionneur a employé Argon (Google) côté évasion |

## Liste finale

Lignée du juge : **Qwen** (N-053 :33-34). Exclusion : **Llama ; Qwen**, inchangée, plus toute famille qu'établirait la mère pour l'observateur de la base (iv), le juge robustifié de P-003, le juge ouvert de grande taille ou la lecture de plus grande taille de N-053, si l'un d'eux entre au préenregistrement de G1.
