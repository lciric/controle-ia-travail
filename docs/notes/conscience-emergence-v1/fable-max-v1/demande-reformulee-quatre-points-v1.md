# Demande reformulée en quatre points — éveil, allumage, anesthésie et transition de phase dans les modèles de langage, avec l'addendum « signature mathématique de la conscience » (v1)

- 23 novembre 2026. Claude Fable 5.2, effort maximal, session fille de la session des collisionneurs. Classe A. Mandat `mandat-fable-max-reformulation-et-motifs-v1.md` (`4177b0c5…`), additif 1 (`d9659a67…`), additif 2 (`59164108…`).
- Marques : **FAIT RAPPORTÉ** (clé de la source et rang de la page dans le fichier, entre crochets), **HYPOTHÈSE**, **PROPOSITION**. Sans page : rapporté de mémoire, non vérifié sur PDF.
- Pages de [G], [DN], [RA], [OS] relevées par moi sur les textes extraits de `docs/notes/protocole-x-conscience-anesthesie-v1/travail/textes-extraits/` (rang de page compté par les sauts de page). Pages de [CO] et [NO] reprises de la réponse précédente de Fable (`reponse-fable-conscience-anesthesie-v1.md`), où un programme les avait contrôlées ; non relues ici.
- Clés (empreintes et adresses dans `docs/notes/protocole-x-conscience-anesthesie-v1/sources/provenance-v1.md`) : [G] Gurnee, Sofroniew et al., « Verbalizable Representations Form a Global Workspace in Language Models », arXiv 2607.15495 ; [DN] Dehaene et Naccache, « Does Claude possess a conscious global workspace? », commentaire du 7 juillet 2026 ; [RA] Rahbar, « The Ignition Index », arXiv 2608.05160 ; [OS] Ostrow, Qian, Liu et Fiete, « A Mathematical Theory of the Jacobian Lens », arXiv 2610.31955 ; [CO] Colombo et al. 2019 ; [NO] Nourski et al. 2021 ; [PA] Tagliabue, Dung et Berg, « The Pain Axis », arXiv 2609.16247 v2 (`docs/sources/pdf/2609.16247v2.pdf`, `fa4b2bb4…`).

## La demande, prise comme un tout

Tu demandes quels motifs, quels signaux et quels outils mathématiques chercher dans un modèle de langage pour y pister l'éveil, l'allumage, l'anesthésie et la transition de phase ; quelles expériences des neurosciences de la conscience s'y transposent ; et, en addendum, quelle signature mathématique de la conscience chercher. Les quatre points ci-dessous disent ce qui manque à cette demande pour qu'une réponse soit profonde plutôt que longue.

## 1. Ce qu'un expert ferait, et que tu ne demandes pas

**Il partirait de ce qui est déjà fait dans les pièces mêmes.**
- FAIT RAPPORTÉ. « Ne pense pas à X », lu dans l'espace de travail du modèle, est fait : la consigne d'ignorer un concept l'y laisse à un taux non nul, que les auteurs rapprochent de l'effet « ours blanc » ; la consigne « surtout, ne pense pas à X » le laisse au taux d'une simple mention ; quand la suppression échoue, l'espace de travail du modèle post-entraîné porte des mots d'échec [G p. 14-15, 46-47, 78-79].
- FAIT RAPPORTÉ. « Penser à quelque chose pendant une autre tâche » est fait (tenir un concept ou un calcul en tête en recopiant une phrase) [G p. 13-14]. Le flux de pensée d'un modèle à qui l'on demande seulement de se parler à lui-même est nommé comme analogue partiel du vagabondage de l'esprit, et la suppression de l'espace de travail le perturbe [DN p. 9 ; G p. 27-28].
- FAIT RAPPORTÉ. La netteté de l'allumage est mesurée couche par couche (largeur de la bascule entre deux concepts quand on mélange leurs plongements d'entrée), et la bimodalité est montrée entre invites, non entre essais d'un même stimulus [G p. 31-32, 83-84]. Deux auteurs de la théorie écrivent que l'allumage « reste à démontrer pleinement » et décrivent l'expérience décisive [DN p. 7]. Un indice d'embrasement existe, avec une rupture au cours de l'entraînement [RA p. 1-2].
- PROPOSITION. La question se déplace donc : non « le motif existe-t-il », mais ce que ces pièces laissent ouvert. Une activité de fond sans consigne ; l'allumage sous dose ; ce que le modèle rapporte après une fenêtre de suppression ; ce qui persiste hors de l'espace de travail quand il est supprimé.

**Il séparerait trois choses que « transition de phase » confond.**
- PROPOSITION. (i) Une non-linéarité raide : des saturations composées couche après couche durcissent toute réponse, sans rien de collectif. (ii) Une bifurcation : un changement qualitatif d'une dynamique de petite dimension quand un paramètre passe un seuil. (iii) Une transition de phase au sens de la physique statistique : un phénomène collectif, qui n'est net qu'à la limite d'un grand nombre d'unités et se prouve par la façon dont la netteté change avec la taille. Chacune a sa valeur nulle ; seule la troisième répond au mot « émergent ».
- FAIT RAPPORTÉ. Un modèle a deux axes de temps : la profondeur, de longueur fixe et sans boucle ; la suite des jetons, où la sortie réinjectée fait une vraie boucle, à débit étroit [G p. 56-57]. PROPOSITION. Toute grandeur dynamique dit sur quel axe elle vit ; hystérésis, activité entretenue et temps de retour n'ont de sens non trivial que sur le second.

**Il séparerait conscience, connexion et réactivité.**
- FAIT RAPPORTÉ. Sous kétamine, des sujets qui ne répondent plus rapportent au réveil une expérience ; sous propofol ou xénon, aucune [CO p. 1]. Sous propofol, la réponse à une nouveauté locale persiste quand la réponse à une nouveauté globale a disparu [NO p. 3, 14].
- PROPOSITION. Chaque motif cherché dit lequel des trois il vise : un espace de travail vide (inconscience), un espace de travail actif mais découplé de l'entrée (déconnexion, rêve), un contenu présent mais non rappelé ensuite (amnésie). Ce sont trois interventions et trois lectures différentes.

**Il exigerait des dissociations qui violent l'ordre de fragilité.**
- PROPOSITION. Le dossier précédent a établi qu'une dégradation à un seul facteur imite « local épargné, global supprimé » dès que les tâches globales demandent plus d'étapes. Un motif plus profond est donc un motif que ce nul ne prédit pas : une fonction coûteuse qui tient quand une fonction simple tombe, un ordre de retour qui diffère de l'ordre de perte, une grandeur qui change de signe et non de taille.

**Il écrirait les nuls avant les motifs.**
- PROPOSITION. Aux quatre nuls du dossier précédent (composition de la profondeur de calcul ; lésion triviale de longue portée ; biais de sélection des directions ; réseaux sans fonction ou brouillés) s'en ajoutent trois. Le nul d'architecture : connexions résiduelles et normalisations tiennent toute jacobienne près de l'identité, si bien que « proche du point critique » est acquis par construction. Le nul du texte : un récit, une consigne ou un mot suffit à poser un contenu, et le modèle a lu des récits d'anesthésie et de rêve. Le nul de la lecture : la lentille lit le réseau même qu'on manipule.

**Il traiterait « il y a forcément une signature mathématique » comme une hypothèse.**
- PROPOSITION. Il dirait d'abord ce qu'une signature doit être pour mériter ce nom : invariante (au rangement des neurones, au changement de coordonnées, à la taille du modèle), discriminante (un réseau sans fonction ne la porte pas, une dégradation quelconque ne l'efface pas comme la lésion visée), ancrée (elle suit le rapport du sujet là où un rapport existe, c'est-à-dire chez l'humain). Puis il dirait ce qui réfuterait l'hypothèse : toute grandeur candidate échoue à l'un des trois, ou les grandeurs qui passent dans le cerveau ne se calculent pas dans un réseau.

**Il chercherait un objet commun aux deux systèmes.**
- FAIT RAPPORTÉ. La lentille jacobienne retient les directions qui agissent comme des modes de Lyapunov dominants et cohérents (amplifiés en profondeur, stables d'une position à l'autre et d'un contexte à l'autre), et ses auteurs de théorie écrivent qu'une famille de telles lentilles pourrait s'appliquer à des données neuronales, les jacobiennes y étant estimées à partir de la dynamique [OS p. 1, 4, 13].
- PROPOSITION. Une même statistique, calculée exactement dans le modèle et estimée dans le cerveau sous dose d'anesthésique, vaut mieux que deux analogies.

## 2. Les données brutes qu'il prendrait

PROPOSITION (renvois : faits rapportés).
- **Dans le modèle** : les jacobiennes couche à couche et position à position, passe par passe, non la seule jacobienne moyenne (une moyenne de jacobiennes peut ne ressembler à aucune d'elles [OS p. 2]) ; le flux résiduel entier sous intervention graduée, avec le jumeau exact de chaque passe ; des trajectoires de génération libre dont les tirages sont consignés, pour rejouer deux copies sous le même hasard ; les points de contrôle publics de l'entraînement et une famille de tailles, pour toute question d'émergence et d'échelle.
- **Dans le cerveau** : des enregistrements bruts et publics sous anesthésique à plusieurs paliers, avec retour ; le jeu ouvert ds003171 existe (dix-sept adultes, récit et repos, quatre niveaux de sédation) ; l'existence d'électroencéphalogrammes bruts du paradigme local-global sous un même anesthésique reste à établir (point d'Astra, inscrit à la passation).
- **Dans l'antériorité** : les tableaux et les annexes des pièces, relus, non leurs résumés.

## 3. Ses méthodes et outils

PROPOSITION.
- **Dynamique** : spectre de Lyapunov à temps fini par produit de jacobiennes, vecteurs covariants, propagation d'un dommage entre deux copies sous hasard commun, temps de retour après perturbation.
- **Physique statistique** : paramètre d'ordre et susceptibilité, cumulant de Binder et mise à l'échelle en taille finie, exposants comparés à ceux du champ moyen (qui sont la valeur attendue de toute bifurcation lisse, donc le nul).
- **Bifurcations** : les drapeaux d'une catastrophe (bimodalité, sauts, hystérésis, zone inaccessible, variance anormale, ralentissement critique), relevés ensemble.
- **Information** : décomposition en synergie et redondance, fermeture informationnelle d'une variable macroscopique, production d'entropie, métrique de Fisher tirée de la sortie, qui donne à toute perturbation une taille en nats, indépendante des coordonnées.
- **États** : modèles de Markov cachés, loi des temps de séjour, répertoire des configurations visitées.
- **Méthode du programme** : jumeau exact, nuls écrits d'avance, lésion plantée par un tiers, porte de jugeabilité, unité statistique égale au réseau entraîné indépendamment, règle à verrous et issue « non jugeable ».

## 4. Ce qui, hors de toi et de Claude, vérifierait le résultat

PROPOSITION, par force décroissante.
1. La même statistique, calculée par d'autres sur des données humaines recueillies par d'autres, à dose croissante d'anesthésique, avec une prévision scellée de son sens.
2. Une prévision écrite d'avance par les tenants du doute publié [DN p. 8-9, 11] : l'issue qui les ferait changer d'avis, et celle qui nous ferait changer d'avis.
3. Une réplique par un tiers sur une autre famille de modèles, avec une seconde définition de l'espace de travail.
4. Les réfutateurs intégrés : réseaux sans fonction, dégradation quelconque de même ampleur, prédicteur sur le texte seul. Une grandeur qui ne les passe pas se réfute sans juge.
5. Une lésion plantée par un tiers dans des copies anonymes, que toute la chaîne doit retrouver à l'aveugle.

## Demande reformulée

**Objet.** Des travaux publiés en 2026 rapportent, dans de grands modèles de langage, un petit ensemble de directions lisibles en mots (l'« espace J », isolé par la lentille jacobienne) qui se comporte comme un espace de travail global : sa suppression épargne la lecture, la classification et l'extraction et dégrade le raisonnement à plusieurs sauts, la traduction et le résumé ; à son entrée, vers le tiers de la profondeur, une entrée ambiguë bascule nettement vers l'une de ses lectures [G]. Deux auteurs de la théorie de l'espace de travail neuronal jugent l'allumage non encore démontré, notent l'absence d'activité autonome, et doutent que supprimer cet espace donne un analogue de la perte de conscience, faute de mécanismes d'éveil [DN]. Une théorie montre que la lentille retient des modes de Lyapunov cohérents [OS]. Établir quels motifs, propres à l'éveil et à l'anesthésie et plus spécifiques que le contraste « local épargné, global supprimé », peuvent être cherchés dans un modèle de langage ; avec quels outils mathématiques ; et quelles expériences des neurosciences de la conscience s'y transposent sans se vider. L'issue négative est recevable : « ce motif ne se transpose pas », ou « cet outil ne distingue rien », avec la mesure qui l'établit.

**Exigences.**

1. **Partir de l'occupé.** Dire, pour chaque idée, ce que les pièces nommées ont déjà fait (suppression de pensée lue dans l'espace J, concept tenu en tête, flux de pensée sous suppression, netteté de la bascule par couche, indice d'embrasement [RA]) et ce qu'elles laissent ouvert. N'écrire ni « inédit » ni « premier ».
2. **Dire quel sens de « transition » est visé** : non-linéarité raide, bifurcation, ou transition collective ; sur quel axe (profondeur, suite des jetons, entraînement, taille du modèle) ; quel est le paramètre de contrôle, quel est le paramètre d'ordre, et quelle observation séparerait les trois sens.
3. **Dire lequel des trois états est visé** : espace de travail vide, espace de travail découplé de l'entrée, contenu présent mais non rappelé ; et par quelle intervention on produirait chacun.
4. **Pour chaque motif** : grandeur, unité, valeur nulle ; ce qui le réfuterait ; première expérience sur un petit modèle ouvert et ce qu'elle tranche ; antériorité, en séparant ce qui a été lu de ce dont on se souvient.
5. **Écarter les sept explications ordinaires** : composition de la profondeur de calcul ; lésion triviale de longue portée ; biais de sélection des directions ; réseaux sans fonction ou brouillés ; architecture qui impose déjà la grandeur ; texte seul ; lecture non indépendante du réseau manipulé. Préférer les motifs qu'un seul facteur de fragilité ne prédit pas.
6. **Instruire les six transpositions proposées**, en disant pour chacune si elle tient, sous quelle forme, ou pourquoi elle se vide : (a) une activité de fond, et un analogue du réseau du mode par défaut ; (b) la suppression de pensée ; (c) le récit au réveil après une fenêtre de suppression, lu par une lentille ; (d) le traitement d'un signal nocif (la direction de la douleur de [PA]) qui continuerait sous suppression de l'espace de travail ; (e) la netteté de l'allumage comme paramètre d'ordre, avec un point critique selon la dose ; (f) l'ordre de perte des fonctions avec la dose. En proposer d'autres.
7. **Chercher un objet commun** : une grandeur calculable exactement dans le modèle et estimable sur des enregistrements humains ou animaux sous anesthésie, et dire quelles données brutes publiques la permettraient.
8. **Dire ce qui, hors des auteurs, vérifierait chaque résultat**, et ce que chaque issue apprend et n'apprend pas sur la conscience d'un système artificiel. Aucune issue ne conclut qu'un modèle est conscient ou ne l'est pas.

**Addendum — signature mathématique de la conscience.** Hypothèse de travail, non fait établi : il existe une grandeur mathématique (invariant, exposant, structure) qui distingue un système conscient d'un système qui ne l'est pas. La servir comme telle :

9. **Dire ce qu'une grandeur doit satisfaire pour être appelée signature** : invariance (rangement des neurones, coordonnées, taille), pouvoir de discrimination (réseaux sans fonction, dégradation quelconque, complexité de l'entrée, profondeur de calcul), ancrage sur un cas où le rapport du sujet existe.
10. **Proposer des grandeurs candidates**, chacune avec sa valeur dans un système sans fonction, ce qui la distinguerait d'un artefact de la profondeur de calcul ou de la complexité de l'entrée, et le calcul qui la donne.
11. **Dire ce qui montrerait qu'il n'y en a pas** : quel ensemble de résultats conduirait à abandonner l'hypothèse, pour une classe de grandeurs ou en général ; et ce que les théories qui lient la conscience au substrat répondraient à toute grandeur calculée sur des activations.
