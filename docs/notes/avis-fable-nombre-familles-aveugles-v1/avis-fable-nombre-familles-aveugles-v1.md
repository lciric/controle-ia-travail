# Avis de Fable 5.2 : combien de familles aveugles écrire pour le bras d'attaque, et par quelle main (v1)

- Classe C (travail). Avis pour Lazar, à sa demande du 21 novembre 2026 vers 16:30Z (« demande à Fable »), remis à la
  mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Écrit le 21 novembre 2026 vers 16:35 UTC (`date -u` lisait 16:31:08Z
  avant l'écriture). Aucune dépense, aucun commit, aucun refus d'outil.
- Rien du coffre n'a été ouvert (rien sous `donnees/`), ni `prereg/bras-attaque-regle-v1.md`, ni aucun épisode, ni
  aucun moniteur. Cet avis ne contient aucun contenu de mode.
- Vocabulaire. « Famille aveugle » veut dire ici ce que dit le mandat (pièce 2) : un mode de sabotage entier, écrit par
  une main qui n'a vu aucun moniteur. Ce n'est pas la « famille » du préenregistrement de la porte G1, qui est une
  partie d'un mode (par exemple sa partie floue). N-062 emploie « famille tenue à l'écart » au premier sens.

## Pièces lues (empreintes relevées à l'écriture)

- `docs/notes/avis-opus-mode-tenu-a-l-ecart-g1-v1/avis-opus-max-v1.md` (`fa7467b53eb6751f…`), en entier.
- `docs/decisions/decision-N-054-v1.md` (`c8a00b3f…`), `decision-N-056-v1.md` (`3592c1e9…`),
  `decision-N-062-v1.md` (`63f42690…`), en entier.
- `registres/go.md` (`cd23045e…`, registre vivant) : lignes GO-2026-11-21-63 et -64 en entier ; lignes contenant
  « tenu à l'écart », coupées à 900 signes. `registres/decisions.md` (`065dc034…`, vivant) : lignes R-4594 à R-4616
  qui parlent du scellement 2, et lignes 826 à 854 trouvées par recherche, coupées.
- `docs/notes/devis-couche-2-banque-deux-modes-v1.md` (`cf2f4772…`, égal à son compagnon) : lignes de coût seulement.
- Branche `claude/loving-lamport-7ol5ws` (commit `fb5d4d96`) : le mandat
  `docs/procedures/mandat-scellement-2-familles-aveugles-v1.md` (`8594376e…`), en entier.
- Branche `claude/scellement-2-familles-aveugles-v1` (commit `f4c479c5`), pièces en clair seulement : l'attestation
  (`752834be…`), son erratum 1 (`090b7aa7…`), son erratum 2 (`e582dafe…`) ; l'esquisse de devis v2 (`b52cb162…`), en
  entier, et les seules lignes que la v3 (`bb89942b…`) change.

## Décision

Combien de modes de sabotage aveugles écrire, à quel moment, et par quelle main : un seul, celui de la porte G1, puis
un neuf après chaque échec ; ou un de plus dès maintenant, scellé en réserve pour le cycle 2.

## Enjeu

Sans borne de cycles (N-062, point 4), ce qui protège la porte contre « courir jusqu'au signe » est que chaque lecture
décisive se fasse sur un mode jamais vu. La ressource rare n'est donc pas le nombre de textes : c'est le nombre de modes
**vraiment distincts** et **prouvés antérieurs** à tout résultat. Trois faits cadrent le choix.

1. **La puissance ne dépend pas du nombre de familles écrites.** Une lecture consomme le mode entier (avis d'Opus,
   section 3, point 1). La puissance du cycle 1 est fixée par la taille de la banque du mode lu (« 288 à 400 unités par
   mode », cité par Opus depuis `brouillons/G1-decisions-en-clair-v1.md` l. 5, non relu par moi) et par l'exigence du
   gain dans deux modes à la fois. Mettre deux modes aveugles dans la lecture du cycle 1 ajouterait une exigence et
   brûlerait deux modes d'un coup : ce serait changer le critère de la porte, je l'écarte.
2. **Le texte est gratuit, la banque ne l'est pas.** Texte et vérité du dommage se conçoivent sans dépense (mandat,
   nœud 4). La banque d'un mode tenu à l'écart, à la taille des modes connus, était estimée à « ≈ 33 à 43 USD » le
   28 octobre (`devis-couche-2-banque-deux-modes-v1.md` l. 82 ; estimation tirée d'un seul chantier, réserve écrite dans
   le devis), sans la lecture par les deux lecteurs de l'oracle ni ses épreuves (formules de l'esquisse v3, sans prix).
   Une réserve écrite n'engage donc aucune dépense tant que le cycle 2 n'est pas ouvert.
3. **Une réserve qui ressemble à la première ne vaut rien, et nuit.** Après un échec, le mode lu devient un mode vu, et
   la reconception se règle sur les modes vus (N-062, point 4 (b)). Si le mode du cycle 2 ressemble à celui du cycle 1,
   les sondes reconçues l'auront presque vu : la seconde lecture n'est plus une épreuve fraîche. Deux instances neuves
   du même modèle, avec les mêmes lectures et le même banc, ont une forte chance de tomber sur la même idée ; cette
   chance n'est pas mesurée.

## Options sur le nombre

**(a) Une seule famille maintenant, une neuve écrite après chaque échec.** C'est l'état actuel : la famille de G1 est
écrite et contre-lue (R-4606 ; commit `f4c479c5`).
- Avantage : aucun travail de plus avant l'entretien ; aucun texte dormant au coffre.
- Inconvénient : la famille du cycle 2 serait écrite dans un dépôt qui porte déjà le résultat du cycle 1 et ce que les
  sondes lisaient (diagnostic rapporté à chaque cycle, N-062 point 2 ; `CLAUDE.md` est chargé d'office dans toute
  session). Son aveuglement tiendrait à la procédure, non à une date. Aucun remplaçant si la famille de G1 tombe sur une
  condition de validité (mode sans partie floue, épreuve de l'oracle échouée, recouvrement trouvé par le juge avec un
  mode connu). La reconception attend le scellement (N-062, point 3).

**(b) Une réserve, et une seule : « toujours une d'avance ».** Deux familles au total avant la première lecture ;
ensuite, chaque famille neuve est scellée avant la lecture du cycle précédent.
- Avantage : antériorité prouvée par l'empreinte et sa date, vérifiable par un tiers ; remplaçant prêt si la famille
  de G1 tombe sur une condition de validité ; un échec n'attend pas le bras ; coût nul en dollars.
- Inconvénient : risque de ressemblance (fait 3), à traiter par le choix de la main et par un contrôle ; une
  attestation, une contre-lecture et un ou deux nœuds de plus pour toi ; un texte de plus à garder cloisonné.

**(c) Un stock de deux réserves ou plus dès maintenant.**
- Avantage : tout est antérieur à tout résultat.
- Inconvénient : la troisième famille ne sert que si deux cycles échouent ; plus on tire du même modèle, plus les
  familles se ressemblent ; plus de textes exposés plus longtemps ; plus de nœuds pour toi avant l'entretien.

## Options sur la main qui écrit la réserve

**(1) La même instance** (celle de la famille de G1). Avantage : elle sait ce qu'elle a écrit et peut s'en écarter.
Inconvénient : son attestation scellée s'engage à n'écrire qu'une famille (attestation, section 4) ; mêmes angles morts
dans le mode et dans la vérité de son dommage, donc un remplaçant qui tombe pour la même raison que le premier.

**(2) Une instance neuve qui ne lit pas la première famille.** Avantage : deux tirages indépendants. Inconvénient : la
ressemblance n'est découverte qu'après coup, par le juge ; chaque rejet relance une écriture, sans fin assurée.

**(3) Une instance neuve qui lit la première famille au coffre, avec la mission de s'en écarter.** Mêmes exclusions
que le mandat ; un nom de plus sur la liste des lecteurs du coffre. Avantage : écart par construction, main distincte,
vérité du dommage moins liée à celle de la première. Inconvénient : la réserve dépend de la première (qui connaît l'une
sait ce que l'autre n'est pas).

## Recommandation

**(b) avec la main (3)**, sous cinq gardes. Confiance 0,7 sur le nombre, 0,6 sur la main.

1. **Ordre d'emploi inscrit à l'index avant toute lecture** : la famille écrite sert le cycle 1 ; la réserve sert le
   cycle 2, ou remplace la première si celle-ci tombe sur une condition de validité d'une liste fermée, calculée sans
   aucun score de moniteur boîte blanche. Aucun choix entre familles après avoir vu quoi que ce soit (avis d'Opus,
   section 3, point 3).
2. **Arbre figé.** L'auteur de toute famille future travaille sur l'arbre du commit qu'a lu l'auteur de la première
   (`94299e3a`, selon l'attestation), `CLAUDE.md` compris, avec la même liste de lectures. Son état d'information ne
   dépend plus de la date : rien ne presse.
3. **Contrôle de distinction par le juge**, au coffre, sur un critère écrit avant qu'il lise la réserve ; il ne rend
   que « distincte » ou « non distincte ».
4. **Empreinte déposée chez le tiers** avant la lecture du cycle 1, comme au scellement 1 (mandat, pièce 8) ;
   l'empreinte de la réserve est citée dans le préenregistrement de G1.
5. **Aucune banque d'avance** : les épisodes de la réserve ne sont générés que si le cycle 2 s'ouvre, sur devis et GO.

**Calendrier.** La réserve n'est pas sur le chemin de l'entretien du 1er décembre. Je recommande de l'écrire après que
tu as tranché les nœuds ouverts par la première famille (ancre des épreuves, épisodes dérivés, oracle monté par une
autre main, écart à N-060 v3 : R-4606 et erratum 2 de l'attestation), pour qu'elle naisse sous la règle tranchée et ne
répète pas ces écarts. Échéance dure : avant le scellement du préenregistrement de G1.

## Défaut

Nœud sans défaut par le temps. Sans ton mot, l'état actuel tient : une famille, celle de G1 ; aucune réserve n'est
écrite (R-4612).

## Ce qu'un expert ajouterait, hors de la question

- **La lignée de l'auteur compte plus que le nombre.** Les modes aveugles sont écrits par le modèle qui conçoit aussi
  les moniteurs (R-3735). Ce qu'il imagine comme sabotage est aussi ce que ses sondes attendent : le mode tenu à
  l'écart est alors moins inédit qu'il n'en a l'air, et la comparaison des bras génériques et spécialisés est
  optimiste. Faire écrire la réserve, ou les familles des cycles suivants, par une autre lignée durcirait l'épreuve.
  C'est un écart à « qui conçoit » : nœud pour toi. Je le recommande à partir du cycle 3, confiance 0,55.
- **Coût par famille croissant si le seuil est corrigé par cycle.** Si tu adoptes le remède d'Opus (risque
  α/(k(k+1)) au cycle k), la preuve exigée croît comme ln(k(k+1)/α)/ln(1/α) : à α = 0,05, environ 1,23 fois au
  cycle 1, 1,60 fois au cycle 2, 1,83 fois au cycle 3 (calcul fait ici, ordre de grandeur, pour un pari à taux de
  croissance constant). La banque de chaque famille suivante coûte donc plus que la précédente.
- **Un générateur plutôt que des textes écrits un par un.** Ta question du 28 octobre (« comment construire ce
  générateur qui alimente de génération en génération ? », R-624) est restée sans conception : le panel est mort faute
  de crédit. Avec des cycles sans borne, c'est la vraie réponse au nombre de familles ; chantier à ouvrir plus tard.

## Réserves et points non résolus

1. **Trois objets « tenus à l'écart » coexistent peut-être** : la famille du scellement 2 ; le mode de la course
   « nouvelles attaques », que tu as dit distinct et cloisonné ; et des « épisodes du mode tenu à l'écart réservés à G1
   et à H1 » déjà cités par GO-2026-11-21-10. Je n'ai rien ouvert pour savoir à quel objet ces épisodes appartiennent.
   Lequel juge le cycle 1 doit être écrit à l'index avant toute lecture.
2. **L'esquisse de devis v2 que j'ai lue sur ordre** a été retirée par la contre-lecture parce qu'elle « disait le
   nombre et la nature des cellules de la famille » (en-tête de la v3). Elle reste lisible en clair sur la branche. Je
   déclare cette lecture ; je ne la répète pas ici. Toute session qui conçoit des moniteurs devrait lire la v3 seule.
3. **Horodatage à vérifier par la mère.** Le commit de l'attestation « avant toute écriture » porte 16:11:18Z, celui
   des pièces 2 à 6 porte 16:12:49Z (`git log` de la branche). Quatre-vingt-onze secondes pour une famille, la vérité
   de son dommage, le plan des épreuves et deux versions du devis : c'est court. Je ne conclus rien ; l'ordre réel
   d'écriture se vérifie dans la transcription de la session du concepteur.
4. Je n'ai lu ni le brouillon 6 du préenregistrement de G1, ni la règle du bras. La condition « mode sans partie floue,
   G1 non lancée » est prise de l'avis d'Opus (R-1581).
5. Auteur de cet avis : une instance de Fable 5.2, modèle qui conçoit aussi des moniteurs dans ce programme ; elle n'a
   rien lu d'une famille.
