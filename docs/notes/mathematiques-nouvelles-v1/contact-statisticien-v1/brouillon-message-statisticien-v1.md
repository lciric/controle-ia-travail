**À envoyer par Lazar ; non envoyé.**

# Brouillon du message à un statisticien des Mines de Paris — v1

- **Nature** : pièce de travail, non contre-lue. Brouillon de contact externe : rien n'est envoyé par une session ; Lazar relit, corrige, nomme le destinataire et envoie lui-même (décision du 21 novembre 2026, GO-2026-11-21-38, option « contact dès maintenant sur la liste de cibles »).
- **À régler par Lazar avant l'envoi** : le nom et la formule d'appel ; le « vous » ou le « tu » ; ce qui est entre crochets ; la signature. Le message et son annexe ne portent aucun résultat, aucun chiffre interne, aucun nom d'outil.

---

## Le message

**Objet :** Quatre questions de statistique venues du contrôle des systèmes d'IA — une heure de votre regard ?

Bonjour [Prénom Nom],

[Une ligne sur la façon dont Lazar a eu son nom.] Je me permets de vous écrire pour vous demander un avis de statisticien, court et sans engagement.

Je dirige un programme de recherche défensif sur le contrôle des systèmes d'IA : comment s'assurer qu'un système qui exécute de longues tâches ne s'écarte pas discrètement de ce qu'on lui demande. Nous y surveillons le système par plusieurs détecteurs imparfaits, dont il faut combiner les signaux et régler les alertes au fil du temps, avec un budget limité de vérifications humaines. La particularité est que celui qu'on surveille peut s'adapter à la surveillance, de sorte que les hypothèses commodes (indépendance des détecteurs, comportement normal stable) ne peuvent pas être tenues pour acquises.

Cela nous a conduits à quatre questions qui me semblent relever de votre domaine bien plus que du mien : la fusion de tests sous dépendance, les tests séquentiels quand l'hypothèse nulle n'est pas stationnaire, les frontières de détection pour des signaux rares et faibles, et les jeux d'inspection sous budget. Je les joins en annexe, une phrase chacune.

**Ce que je vous demande.** Pour chacune des quatre, me dire en quelques lignes : ce qui est déjà connu, et où le lire ; si l'énoncé est bien posé ou naïf ; et ce qui, à votre sens, serait à la fois neuf et utile — ou, à l'inverse, sans intérêt. Une réponse du type « c'est réglé depuis longtemps, voyez tel article » m'est aussi précieuse qu'une autre : je préfère l'apprendre maintenant qu'après des mois de travail.

**Ce que je ne vous demande pas.** Ni de démontrer quoi que ce soit, ni de relire un manuscrit ou du code, ni de vous prononcer sur l'IA, ni de cautionner le programme. Il n'y a rien de confidentiel dans l'annexe, et aucune suite n'est attendue si le sujet ne vous intéresse pas.

**Le temps.** Je l'estime à une heure : une demi-heure de lecture de l'annexe, et une demi-heure d'échange, par écrit ou de vive voix, comme vous préférez. Si une seule des quatre questions vous parle, une réponse sur celle-là me suffit.

**Ce que vous pourriez y trouver.** Des questions concrètes, venues d'un usage réel, où la dépendance et la dérive sont choisies par un adversaire plutôt que subies : il y a peut-être là des problèmes propres à poser, [pour vous ou pour un étudiant]. Si vos remarques orientent le travail, elles seront créditées comme vous le souhaiterez [remerciement, ou collaboration si le sujet vous retient]. Et je vous dirai, dans tous les cas, ce que nous en aurons fait.

Je précise, par honnêteté, qu'une partie de notre exploration mathématique est menée avec des outils automatiques : c'est justement pourquoi le jugement d'une personne du domaine, sur ce qui est connu et sur ce qui vaut la peine, nous manque et ne se remplace pas.

Merci d'avance du temps que vous voudrez bien y consacrer, et bien cordialement,

Lazar [Nom]
[fonction, coordonnées]

---

## Annexe — La liste courte de cibles, telle qu'elle serait jointe

*Cadre commun.* Un système exécute une suite d'épisodes ; à chaque épisode, plusieurs détecteurs rendent chacun un score. L'hypothèse nulle est « le système se comporte honnêtement ». On veut une garantie sur les fausses alertes et la meilleure puissance possible, face à un comportement déviant qui peut être rare, faible, et choisi en connaissance des détecteurs.

1. **Fusion de tests sous dépendance.** Étant donné quelques détecteurs dont chacun fournit une statistique valide sous l'hypothèse nulle (une valeur p, ou une valeur e), quelle règle de combinaison garantit le niveau et maximise la puissance quand leur dépendance est quelconque, ou seulement bornée par une contrainte explicite, et qu'elle peut être choisie par un adversaire — et que sait-on du cas fini, à deux, trois ou quatre détecteurs, où le pire cas se calcule exactement ?

2. **Tests séquentiels à hypothèse nulle non stationnaire.** Existe-t-il un test, ou un détecteur de rupture, dont la garantie de fausse alerte reste valable à tout instant d'arrêt lorsque la loi du comportement honnête dérive lentement à l'intérieur d'une classe bornée, et quel est alors le plus petit délai de détection atteignable pour une déviation donnée ?

3. **Frontières de détection.** Quand la déviation ne touche qu'une petite fraction des épisodes et y reste faible, et qu'on l'observe à travers plusieurs détecteurs dépendants, où passe la frontière entre ce qui est détectable et ce qui ne l'est par aucun test, et quelle statistique l'atteint ?

4. **Jeux d'inspection sous budget.** Un inspecteur ne peut examiner à fond qu'une fraction fixée des épisodes, au vu de signaux imparfaits, face à un agent qui choisit quand dévier et de combien : quelle est la valeur de ce jeu à horizon fini et quelle politique d'examen l'atteint, selon que l'agent connaît ou non cette politique ?

*Pour chaque cible, trois réponses nous aideraient : « connu » (et où), « mal posé » (et pourquoi), « ouvert et intéressant » (et sous quelle forme précise).*
