# LISEZMOI — comparaison à plusieurs bras des règles de choix de paire — v1

Lignée conv-audit, concepteur neuf (Opus), 1er novembre 2026, 15:48 à 16:06 UTC (heures lues par `date -u`).
Mandat : décision de Lazar du 1er novembre, 15:47 UTC (`registres/decisions.md`, R-1051 point 7, sur la reformulation de R-1049).
Rien n'est commité ; aucun compagnon `.sha256` (consigne) ; aucun fichier existant modifié ; rien lu sous `donnees/` ; aucun appel de modèle ; aucune dépense ; aucun résultat décisif lu : seuls des mondes jouets.

## Fichiers et empreintes SHA-256 (calculées par `sha256sum`)

| Fichier | Rôle | SHA-256 |
|---|---|---|
| `conception-comparaison-regles-paires-v1.md` | conception : interface, sept bras, deux épreuves, puissance, multiplicité, Science4Cast, panel, règle d'entrée, gardes, décisions, devis | `f43be110ab5186e316df770d1d8b88e3f086ff4a70957afef49c469dccc0431b` |
| `preenregistrement-comparaison-regles-paires-v1-brouillon1.md` | préenregistrement au gabarit, brouillon 1, non contre-lu | `1ba8bf6de59be36e28bbf0800931458711908ae473945393fb59d9730ce29064` |
| `regles_paires_v1.py` | interface commune, quatre bras codés, trois adaptateurs factices, rétrodiction jouet, gardes G1 à G10, DeLong, Holm, règle d'entrée | `fb80ea312ab12de7a09d2698c642e79b44ff6a0dd6100303a0878a5872baa983` |
| `essais/test_regles_paires_v1.py` | 20 essais : chaque garde sur un cas sain et un artefact ; bras à la main ; bout en bout ; monde nul | `7e5f6627926124ab03e415b1678f001f3c1902405eb8dce04f3eb1176d105855` |
| `calcul-puissance-comparaison-regles-paires-v1.py` | annexe : puissance reproductible (formules et simulation) | `3323d2f648c8ec6b90bd516cb8531d1882867c31ac9cdbf0a2eaf80c9216f7c0` |
| `calcul-puissance-comparaison-regles-paires-v1-sortie.txt` | sa sortie | `18d37d858175a492e1cdba58a3a46563e05252741fd039cb36013685b73f8596` |

Dépendance lue au chargement, empreinte vérifiée par le code : `retrodiction-swanson/code/mesures_v1.py` (`f462dbd52ecd9181e387da1ff1ceb1a529f3bcd07e6ca85d83e9a5898af0888f`), reprise telle quelle pour les métriques et le hasard.

## Relancer (dossier temporaire vide, chemins absolus, Python du système, numpy 2.5.3)

```
D=/home/claude/controle-ia-travail/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/comparaison-regles-paires-v1
cd "$(mktemp -d)"
python3 -I -B -m pytest -q -p no:cacheprovider $D/essais/test_regles_paires_v1.py     # 20 passed
python3 -I -B $D/essais/test_regles_paires_v1.py                                        # même chose sans pytest
python3 -I -B $D/calcul-puissance-comparaison-regles-paires-v1.py                       # redonne la sortie à l'octet près
python3 -I -B $D/regles_paires_v1.py                                                    # démonstration jouet
```

Sortie des essais (16:00 UTC) : `20 passed in 1.55s` ; sans pytest : `20/20 essais réussis`.

## Validateur du dépôt sur le brouillon de préenregistrement

`controle_ia.prereg.problemes` (`src/controle_ia/prereg.py`, `3b2e3ee5…`), lancé à 16:04 UTC :
```
section vide ou à remplir : Seuil
section vide ou à remplir : Contre-lecture
```
Attendu pour un brouillon : la section « Seuil » porte le marqueur du gabarit sur les huit valeurs que Lazar doit fixer (chacune avec recommandation) ; la contre-lecture R2 n'est pas faite. Toutes les autres sections exigées sont présentes et remplies.

## Chiffres clés

- Puissance, épreuve 1 (10 points d'aire, 0,8, Holm au pire rang α/6 unilatéral, contre hasard réalisé) : ≈ 182 positives ; ≈ 66 000 paires au taux de base 0,275 %, ≈ 18 400 à 1 % ; simulation 0,812 et 0,825. À 10⁶ paires : écart détectable ≈ 2,6 points.
- Puissance, épreuve 2 (intérêt de 1 à 5, écart-type ≈ 1,32 tiré de SciMuse) : Δ = 0,5 → 50 à 66 fusions par bras pour trois bras ; Δ = 0,3 → 138 à 184.
- Démonstration jouet (monde par fermeture de triangles, 863 paires candidates) : aires hasard 0,496, loin mais proche 0,524, Swanson 0,625, Adamic-Adar 0,650, allocation de ressources 0,653 ; entrent : Adamic-Adar, allocation de ressources, Swanson. Monde nul : aucun bras n'entre.

## Ce qui reste (prochaine action)

Décisions de Lazar (conception § 10) ; contre-lecture R2 du préenregistrement par un sous-agent neuf ; devis de session-depot (machine louée, moisson des métadonnées d'arXiv et complément OpenAlex) ; voie R-a de Gu-Krenn ; branchement des trois adaptateurs.
