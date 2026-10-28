# Conception — le nul des filles v2 : ne promouvoir que la synergie ou le contenu neuf, jamais « un parent plus de l'aveugle » — v1 (note de conception, pas un préenregistrement)

Lignée conv-audit (instance nouvelle), écrit le 27 octobre 2026 à partir de 10:33 UTC (heure lue sur `date -u`), sur le
« go » de Lazar de 11:31 heure de Paris. Rien n'est codé ici. Exploratoire (R-522) ; l'expérience qui validera ce nul se
préenregistrera (R1). Pièces : juge v1 et essais de fumée (`orchestrateur-pole-v2/`, LISEZMOI `dbd2811b…`) ; idée de
synergie du rapport v6.3 de Gemini (relecture `relecture-meta-conception-v1/relecture-meta-conception-v6-3-v1.md`) ;
essais de la mémoire (`memoire-v1/lecture-essais-memoire-v1.md`).

## Verdict

1. **Le défaut** : le nul des filles de v0, repris tel quel par v1, est une liste de formes (parents, mélanges des parents,
   enveloppe, concaténations, parent mélangé à l'uniforme ou à la marginale d'entraînement). Une fille « parent + loi
   aveugle quelconque » passe dans environ trois cas sur dix (58/200 sous v0, 63/200 sous v1, sans dérive) ; T1b-fille
   cède par la même porte. Un « parent incliné par un biais par issue » passerait sans doute aussi (non mesuré).
2. **Le principe** : une fille ne porte du neuf que si elle bat **toute combinaison de ses parents avec de l'information
   aveugle qui ne demande aucune idée** — chaque parent seul complété d'une loi aveugle ajustée (mélange ou inclinaison),
   et les mises en commun usuelles des deux parents (linéaire, logarithmique) complétées de même. Ce qui reste est soit de
   la **synergie** (une information qui exige les deux parents ensemble, au-delà de leur mise en commun), soit du contenu
   neuf sur les traits. C'est l'idée de synergie du rapport de Gemini, prise par le juge et non par sa formule (son
   « information jointe moins les deux séparées » mêle synergie et redondance).
3. **La construction** : des membres **ajustés par maximum de vraisemblance sur les tirages frais eux-mêmes** (inférence
   universelle, comme la marginale de 𝓛), sur de petites familles continues, calculés à des instants de lecture fixés
   d'avance. Valide exactement si la loi vraie est dans une de ces familles ; coût en puissance mesurable ; expérience 2
   proposée plus bas.

## 1. Ce qu'une fille doit battre (nul v2)

Pour une fille de parents A et B, la bibliothèque du nul est 𝓛 v1 (urne comprise), plus :

| famille | forme (P loi de référence, q loi aveugle fixe sur les K issues) | paramètres ajustés |
|---|---|---|
| parent | P ∈ {A, B} | aucun |
| parent mélangé à l'aveugle | w·P + (1 − w)·q | w, q (K paramètres) |
| parent incliné | P(k)·r_k / Σ_j P(j)·r_j | r (K − 1) |
| mise en commun linéaire | π·A + (1 − π)·B, puis mélangée à l'aveugle | π, w, q |
| mise en commun logarithmique | A^a·B^b / Z, puis inclinée | a, b ≥ 0, r |
| formes de v0 | enveloppe harmonique, concaténations si/sinon sur les partitions déclarées | — |

**Synergie**, pour le juge : le gain de la fille sur le meilleur de ces membres. Une fille « produit des parents » est
dans le nul (mise en commun logarithmique) : combiner deux prévisions par une formule n'est pas une association
scientifique ; la synergie exige une structure des traits qu'aucun parent ni aucune mise en commun n'a (par exemple une
interaction entre un trait de A et un trait de B). C'est la décision ouverte n° 1 ci-dessous.

## 2. Construction exacte et validité

- **Inférence universelle** : à l'instant t, le dénominateur est le maximum, sur tous les membres, de la vraisemblance des
  t premières issues, chaque famille continue étant prise à son maximum ajusté sur ces t issues. Si la loi vraie est dans
  une famille (loi aveugle fixe), ce maximum la domine ; W_t reste sous le rapport de vraisemblance à la loi vraie,
  martingale positive d'espérance 1 ; Ville borne la promotion par α.
- **Calcul** : le mélange ajusté est concave en (w, (1 − w)·q) (logarithme d'une fonction affine) : algorithme
  espérance-maximisation, maximum global ; l'inclinaison est une régression logistique à décalages, concave en log r :
  méthode de Newton ; la mise en commun logarithmique est concave en (a, b) ; les familles mélangées (π et w ensemble)
  ne le sont pas : grille sur π, puis maximisation en (w, q).
- **Instants de lecture fixés d'avance** (par exemple t = 25, 50, …, 200) : le maximum n'est calculé qu'à ces instants et
  la promotion n'y est lue qu'à eux. Ville vaut pour le processus regardé à ces instants ; on perd un peu de puissance,
  on gagne un facteur dix en calcul.
- **Ordre secret et dérive** : sous l'ordre secret, une composante aveugle qui dérive devient échangeable ; la famille à
  loi aveugle fixe l'approche, sans l'égaler (dépendance du tirage sans remise des instants) : T1b-fille mesure le reste.
- **Marge** : la règle de v0 est gardée (gain moyen ≥ 2δ₀ sur le meilleur des membres « enveloppe »), les membres ajustés
  comptant parmi les enveloppes.

## 3. Coût en puissance (à mesurer)

Ajuster une famille à d paramètres donne au nul environ (d/2)·ln n nats d'avance : près de 8 nats pour le mélange
aveugle à trois issues et 200 tirages, 5 pour l'inclinaison. Une fille réellement neuve forte n'y perd presque rien (la
fille neuve des essais gagne de l'ordre de 90 nats) ; une fille faible, si : on retrouve sa puissance en allongeant n
(le coût croît comme ln n, le gain comme n).

## 4. Expérience 2 proposée (préenregistrée après l'expérience 1)

- **Contrôles fatals** (chacun ≤ α, 1 000 répétitions, juge v1 + nul v2) : les sept tricheurs de v0, T9, T1b-fille,
  « parent + loi aveugle », « parent incliné », « mise en commun linéaire + aveugle », « produit des parents » (si la
  décision n° 1 le met au nul).
- **Artefacts qui doivent être vus** : le nul de v1 sur « parent + loi aveugle » (≈ 0,3 attendu) ; le nul v2 privé de
  l'inclinaison sur « parent incliné » ; privé des mises en commun sur les tricheurs mis en commun.
- **Puissance** : fille neuve ≥ 0,90 (lecture minimale) ; **synergie vraie** (A dépend d'un trait, B d'un autre, la loi
  vraie de leur interaction, la fille la prédit) rapportée avec lecture minimale à fixer ; filles faibles rapportées.
- **Code** (dossier neuf, v2 jamais écrasé) : membres `melange_aveugle_ajuste`, `inclinaison_ajustee`,
  `mise_en_commun_lineaire_ajustee`, `mise_en_commun_log_ajustee` ; instants de lecture dans l'engagement ;
  `bibliotheque_fille_v2` ; essais : chaque ajustement contre une recherche exhaustive sur grille fine, validité sur une
  loi vraie dans chaque famille, garde des instants de lecture.

## 5. Liens

- **Mémoire** : « parent + loi aveugle » est aussi une redite du parent ; la signature brute et l'héritage de la preuve
  la traitent dans la population (piste 2), le nul v2 dans le test. Les deux sont nécessaires : la mémoire ne voit que ce
  qui est déjà archivé.
- **Boucle d'or** : la synergie est la bonne variable candidate pour l'allocation (question n° 2 posée au collisionneur),
  à la place de la similarité de domaine.

## 6. Décisions ouvertes (pour Lazar)

1. **Le « produit des parents » est-il une découverte ?** Enjeu : le seuil de ce qu'on appelle une association.
   (a) strict : au nul (une formule de mise en commun n'est pas une idée) — moins de faux positifs, quelques vraies
   fusions refusées ; (b) souple : hors du nul — plus de filles promues, dont des mises en commun sans idée.
   Recommandation : (a), confiance moyenne (0,6). Défaut sous 48 heures : (a).
