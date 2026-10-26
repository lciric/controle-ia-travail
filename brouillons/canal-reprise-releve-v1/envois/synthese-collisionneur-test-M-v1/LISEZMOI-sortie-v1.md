# LISEZMOI — sortie de la synthèse du tour « test des hypothèses de M sur sondes » (v1)

Écrit le 2026-10-26 à 04:00 UTC (heure lue sur `date -u` dans la commande qui l'écrit) par un sous-agent neuf, sur `BRIEF-synthese-test-M-v1.md` et sa mise à jour de la lignée conv-audit (26 octobre 2026, 03:38 UTC). Le jugement de la suite de H-M1 par session-depot n'a été ni lu ni supposé : la synthèse porte sur ce tour seul.

## Ce qui a été fait
1. Lecture intégrale de toutes les pièces de `/var/tmp/fournis-synthese-test-M-v1/`, rien d'autre. Ni git, ni réseau, ni sous-agent, ni clé, ni recherche hors de ce dossier ; écriture dans `/var/tmp/synthese-collisionneur-test-M-v1/` seulement.
2. Empreintes vérifiées avant la lecture des réponses (`sha256sum`) :
   - les neuf cellules contre leurs compagnons `cellules/*.md.sha256` : 9 sur 9 conformes (`sha256sum -c`, code de sortie 0) ;
   - les neuf cellules et leurs neuf compagnons contre `EMPREINTES-collisionneur-test-M-v1.txt`, chemins `run-test-M-e3t1-v1/cellules/…` : 18 sur 18 conformes, chaque chemin présent une seule fois ;
   - la question (`bf3d0f52…`) : conforme à la liste, sous son nom et sous `run-test-M-e3t1-v1/question-etage3.md` ;
   - `LISEZMOI-collisionneur-test-M-v1.md` (`4d930e73…`) : conforme à l'entrée `LISEZMOI-v1.md`, son nom d'origine ;
   - la liste elle-même (`6ab45cc2…`) : conforme à `EMPREINTES-v1.txt.sha256.original`, sous son nom d'origine `EMPREINTES-v1.txt` ;
   - pièces hors de la liste : la v1 du texte du test (`eb9328b9…`) et la v2 (`4fb3ee31…`) concordent avec les empreintes que citent la v2 et la v3 ; la v3, l'avis et le brief ne sont cités par aucune pièce du dossier, leurs empreintes sont seulement consignées ;
   - entrées de la liste sans fichier dans le dossier (outil, scripts, journaux, essais, état, faits) : non vérifiables ici.
3. Lecture des neuf cellules en entier ; aucune ne contient de réflexion interne (recherche de marqueurs, puis lecture).
4. Écriture de `synthese-collisionneur-test-M-v1.md`, heure portée par `date -u` dans la commande même, puis de son compagnon ; enfin de ce fichier et de son compagnon (R6).

## Pièces lues
| pièce | SHA-256 |
|---|---|
| `BRIEF-synthese-test-M-v1.md` | `15b6cdf000d088cdf9a409294f698900bc49cca7083f7dd6e7848ce48db5738b` |
| `LISEZMOI-collisionneur-test-M-v1.md` | `4d930e73e18d3236262f49041f6da05ad4320d02b3c97bad51cf63705387cace` |
| `EMPREINTES-collisionneur-test-M-v1.txt` | `6ab45cc2d150a32e1008387c88ba827f6744a7eb18d631c42b18f385e6ebcf28` |
| `EMPREINTES-v1.txt.sha256.original` | `45a21e094feb776269f89727c7ba18845cfd8e79857067772b2a4fdb7bc9e1fe` |
| `question-test-M-sondes-collisionneur-v1.md` | `bf3d0f522a83e42bac6d4866c73ade68e7ee3f364af1496f3949fefe62c091ff` |
| `avis-test-HM1-gabarit-style-conv-audit-v1.md` | `0112e6979e82ae1f4ed59ad00c830eb7f85a0194f0bbdd0985eac803cb70e58e` |
| `test-hm1-gabarit-style-v1.md` | `eb9328b992e875a35735422a62756a0539f0a4e45fbad28e7b90fd3a97404f53` |
| `test-hm1-gabarit-style-v2.md` | `4fb3ee311dce06079aa3823997066501f0c9169e644d39c3c77d75842ec7d955` |
| `test-hm1-gabarit-style-v3.md` | `225b24c4178287271ac999eddc0b446a4df882eac02098a326d575700af348fb` |
| `cellules/E3-T1-conception-A.md` | `7fd02e77bae903ba8648423cf329df1a8cc2a9be107467d4797553252a3cba50` |
| `cellules/E3-T1-conception-B.md` | `6160aa534bd1c9acf674eaa8cbfb6b0321578663d59d7bfcdfb972e672515a95` |
| `cellules/E3-T1-conception-C.md` | `eb1f884480c27f646cc4a7a10642ee19280fc2c7f87dbf539f26b9c85bb6b760` |
| `cellules/E3-T2-redteam-A.md` | `381684448861a5ee51c3679453de6cd7189265ab61fac911984d2ff8c978b624` |
| `cellules/E3-T2-redteam-B.md` | `b6bb43bd24831a660a7b789977098e2cf8599b566282329308bc64058f664015` |
| `cellules/E3-T2-redteam-C.md` | `6b4b30fdecdbf30752a6bb9d0493997430faaa8f46dda3e68b9dbc5d5e81628a` |
| `cellules/E3-T3-riposte-A.md` | `0fdb108dfff6251021bbddd55ca40cd3cdfafa7214d5a8b170070674e644c73c` |
| `cellules/E3-T3-riposte-B.md` | `4b4893286c8b885531fa732f499ebc1cfd49b48eb82d6a10af92061266950b71` |
| `cellules/E3-T3-riposte-C.md` | `d1bd31ab547d9dc935da93452dbe093e1c799506d22217aef7047e3ecf803e18` |

Codes de cellule de la synthèse : A1, B1, C1 = `cellules/E3-T1-conception-{A,B,C}.md` ; A2, B2, C2 = `cellules/E3-T2-redteam-{A,B,C}.md` ; A3, B3, C3 = `cellules/E3-T3-riposte-{A,B,C}.md`.

## Fichiers produits
| fichier | SHA-256 |
|---|---|
| `synthese-collisionneur-test-M-v1.md` | `b9583209e47c988005ae42b1fbf13a418235e9d2bb7ed1b628d800f412fe7748` |
| `synthese-collisionneur-test-M-v1.md.sha256` | compagnon de la synthèse |
| `LISEZMOI-sortie-v1.md` | dans son compagnon `LISEZMOI-sortie-v1.md.sha256` (un fichier ne peut porter sa propre empreinte) |

## Écarts déclarés
1. **Option (b) de l'avis** : le brief prête à l'avis (message n° 69) une option (b) ayant reçu un go conditionnel ; la pièce fournie ne contient que les options (a), (b), (c) de la question, recommande (a) et écarte (b). La synthèse rapporte ce que les réponses disent de ces trois options et des correctifs propres de l'avis ; elle ne dit rien d'une option (b) absente des pièces.
2. **Critères de classement des tâches** : omis sur consigne, même là où une réponse en propose ; lieux cités au § 7 de la synthèse, sans contenu.
3. **Longueur** : 1 578 mots, 10 625 signes visibles (comptés en UTF-8) ; deux pages en corps 10 sur A4, un peu plus en corps 11 : « deux pages au plus » est tenu de justesse ou dépassé selon la mise en page. Pour tenir, les titres des références sont réduits à leur partie principale et les auteurs abrégés (« et al. » au-delà de deux noms) ; versions complètes dans les cellules.
4. **Acronymes** : seulement dans les titres cités, les noms de fichiers et « SHA-256 » (nom donné par le brief).
5. **Fichiers en plus** : deux compagnons `.sha256`, par R6.
6. **Routine de reprise du dépôt** (R14) non exécutée, aucune passation écrite : la consigne limite les lectures à ce dossier et les écritures au dossier de sortie.
7. **Lectures propres à la synthèse**, marquées « lecture de cette synthèse » (deux endroits) : la condition du défaut dans les gabarits de A1, B1, C3 (§ 3) ; l'objection de C2 appliquée à l'échelle de l'avis (§ 4).
