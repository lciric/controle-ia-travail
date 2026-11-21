# Vérification des corrections de la réponse du concepteur sur la boucle « audit, recapture, réapprentissage » (v2)

- **Date** : 21 novembre 2026, 16:28 UTC (`date -u`).
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), même contre-lecteur que la v1 (R-3735), sur mandat de la session mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Pièce de classe C. Aucun appel payant, ni commit ni poussée.
- **Contre-lecture vérifiée** : `contre-lecture-reponse-fable-boucle-audit-recapture-v1-opus-v1.md` (`c73df63d352068d86b8f9563242cdc62e6e974848f6425cf30a0f155b25ab7ef`), seize constats.
- **Pièces lues, empreintes égales à leurs compagnons** (`sha256sum -c` : « OK » pour chacune) :
  - `reponse-fable-boucle-audit-recapture-v2.md` (`3bc8585c…`). Lu : en-tête, table des constats, verdict, sections 2, 3 (ligne 7), 5 en entier, 6 (épreuves 1, 7 et 13), 7, 8 (ligne Taufeeque et al.), 9, et les décisions D-1 à D-6 ;
  - `collisionneur-v2/faits-boucle-audit-recapture-v2.md` et `collisionneur-v2/question-boucle-audit-recapture-v2.md` ;
  - `question-organisme-boucle-audit-recapture-v2.md`.
  - L'écart avec les pièces de la v1 a été établi par `diff` et `cmp`.
- **Pour la précision (i)** :
  - `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3-v2.md` (`fbe3298ec358fa9b8d041d8675d9ad3369e99591572c8281806f0ade75463b04`), section 2, lignes 64 à 72 ;
  - N-075 v3, l. 247 ;
  - N-060 v3, point 4.

## Verdict

**Conforme.** Les seize constats sont portés, quinze justement ; le sixième est porté justement, mais il était en partie faux de mon côté. Aucun constat ne manque. Le bloquant est levé :
- l'interdit redevient général, avec une seule exception ;
- le rôle « hors rôle » est défini et reste sous l'interdit entier ;
- le bras de flux est déclaré par un texte scellé sur le mot de Lazar, disjoint des portes, de la famille tenue à l'écart et du jeu final ;
- les versions nées du flux sont closes aux concepteurs et à l'auteur du mode tenu à l'écart, et elles ont leur épreuve (la 13).

La précision (i) est citée mot pour mot et confrontée aux cinq points de l'erratum 3 v2 ; sa restriction est l'un des huit oui de D-1. (b′) reste un nœud sans défaut, et la règle d'attente de l'erratum 3 est reprise.

Il reste un écart mineur (constat R-1) ; il ne demande pas une nouvelle version.

## Les seize constats

| n° | État | Où | Remarque |
|---|---|---|---|
| 1 | porté juste | Texte proposé pour le point 4 ; définitions (« hors rôle », bras de flux, enclave) ; clause 1 ; épreuve 1 | « Hors de cette exception, l'interdit vaut pour tout épisode, quel que soit son usage » ferme le trou. |
| 2 | porté juste | Clause 5 ; dernière phrase du texte proposé ; P3 ; ligne 7 de la section 3 ; épreuve 13 | La lecture « seulement » est fermée : l'oracle, ses consignes, la référence cachée, chaque verdict et chaque version restent inaccessibles. |
| 3 | porté juste | Clause 6 ; D-1, point 5 | Le défaut est exogène et l'autre choix demande le mot de Lazar. Le prix du défaut (la sonde « lit le suspect ») est dit, ce qui va au-delà de ma correction. |
| 4 | porté juste | Section 5, alinéa sur la précision (i) ; flèche γ ; verdict, point 9 ; D-1, point 4 | Le texte cité est exact (N-075 v3, l. 247). Le statut « à confirmer » est conforme à l'erratum 3 v2 (l. 70). Les cinq points sont exacts (l. 72) ; ils sont en section 2 de l'erratum, comme la note le dit. La restriction proposée garde le premier membre (« l'annonce ne déclenche aucune leçon »). |
| 5 | porté juste | Définition du bras de flux ; raison (i) ; verdict, point 2 ; D-1 | « (b′) n'est pas (b) mieux écrite » est dit en clair. |
| 6 | porté juste, constat en partie faux | Texte proposé, phrase 1 ; remarques 1 et 2 ; D-1, point 6 | « Entraînement » est retiré côté agent. Sur « (N-053) », le rédacteur a raison : la parenthèse est celle de N-060 v3, point 4, et non un ajout de la note. Mon constat la lui attribuait à tort. Le renvoi à Lazar est la bonne suite. |
| 7 | porté juste | D-4, troisième heurt ; verdict, point 8 | La note dit honnêtement que la lecture cède aussi sur l'esprit de l'invariant. |
| 8 | porté juste | D-2 | Aucun défaut ; l'ordre d'écriture est subordonné à N-076 (§ 13, point 8). |
| 9 | porté juste | En-tête | Le constat est porté dans la v2 plutôt que par un erratum, ce qui est déclaré. |
| 10 | porté juste | D-3 ; section 7, étape 1 | La note ajoute que la règle d'attente « mondes plantés » demande le mot de Lazar même pour l'étape 1 : juste. |
| 11 | porté juste | Clause 5 ; texte proposé | — |
| 12 | porté juste | Texte proposé ; D-1, point 1 | — |
| 13 | porté juste | Verdict, point 6 ; section 7 | — |
| 14 | porté juste | Section 8 | — |
| 15 | porté juste | Faits v2, l. 15 | La phrase proposée est reprise mot pour mot. |
| 16 | porté juste | Question de l'organisme v2 | — |

## Les trois écarts signalés par le rédacteur, tranchés

1. **Trois règles ajoutées aux faits, au-delà du constat 15 : écart accepté.**
   - Ce sont des règles en vigueur ou proposées du programme : les témoins (N-075, point 8 (a)), les moniteurs amnésiques (programme, § 9), et « annoncer n'est pas sélectionner » donnée comme non confirmée.
   - Elles sont fidèlement résumées ; la précision (iii), qui étend la lecture sans la conditionner, est omise sans dommage.
   - Elles ne nomment ni le programme, ni une personne, ni un chemin, et ne livrent ni (b′), ni ses clauses, ni un chiffre.
   - Elles pèsent plutôt contre un assouplissement, donc pas dans le sens de la note. Sans elles, le collisionneur jugerait les options sans connaître les règles qu'elles heurtent.
2. **« (N-053) » : le rédacteur a raison** (constat 6 ci-dessus). Ma correction proposait de « retirer » une parenthèse qui n'était pas de lui ; le signalement à Lazar est la bonne suite.
3. **L'empreinte `1c3d2b66…` que j'ai citée pour l'erratum 3 : erreur de ma part, confirmée.**
   - Je l'ai calculée vers 16:10 UTC, sur le fichier de l'erratum 3 alors en cours d'écriture (33 949 octets, écrit à 16:08:24), avant son état final de 16:10:59 et son scellement de 16:11:25.
   - Empreintes justes : erratum 3 scellé `d51863d24a3798641ce6fd7665ff8db89bd6089f52d643e4a5bccb42a2aef3fd` ; erratum 3 v2 `fbe3298ec358fa9b8d041d8675d9ad3369e99591572c8281806f0ade75463b04`, celui que la v2 de la note emploie.
   - Ma contre-lecture, scellée, n'est pas réécrite (R12) : cette ligne en tient lieu d'erratum.
   - Leçon : ne citer l'empreinte que d'un fichier dont le compagnon existe et concorde.

## Le couple v2

**Neutre.** La question du collisionneur est identique à l'octet à celle de la v1 (`cmp`). Une recherche par motifs sur les deux faits et la question de l'organisme ne trouve rien. Les motifs cherchés :
- un nom de personne ou de modèle maison ;
- un identifiant de décision, d'accord ou de registre ;
- un chemin ;
- « (b′) » ou « épreuve puis leçon ».

La phrase sur le « service » est neutre. Le mécanisme (3) de l'organisme ne nomme plus de réponse.

## Constat résiduel

| n° | Gravité | Lieu | Constat | Correction |
|---|---|---|---|---|
| R-1 | mineur | Texte proposé pour le point 4, « Un bras de flux est déclaré par un texte scellé » | La définition de la section 5 et D-1 (point 2) disent « de la classe décisive » ; le texte proposé pour la décision l'omet. | À porter dans la pièce décisive qui écrira l'amendement : « par un texte scellé de la classe décisive ». |

Hors de la note : l'erratum 3 v2 ne dit pas, dans son propre texte, qu'il remplace l'erratum 3 (même en-tête). C'est à signaler à la mère, pas au rédacteur de la note.
