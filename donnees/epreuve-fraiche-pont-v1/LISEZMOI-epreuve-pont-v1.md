# « Épreuve fraîche » du pont fiche → loi, premier essai — LISEZMOI v1

Rédigé le 1er novembre 2026, achevé vers 17:30 UTC (relevé `date -u` de 17:27), par un sous-agent neuf de session-depot, pour
GO-2026-11-01-09 (plafond 5 dollars, échéance 2026-11-08, mot direct de Lazar). **Rien n'a été lancé** : aucun appel de modèle,
aucun appel réseau, aucune clé lue ; rien de scellé ni de commis ; aucun fichier existant modifié. Le rédacteur n'a lu des fiches
que `auteur`, `identifiant_auteur`, `passe`, `nom`, `empreinte` (et des longueurs) ; aucun énoncé.

## Ce qui est prêt

| fichier | rôle | SHA-256 |
|---|---|---|
| `preregistrement-epreuve-pont-v1.md` | préenregistrement court (brouillon : contre-lecture et deux marqueurs à remplir) | `41dc127b278b3c4faf1fc22145a8d1492f43644d7721fb7e9275999409b23789` |
| `tirer_fiches_v1.py` | tirage aveugle (SeedSequence), dédoublonnage, éligibilité Fable, vue anonyme, manifeste | `10b73a1f98c6344a9a4d3545372d6ee07c2ea55893846835dfdf99d39b9d4412` |
| `lancer_epreuve_pont_v1.py` | préparation, vérification des témoins, lancement, tour neuf (R-750), agrégat L1 à L5 | `eb7d2d37f673bc37ee41dd58b9f920927a8e39e7d0153405bfeb0e802a88bedd` |
| `lancer-epreuve-pont-v1.sh` | lanceur shell : clés sous `env -i`, relais Kimi par identifiant de processus, archive v56 vérifiée | `37fdb5ad805cc21b41f15225156a8d4a3b0ea9e3fa07e7cfa9b8f4448604e558` |
| `test_epreuve_pont_v1.py` | 83 essais hors réseau (faux appelants) | `238d7431668d74d9a9b2a3099b2da853fc7a2895ad7e767465faecd21317dce9` |
| `consigne-metteur-en-forme-temoins-v1.md` | consigne fermée du sous-agent qui écrit T1 à T6 | `cd4e4c42c6e611932cb6d2d6804adf8cce441cec16f332d1946e5b5d4dfa76b7` |
| `verite-temoins-v1.json` | vérité attendue des témoins (jamais servie) | `00030bb7ab72846de4426d3f6d1e42d775316eade92b24b0192402d929f8f429` |
| `catalogue-public-t05-v2-pont-v1.json` | catalogue servi : description publique réelle de `banque-t05-v2` (13 moniteurs, 4 traits) | `90f2440a966ad105867ac5fd04ead342e2d640ed9eef2759afa8fdfbd7eb1697` |
| `noyau-pont-t05-v2-v1.json` | état du noyau, jamais servi : 13 prédicteurs connus, épreuve lue, sonde (40), canaris (80) | `4c07e7b46a4d239d8d34e4fbacb9a23de0a94097e1d0f79b6845c1deb106a44d` |

Catalogue et noyau : produits par `lancer_epreuve_pont_v1.py preparer` avec le **vrai code de l'orchestrateur v56**
(`MondeBanque.description_publique`, `predicteurs_connus_publics`), archive `CODE-orchestrateur-pole-v7-v56.zip`
(`29b1b38c…`, conforme à son compagnon) tirée de `origin/canal/conv-audit-n04` (code seulement ; aucune ref `donnees/*` lue),
banque `exemples/banque-t05-v2.json` (`f26cc857…`) ; aucune issue n'y est écrite. Reproductible avec numpy 2.4.6.

**Essais** (Python du dépôt 3.13.18, pytest 9.1.1, `python -I -B`, depuis un dossier vide) :
- avec `PONT_POLE_V56=<dossier de l'archive v56 dépliée>` : **83 réussis** (dont le bout en bout : tirage réel dans un dossier
  temporaire, témoins validés par le vrai `valider_fiche_ideation`, vraie garde `valider_proposition`, lancement, tour neuf) ;
- sans : **74 réussis, 9 ignorés** avec leur motif ;
- essais du module du pont inchangés : 82 réussis avec la v56 ;
- banc de mutations (hors dépôt) : **25 tuées sur 25** ; un premier passage avait laissé 3 survivantes (garde A4 du tirage,
  entropie sans la valeur engagée, tolérance d'effet des témoins aller-retour), tuées par trois essais ajoutés. Audit R4 :
  25 sur 25 ne prouve pas l'absence de garde manquante.

Jouer : `cd <dossier vide> && PONT_POLE_V56=<v56> /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider /home/user/controle-ia-travail/donnees/epreuve-fraiche-pont-v1/test_epreuve_pont_v1.py`

## Ordre exact des gestes (session-depot)

1. **Contre-lecture R2** du préenregistrement par un sous-agent neuf (ni le rédacteur, ni conv-audit) ; lui donner
   explicitement les fichiers listés dans la section « Contre-lecture » du préenregistrement ; **jamais les fiches**. Toute
   correction d'un fichier gelé = nouveau nom (R12) et nouvelle empreinte dans le tableau « Pièces gelées ».
2. **Valeur engagée**, hors du dépôt, jamais montrée avant le scellement :
   `python3 -c "import secrets; print(secrets.token_hex(32))" > <bloc-notes>/valeur-engagee-pont-v1.txt` ;
   empreinte : `printf %s "$(cat <bloc-notes>/valeur-engagee-pont-v1.txt)" | sha256sum`.
3. **Remplir** dans le préenregistrement : `<<EMPREINTE_VALEUR_ENGAGEE>>` (l'empreinte, entre accents graves),
   `<<COMMIT_DU_DEPOT>>` (`git rev-parse --short HEAD`), la section « Contre-lecture » (au format « Contre-lecture 1 », avec
   l'empreinte du brouillon relu et celle du rapport). Le validateur refuse tant qu'un marqueur reste.
4. **Sceller** (depuis la racine, `PYTHONPATH=src`) :
   `python -c "from controle_ia.prereg import sceller_prereg; print(sceller_prereg('donnees/epreuve-fraiche-pont-v1/preregistrement-epreuve-pont-v1.md'))"`,
   puis `python -m controle_ia.scellement sceller` sur `tirer_fiches_v1.py`, `lancer_epreuve_pont_v1.py`,
   `lancer-epreuve-pont-v1.sh`, `test_epreuve_pont_v1.py`, `consigne-metteur-en-forme-temoins-v1.md`, `verite-temoins-v1.json`,
   `catalogue-public-t05-v2-pont-v1.json`, `noyau-pont-t05-v2-v1.json` (le lanceur exige ces compagnons).
5. **Tirage** : `cd donnees/epreuve-fraiche-pont-v1 && /home/user/controle-ia-travail/.venv/bin/python -I -B tirer_fiches_v1.py --valeur-engagee <bloc-notes>/valeur-engagee-pont-v1.txt`
   → `fiches-tirees/F-01.json` … `F-08.json` et `manifeste-tirage-v1.json` (compagnons écrits). Ne pas ouvrir les fiches.
6. **Témoins** : déplier l'archive v56 hors du dépôt —
   `V=<bloc-notes>/v56-epreuve-pont && mkdir -p $V && git -C /home/user/controle-ia-travail show origin/canal/conv-audit-n04:docs/notes/ideation-organisme-v1/orchestrateur-v56/CODE-orchestrateur-pole-v7-v56.zip > $V/CODE-orchestrateur-pole-v7-v56.zip && echo "29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c  $V/CODE-orchestrateur-pole-v7-v56.zip" | sha256sum -c - && mkdir $V/orchestrateur-v56 && python3 -I -B -m zipfile -e $V/CODE-orchestrateur-pole-v7-v56.zip $V/orchestrateur-v56` ;
   lancer **un sous-agent neuf** avec pour seule pièce `consigne-metteur-en-forme-temoins-v1.md` et, dans la lettre de
   mission, `DOSSIER_V56=$V/orchestrateur-v56` ; il écrit `temoins/T1.json` … `T6.json` et les fait passer
   `verifier-temoins`. Puis session-depot relance `verifier-temoins` elle-même et scelle les six fichiers.
7. **Lancement** (en tâche de fond ; ≈ 1 heure attendue, borne 7 000 secondes) :
   `cd donnees/epreuve-fraiche-pont-v1 && GO_ID=GO-2026-11-01-09 bash lancer-epreuve-pont-v1.sh lancer run-epreuve-pont-v1 3`
   (les variables `GEMINI_API_KEY_2` et `KIMI_API_KEY` sont prises de l'environnement de la session ; jamais tapées dans un
   fichier ni en argument). Sorties : `run-epreuve-pont-v1/` — `manifeste-run.json`, `items/item-kk/` (texte servi, réponses
   brutes, métadonnées d'appel, `resultat.json` avec la fiche-loi), `journal.jsonl`, `manifeste-run-fin.json`, `agregat-v1.json`,
   journal et sortie du relais Kimi. Port du relais : 8802.
8. **Si refus** (R-750) : écrire un préambule plus technique et plus spécifique (domaine, vocabulaire défini, livrable précis)
   d'après la **catégorie** du refus (jamais la fiche), le sceller, puis
   `GO_ID=GO-2026-11-01-09 bash lancer-epreuve-pont-v1.sh reprendre-refus run-epreuve-pont-v1 <préambule> run-epreuve-pont-v1-reprise 3`
   (une seule fois ; plafond cumulé ; `agregat-reprise-v1.json` fusionne les deux tours). Si le processus est tué (borne de
   durée), `lancer_epreuve_pont_v1.py agreger --run run-epreuve-pont-v1` reconstruit l'agrégat (marqué « reconstruit »).
9. **Lecture** par un **lecteur neuf** : il applique les critères L1 à L5 gelés à l'agrégat, fait l'audit de symétrie (R4) si
   l'agrégat le signale, peut relire les réponses brutes des témoins, écrit la lecture agrégée ; c'est elle seule qui va à
   conv-audit (jamais les fiches, les réponses ni les fiches-lois).
10. **Consigner** : dépense (`registres/depenses.md`), décisions, passation ; sceller la lecture.

## Ce qui reste

1. Contre-lecture R2, valeur engagée, commit, scellement (gestes 1 à 4) ; tirage ; témoins par le sous-agent tiers ; lancement ;
   lecture par un lecteur neuf.
2. **Coût** : estimé ≈ 3,3 dollars (fourchette 2,0 à 6,4, SUPPOSÉ ; barèmes Argon 10/50, Kimi 2/10 par million de jetons) ; la
   garde de plafond (pire cas ≈ 0,64 par appel d'Argon) peut arrêter le tour avant la fin : lecture partielle selon les règles
   de lisibilité du préenregistrement, complément sur nouveau devis.
3. Non vérifié ici faute d'appel réel : format exact des réponses de Kimi et d'Argon à cette consigne (le module renvoie N10 si
   aucun bloc conforme) ; durée des appels de Kimi (jusqu'à 1 800 secondes par appel au relais).

## Réserves

1. Le noyau v56 et le catalogue réels **ont été trouvés** (archive v56 de la branche conv-audit) ; la couche v57 n'existe pas :
   stratégie du pont ajoutée **en mémoire** au catalogue du vrai proposeur, dans le processus du lanceur (écart 8 déclaré).
2. Les témoins nomment des objets du catalogue réel, ce que les fiches de la course 1 ne font pas : un traducteur pourrait les
   reconnaître (limite dite au préenregistrement).
3. Les choix 5 à 12 du préenregistrement sont du rédacteur : à juger par la contre-lecture.
4. Les prédicteurs connus du noyau sont ajustés sur le calibrage (aucune lecture de l'épreuve) ; ils n'entrent que dans la
   divergence rapportée et la puissance approchée, jamais dans le classement (toute épreuve est lue).
