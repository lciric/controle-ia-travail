You are powered by the model named Opus 5.5.

# Vérification des corrections : questions et devis du collisionneur, versions 2 — v1

Écrite le 20 novembre 2026 par le contre-lecteur de la version 1 (Claude Opus 5.5), en une passe courte. Pièces vérifiées, sceaux vérifiés : `question-modes-sabotage-v2.md` (`9e7e8246…`), `question-attaques-v2.md` (`349b3dc8…`), `devis-collisionneur-modes-et-attaques-v2.md` (`0eeed2b4…`). Référence : ma contre-lecture `contre-lecture-questions-et-devis-v1.md` (`df23e431…`, sceau vérifié). Sans réseau, sans dépense, sans commit ; aucun mode proposé.

## Verdict

**Soumissible après ces corrections** (version 3 des deux questions ; trois retouches au devis).

- **Corrections portées à la lettre.** Chaque couple de ma contre-lecture est porté mot pour mot : B1 à B7, M1 à M5, m1 à m5. J'ai cherché chaque ligne de chaque texte « après » dans les versions 2 : chacune s'y trouve une seule fois. Il n'y a que trois écarts, tous déclarés en tête du devis : 3,61 et 3,69 au lieu de 3,60 et 3,68 ; 19,07 et 21,49 au lieu de 19,01 et 21,43 ; une phrase de plus à B3. Ils suivent la longueur des questions de version 2.
- **Rien d'autre n'a changé**, hors ce que listent les têtes. Le différentiel mot à mot de la version 1 à la version 2 ne montre que les couples et les changements déclarés : titres, statuts, tables des sorts, noms et tailles des questions, centimes, titres des tables, ligne « par clé ».
- **Centimes rejoués.** J'ai rejoué mon outil (`contre-lecture-questions-et-devis-v1-outils/recalcul_devis_v1.py`, `2e9822fc…`) sur les deux questions de version 2. Ma sortie, `sortie-recalcul-questions-v2-par-verificateur.txt` (`20f625b9…`, scellée), est identique octet pour octet à celle du rédacteur. Chaque centime de la version 2 s'y retrouve : tailles 9 136 et 8 898 ; tables par espèce ; totaux 18,01 / 33,94 / 48,13 / 94,00 et 19,29 / 37,26 / 52,16 / 102,69 ; ligne « par clé » ; 3,61 et 2,13 ; 3,69 et 2,16 ; épreuve à 2,13 et 2,16 ; point 15, 19,07 et 21,49, d'où 26 et 28, puis 54,13 et 58,16. Les plafonds de 23 et 25 tiennent.
- **Mais les deux questions ne sont pas servables telles quelles.** Le script sert le fichier entier, deux fois (comme faits et comme question, devis section 6, point 3). Or chaque question nomme le directeur deux fois : à la ligne 3 et dans le fait qui rapporte son mot. Sa tête porte aussi des éléments internes : le chemin d'un mandat, des identifiants d'accord, les modèles rédacteur et contre-lecteur, des empreintes, et une table des sorts qui nomme une contre-lecture et ses couples. Je n'ai trouvé aucun identifiant de session ni aucun courriel. De plus, le **préambule du script v8** nomme le directeur en toutes lettres (ligne 154, « arbitrée par un humain, » suivi de son nom). Le devis doit exiger que la version neuve le retire.
- **R6.** La sortie du rédacteur, `sortie-recalcul-questions-v2-par-redacteur.txt`, n'a pas de compagnon `.sha256`. Elle est identique à la mienne, qui est scellée ; le devis peut citer la mienne (couple D2).

## Couples pour une version 3

### Q1. Question « modes de sabotage » : retirer la tête interne

Raison : la tête est servie aux fournisseurs. Elle nomme le directeur et porte des éléments internes. La provenance passe au devis (couple D3).

Avant (lignes 3 à 10 de `question-modes-sabotage-v2.md`, exactes) :
> Écrite le 20 novembre 2026 par un agent concepteur (Claude Fable 5.2), sur le mandat 1 de `docs/notes/mere-mandats-fable-perdus-2026-11-20/mandats-a-relancer-v1.md` (`57424307…` ; accord de Lazar GO-2026-11-20-36, point 4, et GO-2026-11-20-32). Pièce décisive. Elle n'autorise aucune dépense. Elle ne propose elle-même aucun mode.
>
> **Version 2.** La version 1 (`question-modes-sabotage-v1.md`, `5c91743c…`, gardée telle quelle) corrigée après la contre-lecture `contre-lecture-questions-et-devis-v1.md` (`df23e431…`, Claude Opus 5.5, « soumissible après ces corrections »). Chaque couple « avant, après » est appliqué à texte exact, par programme, l'« avant » compté une fois. Reste à faire : la vérification de ces corrections par le même contre-lecteur. Hors couples, seuls changent le titre, la phrase de statut et ce paragraphe.
>
> | couple | sort | raison |
> |---|---|---|
> | M2 (fait 6, épreuves de l'instrument) | appliqué | le fait dit maintenant ce que dit sa source |
> | M3 (rubrique 5, épreuves décrites, jamais rédigées) | appliqué | ferme la seule rubrique qui pouvait appeler un exemple rédigé |

Après : rien. Le titre est suivi d'une ligne vide, puis de « Ce fichier porte les faits et la question. » Le titre passe de « — v2 » à « — v3 ».

### Q2. Question « attaques » : retirer la tête interne

Raison : la même que pour Q1.

Avant (lignes 3 à 9 de `question-attaques-v2.md`, exactes) :
> Écrite le 20 novembre 2026 par un agent concepteur (Claude Fable 5.2), sur le mandat 1 de `docs/notes/mere-mandats-fable-perdus-2026-11-20/mandats-a-relancer-v1.md` (`57424307…` ; accord de Lazar GO-2026-11-20-36, point 4, et GO-2026-11-20-32). Pièce décisive. Elle n'autorise aucune dépense. Elle ne propose elle-même aucun mode.
>
> **Version 2.** La version 1 (`question-attaques-v1.md`, `d9d105d9…`, gardée telle quelle) corrigée après la contre-lecture `contre-lecture-questions-et-devis-v1.md` (`df23e431…`, Claude Opus 5.5, « soumissible après ces corrections »). Chaque couple « avant, après » est appliqué à texte exact, par programme, l'« avant » compté une fois. Reste à faire : la vérification de ces corrections par le même contre-lecteur. Hors couples, seuls changent le titre, la phrase de statut et ce paragraphe.
>
> | couple | sort | raison |
> |---|---|---|
> | M4 (fait 2, réserve de détecteurs retirée) | appliqué | la question n'en a pas besoin, et la nommer invite à viser l'outil de l'audit |

Après : rien. Le titre est suivi d'une ligne vide, puis de « Ce fichier porte les faits et la question. » Le titre passe de « — v2 » à « — v3 ».

### Q3. Question « modes de sabotage », fait 8 : ne pas nommer le directeur

Avant :
> 8. RAPPORTÉ (mot de Lazar, directeur du programme, transmis par une autre session le 20 novembre 2026, pas encore relu à la source) :

Après :
> 8. RAPPORTÉ (mot du directeur du programme, 20 novembre 2026, pas encore relu à la source) :

### Q4. Question « attaques », fait 7 : ne pas nommer le directeur

Avant :
> 7. RAPPORTÉ (mot de Lazar, directeur du programme, transmis par une autre session le 20 novembre 2026, pas encore relu à la source) :

Après :
> 7. RAPPORTÉ (mot du directeur du programme, 20 novembre 2026, pas encore relu à la source) :

Contrôle à faire sur chaque version 3 avant de la sceller : aucune occurrence de « Lazar », de « Ciric », de « session_ », de « @ », de « GO- », de « R- » suivi d'un chiffre, de « Claude », de « Fable », d'« Opus », de « contre-lecture », ni d'une empreinte. Les chemins des décisions citées dans les faits (`docs/decisions/…`, `docs/programme-controle-ia-v2.md`) ne nomment personne et peuvent rester ; les remplacer par « le programme, section 6 », par exemple, est permis, sans être exigé.

### D1. Devis, section 6, point 2 : le préambule du script ne nomme personne

Raison : le préambule du v8 est servi à chaque appel, et il nomme le directeur.

Avant :
> C'est un instrument : écrit, contre-lu par un autre modèle, essayé hors réseau sur un cas sain et sur un artefact pour chacune des conditions (a) à (d) (R5), sans dépense.

Après :
> La version neuve retire aussi du préambule servi aux modèles tout nom de personne : celui du v8 nomme le directeur après « arbitrée par un humain » ; il dira seulement « arbitrée par un humain ». C'est un instrument : écrit, contre-lu par un autre modèle, essayé hors réseau sur un cas sain et sur un artefact pour chacune des conditions (a) à (d) (R5), sans dépense.

### D2. Devis, section 3 : citer le rejeu scellé (R6)

Avant :
> Sa sortie (`20f625b9…`) n'est pas versée, le rédacteur n'écrivant que trois fichiers : elle est à rejouer et à verser par le contre-lecteur ou par la mère.

Après :
> Sa sortie est versée et scellée par le contre-lecteur : `sortie-recalcul-questions-v2-par-verificateur.txt` (`20f625b9…`), dans le même dossier que l'outil. Pour les questions de version 3, plus courtes, le rejeu se refait et se verse scellé avant la remise.

### D3. Devis, section 1 : questions de version 3, servies sans rien d'interne

Raison : la provenance retirée des questions doit rester quelque part. Les centimes changent, car les questions de version 3 sont plus courtes ; les plafonds par passage ne devraient pas bouger (22,71 et 24,49 avant arrondi avec la version 2), mais le rejeu le dira.

Avant :
> - **Questions** (même dossier que ce devis) : `question-modes-sabotage-v2.md` et `question-attaques-v2.md`. Chacune porte ses faits et sa question.

Après :
> - **Questions** (même dossier que ce devis) : `question-modes-sabotage-v3.md` et `question-attaques-v3.md`. Chacune porte ses faits et sa question, et rien d'autre : elles sont servies telles quelles aux fournisseurs, sans nom de personne, ni identifiant de session, ni courriel, ni tête interne. Leur provenance est tenue ici : écrites par un agent concepteur (Claude Fable 5.2) sur le mandat 1 de `docs/notes/mere-mandats-fable-perdus-2026-11-20/mandats-a-relancer-v1.md` (`57424307…`), sous GO-2026-11-20-36, point 4, et GO-2026-11-20-32 ; versions 1 et 2 gardées ; contre-lecture `contre-lecture-questions-et-devis-v1.md` (`df23e431…`) ; vérification `verification-corrections-questions-et-devis-v2-v1.md` ; la version 3 ne change, de la version 2, que les couples Q1 à Q4 de cette vérification.

Dans le devis, les autres mentions des questions de version 2 (tailles, centimes, commande de rejeu) suivent la version 3, par le rejeu de l'outil. Ce sont des changements de conséquence, à déclarer en tête comme dans la version 2.

## Limites

Une passe courte. Je n'ai relu le fond des versions 2 qu'aux endroits touchés par les couples et par le différentiel. Je n'ai lu aucune réponse de modèle, ouvert aucun coffre, ni lu aucun fichier interdit. Je n'ai modifié aucun autre fichier : j'ai seulement ajouté ma sortie de rejeu scellée dans `contre-lecture-questions-et-devis-v1-outils/`. La sortie du rédacteur reste sans compagnon `.sha256` ; c'est à la mère de la sceller ou de la laisser à côté de la mienne.
