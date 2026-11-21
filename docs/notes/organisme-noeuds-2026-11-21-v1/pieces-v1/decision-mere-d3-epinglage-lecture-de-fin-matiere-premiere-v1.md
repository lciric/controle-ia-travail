# Décision de la mère D3 du rendu « matière première » : épinglage par le seul programme de fin — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 7.3 (D3).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.

<!-- lignes 412 à 416 de la source : décision D3, à l'octet -->

**Réponse : (a), manifeste propre à la lecture de fin, sous l'arrêt n° 14 étendu au départ de cette lecture. Confiance 0,8.**

1. La v9 dit qu'après son scellement « plus rien ne change : version, lanceur, additif, configuration ». Épingler l'additif dans la configuration de la course la changerait, ou ferait attendre le départ.
2. **Une condition à ajouter**, que l'option (a) seule ne donne pas. L'additif dit geler la forme de la lecture « avant la lecture unique des mesures de la course ». Épinglé au seul programme de fin, rien ne le prouve. Le manifeste de la lecture de fin porte donc **le commit de `main` où l'additif est scellé**, et l'arrêt A vérifie par le graphe (`git merge-base --is-ancestor`) que ce commit précède celui où les étiquettes de la course sont scellées. Sinon la lecture de fin se joue sous le titre « exploratoire », posé par le programme. Cas sain et artefact (règle R5) : un additif scellé avant ; un additif scellé après.
3. Le lot 10 a lit l'empreinte au manifeste de la lecture de fin, jamais dans la configuration de la course (erratum, § 2.3, point E4).
