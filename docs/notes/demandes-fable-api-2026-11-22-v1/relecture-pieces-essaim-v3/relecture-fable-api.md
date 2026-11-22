# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHUXp6ntMe5cnyYnxVCo`
- Heure (UTC) : 2026-11-22T06:19:09Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-correction-motif-duel-v1.md` — sha256 0795c9fb613ab6d25c69074a631d6fbae7063e075660cb88acd692fc0dee145e (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/pieces-comparaison-essaim-v3.md` — sha256 3931390197977729947f87cf66cd7ce8e388639f10de18692d618ed786886734 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve-motifs-correction-28-v1.md` — sha256 d1270c2b7dab522169d8c7328d4542a9dab5710f6eca9924ca61e7485c1b2d2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve_motifs_correction_28_v1.py` — sha256 314c293c0efec278b14b4ad5e6a3715adbce4854958a7317fd3cd2faf80beaca (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/table-corrections-pieces-essaim-v3.md` — sha256 e05c26a91496a99c6df8c1fa2580a806abeae74afb9b262a0e7be75fdf73b68b (compagnon : vérifié)
- Empreinte de l'invite envoyée : e43d18af14159dee65318ecc8aaba57adec3822a85a1ad2d3d2f2c281c153b81
- Jetons : entrée 24251, sortie 25276 (dont réflexion 22019), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.205048 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Correction du motif de duel, version 3 : corrections 43 et 44

**Verdict : scellable après ces corrections et la réussite de l'épreuve rejouée.**

Je n'ai rien exécuté. La règle ci-dessous a été suivie à la main, ligne par ligne, sur les dix textes du script ; c'est l'épreuve rejouée qui fait foi. Je n'ai lu ni cellule ni le script du collisionneur.

## Correction 43 : article 4, motif de duel

Le motif seul ne peut pas suffire. La suite des mentions est la même dans un duel du texte 3 (titre « H_A contre H_B », puis une puce H_A, une puce H_B) et dans deux duels du texte 9 (une ligne « H_A : … ; H_B : … » chacun). Il faut donc une règle sur les lignes.

**ANCIEN**

Un duel commence à chaque ligne de cette section qui contient `H_?A\b` ou `H₁`, et finit au duel suivant ou à la fin de la section.

**NOUVEAU**

Dans cette section, casse respectée, « A » désigne toute occurrence de `\bH_?A\b` ou `\bH₁`, et « B » toute occurrence de `\bH_?B\b` ou `\bH₂`. Une ligne d'opposition est une ligne où un A est suivi d'un B (`A.*B`). Une ligne d'amorce est une ligne qui contient un A, qui n'est pas une ligne d'opposition, et telle que la première occurrence de A ou de B dans les lignes suivantes de la section est un B. Un duel commence à chaque ligne d'opposition ; il commence aussi à chaque ligne d'amorce placée avant la première ligne d'opposition de la section. Aucune autre ligne n'ouvre de duel, et une ligne en ouvre un au plus. Un duel finit à l'ouverture du duel suivant ou à la fin de la section.

**Casse.** Elle est respectée pour A et B : H, A et B en majuscules, comme dans les consignes. Elle reste ignorée pour les motifs de section (b) et (c), qui ne changent pas. Le `\b` ajouté en tête évite « SHA-256 » ou « ALPHA », que l'ancien motif prenait pour H_A.

**Délimitation.** Rien d'autre ne bouge :
- La recherche de la « première occurrence dans les lignes suivantes » s'arrête à la fin de la section.
- La ligne de titre de la section reste dans la section.
- Le texte placé avant le premier duel n'appartient à aucun duel.

**Dans le script (version 2).** Les dix textes et les nombres attendus restent tels quels. `MOTIF_DUEL` et la ligne `ouvertures = …` de `duels()` sont remplacés par :

```python
HA = r"\bH_?A\b|\bH₁"
HB = r"\bH_?B\b|\bH₂"
MOTIF_A = re.compile(HA)                                  # casse respectée
MOTIF_A_OU_B = re.compile(f"{HA}|{HB}")
MOTIF_OPPOSITION = re.compile(f"(?:{HA}).*(?:{HB})")


def ouvertures_duels(section):
    premiere = [MOTIF_A_OU_B.search(l) for l in section]   # première occurrence de A ou de B, par ligne
    ouvertures, opposition_vue = [], False
    for k, ligne in enumerate(section):
        if MOTIF_OPPOSITION.search(ligne):
            ouvertures.append(k)
            opposition_vue = True
        elif not opposition_vue and MOTIF_A.search(ligne):
            suivante = next((m for m in premiere[k + 1:] if m), None)
            if suivante and suivante.group().endswith(("B", "₂")):
                ouvertures.append(k)
    return ouvertures
```

Dans `duels()` : `ouvertures = ouvertures_duels(section)`.

**Trace à la main sur les dix textes.**

| Texte | Attendu | Lignes qui ouvrent | Obtenu |
|---|---|---|---|
| 1 | 2 | deux lignes d'opposition (« H_A : … ; contre H_B : … ») | 2 |
| 2 | 3 | aucune opposition ; trois amorces (« - H_A : » suivie de « - H_B : ») | 3 |
| 3 | 2 | les deux titres « H_A contre H_B » ; les puces H_A viennent après une opposition ; « falsifie H_A » et « sous H_A » ne sont pas suivies d'un B | 2 |
| 4 | 2 | les deux titres « — H_A contre H_B » ; même raisonnement | 2 |
| 5 | 2 | les deux lignes « H₁ contre H₂ » ; « falsifie H₁ » est suivie d'un H₁ | 2 |
| 6 | 1 | une ligne d'opposition | 1 |
| 7 | 2 | deux lignes d'opposition ; la mention en (c) est hors section | 2 |
| 8 | 2 | deux lignes d'opposition (« HA, … ; HB, … ») | 2 |
| 9 | 3 | trois lignes d'opposition ; la mention en (a) est hors section | 3 |
| 10 | 2 | aucune opposition (la dernière ligne porte B puis A) ; amorces aux deux lignes « On oppose H_A, » ; « falsifie H_A est » est suivie d'un H_A | 2 |

**Limites connues, sans changement de texte.**
- **Rappel sur une ligne.** Une ligne interne à un duel qui nomme A puis B (« H_A si l'écart dépasse 0,1, sinon H_B ») ouvre un duel en trop. Aucun des dix textes ne porte ce cas.
- **Section mixte.** Un duel sans ligne d'opposition, placé après un duel qui en a une, n'est pas compté.
- **L'épreuve n'est plus aveugle.** J'ai écrit la règle après avoir lu les dix textes. Sa réussite montre que la règle les couvre, pas qu'elle couvre les cellules.
- **Recommandation.** Faire écrire deux ou trois textes de plus par une session qui n'a pas lu la correction 43, dont un avec un rappel sur une ligne, et les jouer à titre indicatif. Je n'en fais pas une condition du scellement ; la décision revient au directeur.

## Point 1 : correction 34

Je maintiens la prévision « facultatif » à **0,05**, sans mention. Le repli n'est pas porté et le texte ne change pas.

- **Cohérence avec l'article 11.** L'article dit lui-même que le seuil de révision est atteint dès qu'un duel perd un cinquième de ses mots pleins ou en remplace un sur neuf. J'ai revérifié ce calcul : il est exact. Garder 0,15 à côté de cette phrase serait contradictoire.
- **Pas de regard sur l'issue.** La baisse vient de l'arithmétique de la règle, pas d'une donnée : rien n'est scellé ni calculé, aucune cellule n'a été lue.
- **Une prévision étiquetée ne se note pas.** Sceller 0,15 avec « antérieur à la contre-lecture » donnerait une prévision qu'on ne pourrait pas confronter au résultat.
- **Trace.** L'ancienne valeur reste lisible dans la version 2 et dans la table des corrections.

## Point 2 : correction 39 → correction 44

Je ne peux pas établir que la garde de motifs lit un fichier tenu hors du dépôt : le script du collisionneur n'est pas dans les pièces. La puce affirme donc une capacité non vérifiée et ne doit pas être scellée telle quelle. Plutôt qu'une suppression nue, je propose un contrôle qui ne dépend pas de la garde.

**ANCIEN** (Pièce 2 (b), point 5)

Ces couples sont versés comme motifs interdits dans la garde de motifs du collisionneur, par un fichier tenu hors du dépôt comme la liste. La garde ne s'applique qu'aux textes écrits par le programme.

**NOUVEAU**

Ce contrôle est un script autonome, qui ne dépend pas de la garde de motifs du collisionneur. Celui qui détient la liste le lance hors des sessions, avant chaque exécution, sur les textes à servir. Il n'écrit au journal que « passe » ou « échoue » et le nombre de textes lus, jamais le couple trouvé.

Si le directeur préfère le minimum, la suppression pure de la puce reste acceptable. La puce précédente (« Un contrôle mécanique vérifie… ») et la liste d'arrêt de la pièce 2 (a) portent déjà l'exigence ; seul le mode d'exécution resterait à préciser.

## Suite

1. Porter 43 et 44 ; la correction 34 reste telle qu'elle est en version 3.
2. Rejouer l'épreuve avec le script en version 2 : mêmes dix textes, mêmes nombres attendus, 10 sur 10 exigé.
3. Si un texte échoue, les motifs ne sont pas scellés et le verdict redevient « à corriger ».

FIN DE LA RÉPONSE
