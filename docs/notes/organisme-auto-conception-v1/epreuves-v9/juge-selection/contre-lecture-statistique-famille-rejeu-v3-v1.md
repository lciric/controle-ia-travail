# Contre-lecture de la statistique de famille du rejeu à blanc v3 et de son programme — v1

Contre-lecteur de repli : le contre-lecteur prévu (modèle K) a été refusé pour limite d'usage le 2026-11-19 vers 14:50Z ; repli selon la consigne de la mère pour les vérifications.

- **Contre-lecteur** : modèle S (neuf ; je n'ai écrit ni la statistique, ni le programme, ni les essais, ni aucune carte). Auteur lu : modèle L′.
- **Heure** : 2026-11-19, `date -u` au début de la lecture : 2026-11-19T14:48:37Z. Hors ligne, processeur seul, aucune dépense, aucun appel de modèle, aucune valeur de clé.
- **Non ouverts** : `fiches.json`, toute carte, le champ `meta`, `diag/`, `donnees/`, bras d'attaque, conservation des réponses, `.claude/`, coffre. Le programme n'a pas été lancé sur les vraies cartes ; seuls les essais synthétiques ont tourné.

## Empreintes lues

| pièce | sha256 | attendu |
|---|---|---|
| `statistique-famille-rejeu-v3-v1.md` | `bb2fa4a8c849e8f981a5cd27c747d97735bd3b364802a37dda9f0c68f4114738` | conforme, compagnon `.sha256` vérifié |
| `statistique_famille_rejeu_v3_v1.py` | `298dde07f18cdaddde6438bbced8e378afd45ad87eb4921567c8be8838a5683d` | conforme, compagnon vérifié |
| `tests/test_statistique_famille_rejeu_v3_v1.py` | `4c465d5035f97b1f5b9b26715a6270b79a3683d170b4ef0fd7fb7c53d2a576ae` | conforme |
| `statistique-famille-rejeu-v3-essais-sortie-v1.txt` | `0ff060a28543bf4258bebe8157ab0d5f5a0de15491064d99d5b8d43dcfac3805` | conforme |
| `audit-symetrie-rejeu-v2-v1.md` | `ff814fc980925ea4304c2a784c20e41378fc11d92b2b08d3eb835a71451d4673` | conforme |
| `configuration-course-auto-conception-v5.json` | `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8` | cohérent avec le § 0 du texte |
| orchestrateur `a41b7b50f7c6…` (HEAD de `/home/user/ideation-organism`), `orchestrator/pole/course2_v54.py` | `ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342` | conforme à celle citée au § 0 du texte |

## Constats

1. **Empreintes** : toutes conformes (tableau ci-dessus). Le chemin de l'orchestrateur est `orchestrator/pole/course2_v54.py`, non à la racine ; le texte le donne sous cette forme.
2. **Réponse à la demande** : la statistique compare la part de la famille des lecteurs (Opus, Fable) dans les trois listes (note maximale, nombre visé, veto) à deux bases (sur les 94, parmi les notées). Elle donne la permutation stratifiée par voie (20 000), le calcul exact, le descriptif par lignée sans test, par lecteur (F, O, programme) et pour l'assemblage. Conforme.
3. **Ce que le programme lit des cartes** : la seule fonction `extraire_especes` touche aux enregistrements, par `rec["meta"]` puis `meta["proposeur"]` ; `CHEMIN_ESPECE` est constant et tout autre chemin est refusé ; l'objet est supprimé (`del fiches`) aussitôt. Je l'ai lu dans le code. L'essai espion (`test_extraction_d_une_seule_cle`) enregistre les accès sur tous les niveaux imbriqués : seules les clés `meta` et `proposeur`, et seulement par lecture ou test d'appartenance, jamais par parcours. Le décodage du JSON traverse le fichier entier, ce que le texte dit (§ 2, point 4). La clé `meta.proposeur` est bien écrite par `f["meta"]["proposeur"] = p["etiquette"]` dans `course2_v54.py` (ligne 161) ; les étiquettes de la table sont celles de la configuration v5. Réserve reprise du texte : le fichier n'a pas été ouvert, donc la clé n'est pas vérifiée sur lui ; les gardes (étiquette hors table refusée, totaux par lignée comparés à la pièce, tout « non concluant » en cas d'écart) la couvrent.
4. **Justesse statistique** :
   - la permutation est faite par voie, avec effectifs de la famille conservés ; statistique T = k − E, E stratifié ; p bilatérale (1 + #{|T*| ≥ |T|}) / (n + 1), les deux unilatérales rapportées ; tolérance numérique 10⁻⁹ ;
   - le calcul exact est la convolution de lois hypergéométriques en fractions : je l'ai recoupé par énumération complète sur trois voies (5, 2, 3), (4, 3, 2), (3, 1, 1) : lois identiques ;
   - la p minimale atteignable est le minimum, sur les valeurs possibles de k, de la p exacte bilatérale : correcte ;
   - Holm : recoupé à la main ({0,01 ; 0,02 ; 0,04 ; 0,5} donne {0,04 ; 0,06 ; 0,08 ; 0,5}) ; appliqué séparément à la permutation et à l'exact, sur les seuls tests concluants ;
   - règle « non concluant » : les six conditions du § 5 sont toutes dans `lire`, ainsi que le désaccord permutation/exact après Holm ; une p minimale NaN tombe en « non concluant » (pas de repli silencieux) ;
   - graine (R9) : `SeedSequence` d'entropie sha256 du texte, `spawn(4)`, un enfant par ensemble selon l'ordre fixe F, O, programme, assemblage quels que soient les ensembles présents ; version de numpy exigée ≥ 1,25 et écrite en sortie avec l'entropie et l'empreinte du programme. Reproductibilité testée.
5. **Refus et sorties** : empreinte vérifiée pour toutes les entrées avant toute lecture (illisible, absente ou différente : refus, code 2, rien d'écrit) ; cartes différentes de celles de la v9 refusées hors `--essai-synthetique` ; refus d'écraser la sortie, le résumé et leurs compagnons (R12), testé ; sortie sans identifiant ni espèce par carte (test sur valeurs sentinelles). Les identifiants de cartes de liste inconnus sont refusés, les doublons retirés et comptés, les cartes hors population sorties du test et comptées.
6. **Essais** : lancés au premier plan par la commande demandée : **29 passés sur 29** en 2,69 s, identique à la sortie scellée des essais. Couverts : cas sain, artefact planté dans les deux sens, refus d'empreinte, refus d'un autre champ, stratification exacte, concordance permutation/exact, calibration sous le nul, petits effectifs, Holm, reproductibilité, refus d'écraser, quatre correspondances refusées, identifiant inconnu.
7. **Commande pour la mère** (§ 7) : autonome (vérification des compagnons, chemin des cartes et empreinte, correspondance, quatre sélections avec empreintes, sortie et résumé neufs). Le dossier d'archives des cartes existe ; numpy 2.5.3 sous `-I`, donc l'isolement ne cache pas la bibliothèque. Le fichier de correspondance est bien défini : clés `piece`, `ecrite_utc`, `ensembles` seules ; par ensemble `cartes`, `voie`, `note` exigées, `id`, `exclue`, `nombre_vise`, `veto` facultatives, toute autre clé refusée ; l'ensemble des noms de la correspondance doit égaler celui des sélections passées ; `id` null exigé pour un objet, pointeur exigé pour une liste ; pointeur faux ou clé manquante dans un enregistrement : refus, jamais « non notée » ; valeur nulle de voie ou de note : « non notée », comptée.

### Remarques mineures, sans effet sur la scellabilité

- Une carte sans espèce dans la population rend toutes les listes de l'ensemble « non concluant » : prudent, dit au § 5, à ne pas confondre avec un défaut.
- Les p exacte et de permutation sont bilatérales sur T ; le sens n'est lu que par le signe de T sur les listes concluantes : cohérent avec le texte.
- Le veto « titulaires seulement, avant retrait par lignée » dépend de la correspondance écrite par la mère, non du programme : à écrire avec soin avant le lancement.

## Corrections

Aucune exigée.

## Verdict

Scellable.

Aucune correction. La statistique répond à la demande, le programme ne lit que `meta.proposeur`, la justesse statistique est recoupée (exact par énumération, Holm à la main, essais 29 sur 29), les refus et la sortie sans identifiant tiennent, la commande de la mère est juste et autonome. Contre-lecteur de repli : ce verdict n'a pas la portée d'une lecture par le contre-lecteur prévu pour ce qui touche au fond de la règle de lecture (seuil 0,05, minimum de 3 cartes, Holm : choix de conception que le texte laisse à la mère).
