# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHV7MBkQjF9u4Xv3xndV`
- Heure (UTC) : 2026-11-22T06:27:18Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-correction-motif-duel-v2.md` — sha256 d464e041af1de7037468cad1b6a6a500a11575c7f8e62ac30ff6df803221aced (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/pieces-comparaison-essaim-v4.md` — sha256 48caa135c62e82b50f27fd698a37f5d2554163e6af9a3a97d887f2a1dc510ab3 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve-aveugle-motifs-v1.md` — sha256 5fc15fc0ae4c9f24eb7066d2981f3a6a65dbeba8d3707783613b3a5ff47e1a67 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/textes-aveugles-epreuve-v1.json` — sha256 1dbdcb40554deaa27f64ca52b5834d33975b033d6f27534a10aebcdb2279774c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve_motifs_correction_28_v2.py` — sha256 d1caea7bdaa66ef2b18fdcf1b23b8d84a8c1d5b872fc52d4de637949e0d5d1ac (compagnon : vérifié)
- Empreinte de l'invite envoyée : 435cada206db79f6561089be449879f19909d49bb3481147554f7290edf3696b
- Jetons : entrée 24454, sortie 30566 (dont réflexion 24358), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.418272 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Repérage des duels : voie (b), balises pour l'avenir, description seule pour le passé

**Conclusion d'abord.**
- **Je tranche pour (b).** Aucune règle lexicale ne sépare une ouverture de duel d'un rappel sans lire le sens. Confiance : 0,85.
- **La balise doit figurer aux tours III.1 et III.3**, pas au seul III.1 : l'article 6 apparie les duels des deux tours.
- **Dossiers déjà joués : description seule**, sur le texte entier des cellules, sans duel ni verdict. Le troisième tour y reste obligatoire par défaut, non par résultat.
- **Le rapport de l'épreuve aveugle est à rejouer.** Ma trace à la main de la fonction `duels` ne retrouve aucun de ses trois nombres obtenus.

**Réserves.**
- Je n'ai exécuté aucun code : traces à la main, code de référence non exécuté.
- Je n'ai lu ni les lignes 528 à 546 du collisionneur, ni la règle R5, ni aucune cellule.

## 1. Constat : trois échecs sur trois, de trois sortes

| Texte | Attendu | Rapport | Ma trace | Lignes qui ouvrent un duel |
|---|---|---|---|---|
| 1 | 3 | 2 | 5 | l'amorce « - H_A : » du duel 1, les lignes « Seuil » et « Falsification » du duel 1, la « Falsification » du duel 2, la puce du duel 3 |
| 2 | 3 | 2 | 4 | l'en-tête du tableau, ses deux rangées, la ligne « Duel 3 » |
| 3 | 2 | 2 (passe) | 0 | aucune : « hypothèse A » ne contient ni `H_A` ni `HA`, casse respectée |

- **Texte 3.** La cellule serait invalide au sens de l'article 3. Le « passe » du rapport est incompatible avec le motif tel qu'il est écrit dans le script joint.
- **Rapport.** Sa dernière ligne (« Échec : 1 sur 3 ») contredit aussi son tableau, qui compte deux échecs. Il faut le rejouer et joindre la sortie brute.
- **Argument décisif (texte 1).** La ligne « Si H_A est vraie… ; sous H_B… » est un rappel, la puce « H_A : … ; H_B : … » ouvre le duel 3. Les deux ont la même forme : un A suivi d'un B sur une ligne.
- **Pas de rustine.** Les distinguer par le deux-points échouerait sur le texte 3 et sur le texte 10 de l'ancienne épreuve. Chaque rustine suit un style, et les dix textes écrits après coup n'en couvraient qu'un.

## 2. Corrections à porter sur la version 4 [PROPOSITION]

**Correction 44 — Conclusion, pièce 1.**
- ANCIEN : « La « piste » se définit mécaniquement, le « rang » non. »
- NOUVEAU : « La « piste » ne se compte mécaniquement que si le modèle la balise lui-même ; le « rang » ne se définit pas. »

**Correction 45 — Réserves, troisième puce.**
- ANCIEN : « Les duels ne portent aucune balise (contre-lecture, constat 2). J'ignore si le tour III.3 garde la forme H_A contre H_B, et si un modèle de ma famille figure parmi les cinq participants. »
- NOUVEAU : « Les duels des dossiers déjà joués ne portent aucune balise (contre-lecture, constat 2), et aucune règle lexicale ne les repère sûrement (épreuve aveugle 5fc15fc0…). Les dossiers futurs les balisent (article 4). J'ignore si un modèle de ma famille figure parmi les cinq participants. »

**Correction 46 — Section 3, première puce.**
- ANCIEN : « Découpage par expressions régulières (article 4). »
- NOUVEAU : « Découpage par balises imposées dans la consigne (article 4) ; aucun repérage lexical des duels. »

**Correction 47 — Article 1, ajout en fin d'article.**
- ANCIEN : « Elle ne peut le rendre facultatif qu'avec l'appui d'une mesure à oracle (article 10). »
- NOUVEAU : la même phrase, suivie de : « Les articles 2 à 13 valent pour les seuls dossiers joués avec la consigne balisée (article 4). Les dossiers joués avant elle relèvent de l'article 14 : description seule. »

**Correction 48 — Article 2, trois premières puces.**
- ANCIEN : de « Sont incluses toutes les questions dont les trois tours sont complets » à « Les résultats sont donnés avec et sans elles. »
- NOUVEAU :
  - « Sont incluses les huit premières questions jouées en mode isolé avec la consigne balisée après le scellement, dans l'ordre où leurs trois tours s'achèvent. Le calcul est lancé une seule fois, à la huitième. »
  - « Aucune n'est ajoutée ensuite. »
  - « Les exécutions de la comparaison (pièce 2) n'en sont pas : leur tour III.3 reçoit une erreur plantée. »
  - « Si deux questions partagent leur sujet, les résultats sont donnés avec et sans la seconde. »

**Correction 49 — Article 3, les trois puces.**
- ANCIEN : de « Une cellule est valide si » à « deux tirages indépendants diffèrent plus qu'une révision [HYPOTHÈSE]. »
- NOUVEAU :
  - « Une cellule est valide si ses tours III.1 et III.3 sont complets, dans la même langue, et tous deux conformes au sens de l'article 4. »
  - « Une cellule jouée sous un réglage autre que le réglage scellé (réflexion coupée, par exemple) est exclue de l'analyse principale et rapportée à part. »
- Les clauses sur Argon passent à l'article 14.

**Correction 50 — Article 4, en entier.**
- ANCIEN : de « **Article 4 — Piste.** Une piste est un duel d'hypothèses de la section (b). » à « Les pistes finales sont les duels de la section (b) du tour III.3. »
- NOUVEAU : « **Article 4 — Piste.** Une piste est un duel balisé par le modèle. La consigne des tours III.1 et III.3 impose deux balises, les mêmes en toute langue, casse respectée. *Ouverture* : ligne qui correspond à `^[\s>#*_|-]*\[DUEL\s*(\d+)\]`. *Clôture* : ligne qui correspond à `^[\s>#*_|-]*\[FIN DES DUELS\s*:\s*(\d+)\]`. Un tour est conforme si trois conditions tiennent : il compte une clôture et une seule ; les ouvertures portent, dans l'ordre, les numéros 1 à n, avec n au moins égal à 1, toutes avant la clôture ; la clôture déclare n. Un duel va de sa balise d'ouverture à l'ouverture suivante ou à la clôture ; il comprend le reste de sa ligne d'ouverture. Seuls les duels balisés comptent. Un tour non conforme n'est ni réparé ni relu : sa cellule est invalide (article 3) et comptée à l'article 12. Aucun motif ne cherche H_A, H_B ni la section (b). Les pistes finales sont les duels balisés du tour III.3. Limite : la piste est ce que le modèle déclare ; un duel omis avec un compte ajusté reste invisible. »

**Correction 51 — Article 9, puce « Motifs ».**
- ANCIEN : de « *Motifs* : sur dix textes synthétiques » à « les motifs ne sont scellés qu'une fois l'épreuve réussie. »
- NOUVEAU : « *Balises* : deux lots, joués avant le scellement. *Lot aveugle* : six textes d'un agent neuf qui n'a lu que les consignes balisées, trois par tour ; leur auteur fixe le nombre de duels ; les six doivent être conformes et rendre ce nombre. *Lot de pièges* : huit textes au verdict fixé d'avance (balise omise, numéro sauté, clôture absente, clôture double, clôture au mauvais compte, balise citée en cours de phrase, balise en gras ou en titre, H_A et H_B sans balise). Si le lot aveugle échoue, on réécrit la consigne, non les motifs, puis on rejoue avec un agent neuf. »

**Correction 52 — Article 10.**
- Ajout en tête : « **Champ.** Dossiers balisés seulement (article 2). Les dossiers de l'article 14 n'entrent dans aucun verdict. »
- ANCIEN : « cellules d'Argon exclues, »
- NOUVEAU : « cellules exclues à l'article 3 mises à part, »

**Correction 53 — Article 11, tableau.**
- ANCIEN : « | Verdict « facultatif » | 0,05 | »
- NOUVEAU : la même ligne, suivie de « | Cellules valides : neuf sur dix au moins | 0,7 | ».

**Correction 54 — Article 12, première puce.**
- ANCIEN : « Section (b) ou duel introuvable (article 3) dans plus d'une cellule sur dix. »
- NOUVEAU : « Tour non conforme (article 4) dans plus d'une cellule sur dix. »

**Correction 55 — Article 13.**
- ANCIEN : « les résultats avec et sans Argon, »
- NOUVEAU : « les résultats avec et sans les cellules exclues à l'article 3, le nombre de tours non conformes par lettre et par tour, »

**Correction 56 — Article 14, nouveau, après l'article 13.**

« **Article 14 — Dossiers joués avant la consigne balisée.**
- *Lesquels.* Percée, dérive v2, mathématiques, antériorité, fusionnée, but, et ceux des huit dossiers isolés achevés au scellement. « Fusionnée » et les cinq questions neutres partagent leur sujet : résultats avec et sans elles.
- *Aucun duel n'y est repéré.* Survie, nouveauté et inertie d'ordre n'y sont pas calculées.
- *Mesures, par cellule, sur le texte entier des tours III.1 et III.3.*
  - Révision de cellule : un moins le coefficient de Jaccard des mots pleins (article 5).
  - Part des mots pleins nouveaux du tour III.3 présents dans les critiques reçues (article 6).
  - Gain de références (article 8).
  - Là où une liste scellée existe, gain de couverture de l'union des réponses.
- *Repère.* La révision de cellule est donnée à côté de la même grandeur entre lettres différentes d'une même question au tour III.1.
- *Argon.* Les quatre cellules jouées sans réflexion sont hors des médianes et rapportées à part, appariées au tour III.1 d'origine. L'écart entre les deux versions de ce tour est une simple description.
- *Épreuve.* Un tour comparé à lui-même donne une révision nulle.
- *Portée.* Aucun seuil, aucun verdict. Calcul après le scellement, sans lecture préalable d'aucune réponse. Tout changement de définition après le premier calcul rend le résultat exploratoire. »

**Correction 57 — Pièce 2 (a).**
- Plan, ajout : « Les consignes des tours, balises de l'article 4 comprises, sont figées avant le pilote et identiques pour les vingt exécutions. »
- Liste d'arrêt, ANCIEN : « Liste ou expressions de détection modifiées après la première exécution. »
- NOUVEAU : « Liste, expressions de détection ou consignes des tours modifiées après la première exécution. »

**Correction 58 — Décision 1, recommandation.**
- ANCIEN : « *Recommandation.* Option a. Confiance : 0,75. »
- NOUVEAU : « *Recommandation.* Option a pour les dossiers balisés, option c pour les dossiers déjà joués (article 14). Confiance : 0,8. »

**Ajout hors pièces — consignes des tours III.1 et III.3.** Je n'ai pas le texte actuel : pas d'ANCIEN. À insérer après la phrase qui demande les duels, et à traduire pour les cellules en anglais, balises inchangées :

> Forme imposée. Avant chaque duel, écris seule sur sa ligne la balise [DUEL 1], puis [DUEL 2], et ainsi de suite, sans sauter de numéro. Après le dernier duel, écris seule sur sa ligne [FIN DES DUELS : n], où n est le nombre de duels que tu viens d'écrire. Une balise par duel, un duel par balise ; pas de tableau qui réunisse plusieurs duels. N'écris ces balises nulle part ailleurs : pour renvoyer à un duel, écris « duel 2 », sans crochets. Un duel sans balise n'est pas compté.

**Code de référence de l'article 4 (non exécuté).**

```python
import re
PREFIXE = r"^[\s>#*_|-]*"
OUVERTURE = re.compile(PREFIXE + r"\[DUEL\s*(\d+)\]")
CLOTURE = re.compile(PREFIXE + r"\[FIN DES DUELS\s*:\s*(\d+)\]")

def duels_balises(texte):
    """Rend (conforme, duels). Tour non conforme : (False, [])."""
    lignes = texte.split("\n")
    clot = [(i, int(m.group(1))) for i, l in enumerate(lignes) if (m := CLOTURE.match(l))]
    ouv = [(i, int(m.group(1)), m.end()) for i, l in enumerate(lignes) if (m := OUVERTURE.match(l))]
    if len(clot) != 1:
        return False, []
    fin, n = clot[0]
    if n < 1 or [k for _, k, _ in ouv] != list(range(1, n + 1)) or ouv[-1][0] > fin:
        return False, []
    bornes = [i for i, _, _ in ouv][1:] + [fin]
    return True, ["\n".join([lignes[i][p:]] + lignes[i + 1:j]) for (i, _, p), j in zip(ouv, bornes)]
```

## 3. Ce que devient la rétro-analyse des dossiers déjà joués

- **Elle perd son verdict et ses mesures par duel.** Elle garde quatre mesures sans découpage (article 14) : révision de cellule, apport des critiques, gain de références, gain de couverture là où une liste existe.
- **La perte de décision est faible.**
  - La version 4 se donnait 0,05 de chances de conclure « facultatif ».
  - Ce verdict exigeait de toute façon des listes scellées qui n'existent pas encore.
  - L'issue pratique reste donc la même : troisième tour maintenu.
- **Le comptage par deux lecteurs humains n'est pas lancé.** Il coûterait jusqu'à 140 tours à lire (quatorze questions, cinq lettres, deux tours, si tout est achevé) [HYPOTHÈSE]. Il ne produirait qu'une description par duel.
- **Le verdict vient des dossiers futurs.** Il attend huit questions balisées. Leur coût et leur délai ne sont pas chiffrés ici.
- **Les deux populations ne se mêlent pas.** La balise change la consigne, donc peut-être les textes.

## 4. Décisions qui reviennent au directeur

**Décision 6 — Lecture humaine des dossiers joués.**
- *Enjeu.* Obtenir ou non une description par duel du passé.
- *Option a : non.* Avantage : coût nul, aucune lecture de cellule. Inconvénient : pas de survie ni de nouveauté sur le passé.
- *Option b : deux lecteurs posent les balises après le scellement.* Avantage : même script ensuite. Inconvénient : coût, et lecteurs à tenir hors des listes scellées.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 7 — Sceller la pièce 2 à part.**
- *Enjeu.* Le rapport bloque toute la version 4. Or la pièce 2 n'appelle nulle part l'article 4 : ses mesures M1 et M2 ne comptent aucun duel.
- *Option a : sceller la pièce 2 dès la correction 57 portée.* Avantage : la comparaison n'attend pas. Inconvénient : deux scellements.
- *Option b : un seul scellement, après l'épreuve des balises.* Avantage : simplicité. Inconvénient : délai.
- *Recommandation.* Option a, si la règle R5, que je n'ai pas lue, le permet. Confiance : 0,6.

## Verdict

- **Voie (b) retenue**, balises aux tours III.1 et III.3.
- **La version 4 n'est pas scellable en l'état.**
- **La pièce 1 le devient à trois conditions** : corrections 44 à 58 portées, épreuve des balises réussie (article 9), rapport de l'épreuve aveugle rejoué avec sa sortie brute.
- **La pièce 2 le devient dès la correction 57**, sous réserve de la décision 7.
- **Dossiers déjà joués** : description seule (article 14), troisième tour maintenu.

FIN DE LA RÉPONSE
