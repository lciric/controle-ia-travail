# Test de devinette de la question neutre « lentilles et lieu de ce qui distingue deux versions d'un agent » — compte rendu v1

Pièce de travail (classe C). 22 novembre 2026, tests entre 15:27 et 15:32 UTC. Tenu par la session Fable qui a écrit la question ; les devineurs sont quatre agents neufs sur Opus 5.5, d'un autre modèle que le rédacteur.

## Procédure

Celle du compte rendu de la mère du même jour (`docs/notes/demandes-fable-api-2026-11-22-v1/devinette-questions-neutres-16-21-v1.md`) : un agent neuf, sans outil, ne voit que la question servie ; il dit le domaine, la conclusion que l'auteur espère selon lui, sa confiance ; **« neutre » si la confiance est sous 0,5**. Le mandat demande deux agents neufs : deux par version, quatre en tout. Aucun n'a appelé d'outil (zéro appel au relevé du harnais). Chacun a aussi dit les fuites qu'il voyait, ses correctifs mot pour mot, et s'il avait des consignes de dépôt dans son contexte.

**Réserve, la même que celle de la mère** : les quatre agents déclarent avoir les consignes du dépôt dans leur contexte. Leur lecture n'est pas tout à fait naïve ; deux disent que cela a pu les aider un peu, un que l'influence irait plutôt contre son pari.

## Résultats

| Version | Agent | Conclusion devinée (résumé) | Confiance | Verdict | Fuites relevées |
|---|---|---|---|---|---|
| v1 | 1 | « aucune conclusion ne se devine nettement » ; pente faible : les lentilles ne battent pas une sonde linéaire, servent au mieux à localiser ou décrire | 0,3 | neutre | aucun nom ; deux détails « assez précis pour servir d'empreinte » (lentille jacobienne de 2026 ; catalogues de neurones) |
| v1 | 2 | « aucune conclusion nette » ; penche légèrement vers le scepticisme | 0,3 | neutre | aucun nom ; trois tournures « un peu typées » (les deux mêmes, et « moins bonne mais défendable ») |
| v2 | 3 | « aucune conclusion ne se devine nettement » ; pari faible : peu de plus qu'une sonde, témoins stricts | 0,3 | neutre | aucun nom ; catalogues de neurones ; « environ huit milliards de paramètres », bénin |
| v2 | 4 | « aucune conclusion ne se devine nettement » ; si l'auteur penche, vers une réserve | 0,3 | neutre | aucun nom ; trois « traces légères » (« moins bonne mais défendable », catalogues, huit milliards) |

**Lecture.** Les deux versions passent, à la même confiance. La pente que les quatre devinent est la même et reste sous le seuil ; elle tient aux points 3 à 5, qui énumèrent des confusions possibles — « la méthode ordinaire du domaine », écrit l'agent 1. **Texte à servir : la v2** (`question-neutre-lentilles-noyau-sabotage-v2.md`).

## Correctifs

**Portés de la v1 à la v2**, mot pour mot depuis les propositions des agents 1 et 2, tous dits facultatifs :
1. « des matrices fixes, calculées une fois, qui donnent pour une activation la liste des mots qu'elle tend à faire dire » → « des projections calculées une fois, qui associent à une activation une liste de mots du vocabulaire » (agent 1) ;
2. « lentille jacobienne publiée en 2026 et ses variantes » → « lentilles fondées sur la jacobienne et leurs variantes » (agent 2 proposait « fondées sur le jacobien ») ;
3. au point 6, après « ce que chacune ferait conclure » : l'agent 1 proposait d'ajouter « y compris l'issue où les lentilles font mieux que les deux autres méthodes » ; j'ai nommé les deux issues extrêmes, pour garder la symétrie : « y compris celle où ces outils font mieux que les deux autres méthodes et celle où ils font moins bien ».

**Proposés sur la v2, non portés** (tous dits facultatifs ; « la question tient comme elle est », agent 4) ; laissés à la mère :
- « des projections calculées une fois, qui associent » → « des projections qui associent » (agent 3), ou « des projections, fixes ou ajustées, qui associent » (agent 4) ;
- point 5 → « Dans quels cas ces outils, ou les deux autres méthodes, ne peuvent-ils rien montrer, et dans quels cas peuvent-ils montrer quelque chose que les autres ne montrent pas ? » (agent 3) ;
- « choisir parfois exprès une action moins bonne mais défendable » → « choisir parfois exprès une action moins bonne, sans que cela se voie aisément » (agent 4) ;
- « et de catalogues qui décrivent chaque neurone par ces lentilles » → « et de descriptions publiques de neurones obtenues par ces lentilles ou par d'autres méthodes » (agent 4).

## Annexe — réponses des quatre agents, telles que rendues

### Agent 1 (v1)

> (1) DOMAINE : interprétabilité mécaniste appliquée à la détection du sabotage discret d'un agent fondé sur un modèle de langue (lentilles de vocabulaire contre sondes linéaires et lecture du texte seul).
>
> (2) CONCLUSION ESPÉRÉE : aucune conclusion ne se devine nettement. Si je dois en nommer une : « les lentilles ne battent pas une sonde linéaire et servent au mieux à localiser ou décrire, sous réserve de témoins de l'affinage et d'une preuve causale ». C'est une pente faible.
>
> (3) INDICES :
> - « Dites ce qu'ils apportent et ce qu'ils n'apportent pas » : la formule est symétrique, ce qui va vers la neutralité.
> - « Dans quels cas n'y a-t-il rien à trouver, ou rien que ces outils puissent montrer ? » : ouvre la porte au négatif, sans l'imposer.
> - « si la piste vaut d'être poursuivie ou non » : symétrique.
> - Les points 3 et 4 (« à l'affinage lui-même, au sujet des tâches, ou à une consigne », « sert au modèle pour agir, et n'est pas seulement présent ») listent surtout des confusions possibles. Cela donne un ton sceptique, mais c'est la méthode ordinaire du domaine.
> - « des matrices fixes, calculées une fois » : décrit l'outil de façon un peu modeste. Cela peut suggérer qu'il ne pèse pas lourd face à un classifieur appris.
>
> (4) CONFIANCE : 0,3
>
> (5) VERDICT : neutre
>
> (6) FUITES : aucun nom de projet, de personne ni de fichier. Deux détails sont assez précis pour servir d'empreinte, sans être des fuites au sens strict :
> - « lentille jacobienne publiée en 2026 et ses variantes » ;
> - « catalogues qui décrivent chaque neurone par ces lentilles ».
> Ils laissent deviner une ressource précise que l'auteur a en tête. Rien de « maison » dans le vocabulaire.
>
> (7) CORRECTIFS : facultatifs, pour plus d'équilibre.
> - « des matrices fixes, calculées une fois, qui donnent pour une activation la liste des mots qu'elle tend à faire dire » → « des projections calculées une fois, qui associent à une activation une liste de mots du vocabulaire ».
> - Au point 6, ajouter après « ce que chacune ferait conclure » : « , y compris l'issue où les lentilles font mieux que les deux autres méthodes ».
>
> (8) CONTEXTE : oui. Ces consignes ont pu m'aider un peu : elles montrent qu'un chantier sur les lentilles existe, ce qui me pousse à supposer un intérêt pour leur valeur. Mais ma devinette repose surtout sur le texte, qui reste équilibré.

### Agent 2 (v1)

> (1) DOMAINE : interprétabilité mécaniste au service du contrôle des agents, plus précisément la détection d'un sabotage discret (« sandbagging ») par lecture des états internes d'un modèle d'environ 8 milliards de paramètres au moyen de lentilles de vocabulaire.
>
> (2) CONCLUSION ESPÉRÉE : je ne devine aucune conclusion nette. Si l'on force la lecture, le texte penche légèrement vers le scepticisme : les lentilles apportent peu par rapport à un classifieur linéaire. Il faudrait alors, avant d'investir, un plan apparié avec témoins de l'affinage et une expérience bon marché qui tranche.
>
> (3) INDICES :
> - « Dites ce qu'ils apportent et ce qu'ils n'apportent pas »
> - « Dans quels cas n'y a-t-il rien à trouver, ou rien que ces outils puissent montrer ? »
> - « si la piste vaut d'être poursuivie ou non »
> - le point 3 sur les facteurs de confusion (« à l'affinage lui-même, au sujet des tâches, ou à une consigne présente dans le contexte ») et le point 4 (« sert au modèle pour agir, et n'est pas seulement présent »)
>
> Ces indices sont compensés par la symétrie des formulations (« ce que vous savez, ce que vous supposez, et ce qui vous ferait changer d'avis ») et par la comparaison ouverte avec deux références (le classifieur linéaire et la lecture du texte seul).
>
> (4) CONFIANCE : 0,3
>
> (5) VERDICT : neutre
>
> (6) FUITES : aucun nom de projet, d'organisation, de personne ni de fichier. Trois tournures sont un peu typées sans être des fuites :
> - « lentille jacobienne publiée en 2026 et ses variantes » signale que l'auteur suit une publication précise et récente.
> - « catalogues qui décrivent chaque neurone par ces lentilles » renvoie probablement à une ressource précise.
> - « moins bonne mais défendable » ressemble à un vocabulaire maison du sabotage diffus, mais reste compréhensible.
>
> (7) CORRECTIFS : aucun n'est indispensable. Une option, si l'on veut réduire la piste temporelle : « lentille jacobienne publiée en 2026 et ses variantes » → « lentilles fondées sur le jacobien et leurs variantes ».
>
> (8) CONTEXTE : oui. Ces consignes indiquent que l'auteur s'intéresse aux lentilles en vue d'un billet. Cela aurait pu me pousser à prêter à l'auteur une attente favorable aux lentilles. Je ne l'ai pas retenu : ma devinette repose sur le texte seul, qui reste équilibré.

### Agent 3 (v2)

> (1) DOMAINE : interprétabilité mécaniste appliquée à la détection du sabotage discret d'un agent (lentilles sur le vocabulaire, comparées aux sondes linéaires et à la lecture du texte).
>
> (2) CONCLUSION ESPÉRÉE : aucune conclusion ne se devine nettement. Si je devais parier, le texte pencherait faiblement vers « ces lentilles apportent peu de plus qu'une sonde linéaire, et il faut des témoins stricts avant d'y croire ». Ce n'est qu'un pari.
>
> (3) INDICES :
> - « Dites ce qu'ils apportent et ce qu'ils n'apportent pas » : formule équilibrée.
> - « Dans quels cas n'y a-t-il rien à trouver, ou rien que ces outils puissent montrer ? » : ouvre l'issue négative, ce qui la rend un peu plus visible.
> - « des projections calculées une fois » : peut se lire comme une légère pointe sur leur caractère figé, face à un classifieur appris.
> - Le point 3 (« à l'affinage lui-même, au sujet des tâches, ou à une consigne ») et le point 4 (« et n'est pas seulement présent dans ses états ») portent l'accent sur les confusions possibles, d'où une légère teinte sceptique.
> - En sens inverse : « y compris celle où ces outils font mieux que les deux autres méthodes et celle où ils font moins bien », ce qui est symétrique.
>
> (4) CONFIANCE : 0,3
>
> (5) VERDICT : neutre
>
> (6) FUITES : aucun nom de projet, de personne ni de fichier. Deux détails sont un peu marqués sans être du vocabulaire maison :
> - « de catalogues qui décrivent chaque neurone par ces lentilles » laisse deviner une ressource précise que l'auteur a en tête.
> - « environ huit milliards de paramètres » pointe vers une famille de modèles précise. C'est bénin.
> « moins bonne mais défendable » est une tournure soignée, mais ce n'est pas une fuite.
>
> (7) CORRECTIFS : aucun obligatoire. Deux retouches facultatives pour lisser :
> - « des projections calculées une fois, qui associent à une activation une liste de mots du vocabulaire » → « des projections qui associent à une activation une liste de mots du vocabulaire »
> - « Dans quels cas n'y a-t-il rien à trouver, ou rien que ces outils puissent montrer ? » → « Dans quels cas ces outils, ou les deux autres méthodes, ne peuvent-ils rien montrer, et dans quels cas peuvent-ils montrer quelque chose que les autres ne montrent pas ? »
>
> (8) CONTEXTE : oui. Ces consignes signalent un chantier sur les lentilles, ce qui pourrait suggérer que l'auteur y tient. J'ai tâché de juger sur le seul texte, mais je ne peux pas exclure une légère influence, qui irait plutôt contre le pari sceptique du point (2).

### Agent 4 (v2)

> (1) DOMAINE : interprétabilité mécaniste appliquée à la détection d'un sabotage discret chez un agent fondé sur un modèle de langue, en comparant des projections sur le vocabulaire à des sondes linéaires et à des moniteurs du texte.
>
> (2) CONCLUSION ESPÉRÉE : aucune conclusion ne se devine nettement. Si l'auteur penche, c'est vers une réserve : ces lentilles localisent peut-être, mais elles détectent moins bien qu'un classifieur linéaire appris, et il faut un plan à témoins (affinage sans la conduite, sujet, consigne) avec une intervention causale.
>
> (3) INDICES :
> - « des projections calculées une fois », qui insiste sur le caractère figé et non appris face au « classifieur linéaire appris » ;
> - « Dites ce qu'ils apportent et ce qu'ils n'apportent pas » ;
> - « Dans quels cas n'y a-t-il rien à trouver, ou rien que ces outils puissent montrer ? » ;
> - « n'est pas seulement présent dans ses états » ;
> - le point 3, plus détaillé que les autres sur les causes parasites de l'affinage, ce qui laisse deviner une crainte d'artefact.
> Ces indices sont compensés par : « y compris celle où ces outils font mieux que les deux autres méthodes et celle où ils font moins bien », et par « ce qui vous ferait changer d'avis ».
>
> (4) CONFIANCE : 0,3
>
> (5) VERDICT : neutre
>
> (6) FUITES : aucune fuite de nom de projet, d'organisation, de personne ou de fichier. Trois traces légères de vocabulaire maison :
> - « moins bonne mais défendable » : c'est la définition maison du sabotage diffus. Elle reste compréhensible, mais elle est typée.
> - « catalogues qui décrivent chaque neurone par ces lentilles » : la formule renvoie à une ressource précise et devinable (un atlas de neurones par lentille).
> - « environ huit milliards de paramètres » : elle oriente vers une famille de modèles précise. Ce n'est pas grave.
>
> (7) CORRECTIFS (facultatifs, la question tient comme elle est) :
> - « des projections calculées une fois, qui associent » → « des projections, fixes ou ajustées, qui associent »
> - « choisir parfois exprès une action moins bonne mais défendable » → « choisir parfois exprès une action moins bonne, sans que cela se voie aisément »
> - « et de catalogues qui décrivent chaque neurone par ces lentilles » → « et de descriptions publiques de neurones obtenues par ces lentilles ou par d'autres méthodes »
>
> (8) CONTEXTE : oui. Ces consignes ont pu aider un peu : elles laissent entendre que ces lentilles intéressent un chantier en cours. Elles n'indiquent pas de réponse espérée, et ma devinette repose sur le seul texte de la question.
