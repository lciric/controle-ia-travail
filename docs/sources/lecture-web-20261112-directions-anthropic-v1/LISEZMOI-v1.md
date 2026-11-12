# Lecture web du 12 novembre 2026 — directions d'Anthropic, menaces diffuses, moniteurs d'activations sous décalage — v1

Session « attaquant informé » `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Pièce de
sources, pas une analyse. Ne se réécrit pas (R12).

## Origine
Questions de Lazar du 12 novembre 2026 : (1) le programme fait-il de la surveillance des activations, de la surveillance
du comportement, de la détection d'anomalies ; (2) répond-il assez au risque de décalage de distribution ; (3) comment
amender le programme et l'organisme au regard de ce qu'Anthropic juge prometteur ; (4) « a-t-on bien fait de prendre des
moniteurs dans notre programme sur les menaces diffuses ? ».

## Contenu
- `rendus-huit-lecteurs-v1.json` : sorties structurées de huit sous-agents de lecture web, un thème chacun (constats avec
  adresse et citation exacte, « lentille », lacunes). Consigne exacte : `consigne-huit-lecteurs-v1.js`.
- `page-anthropic-recommended-directions-20250110.html` : la page « Recommendations for Technical AI Safety Research
  Directions » (10 janvier 2025), relevée le 12 novembre 2026 sur https://alignment.anthropic.com/2025/recommended-directions/ .
- `billet-anthropic-diffuse-ai-control-20260623.html` : « Diffuse AI Control on Fuzzy Tasks » (23 juin 2026),
  https://alignment.anthropic.com/2026/diffuse-ai-control/ .
- `billet-hebbar-diffuse-threats-20250430.md` : « How can we solve diffuse threats like research sabotage with AI
  control? » (Vivek Hebbar, 30 avril 2025), texte rendu par l'interface publique du forum (identifiant `Mf5Hnpi2KcqZdmFDq`).
- `index-blog-alignement-anthropic-20261112.html` : index du blog d'alignement d'Anthropic au 12 novembre 2026.
- Non déposé (4,6 Mo) : rapport de risque d'août 2026,
  https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf ,
  SHA-256 `d76815f8c0bd284a33c7017d642d0734ba903ae63f7c1e6ca7778b35b2c40fa4`.

## Statut de provenance (R7)
**Relevé web par sous-agents : non opposable.** Chaque constat porte « lu_sur_source_primaire », déclaré par le lecteur ;
aucun PDF n'est empreinté ici, aucune page n'est citée. Aucun chiffre de cette pièce n'entre dans un préenregistrement ou
un papier sans vérification sur source primaire empreintée.

Contre-vérifié par la session elle-même, sur la source : la phrase du billet du 23 juin 2026 sur les interventions
d'entraînement ; la prémisse et la complémentarité chez Hebbar ; le résumé de arXiv 2604.16286 ; la phrase de Gasteiger et
collègues (« the noisy monitoring signal might be sufficient to train away sandbagging ») ; les chiffres du billet du
21 août 2026 sur les détecteurs de mensonge ; les trois versions de arXiv 2606.08892 (v3 du 4 novembre 2026) ; trois
phrases du rapport de risque d'août 2026 (texte extrait du PDF, numéros de page non relevés).
Non contre-vérifié : le contenu du dépôt de code `MikhailTerekhov/diffuse_control` (inaccessible depuis la session) ;
tout le reste.

## Réserves
- Cloison : les lecteurs n'ont ouvert aucun fichier du dépôt ; aucune requête web ne nomme le programme. La session n'a
  lu aucun résultat, score ni seuil calibré de sonde ou de moniteur du programme.
- Cette pièce vient de la session du bras d'attaque : les suggestions de « lentille » qui touchent à la conception de
  moniteurs sont du matériau, jamais une consigne ; leur usage se décide hors du bras d'attaque.
- Le dépôt connaissait déjà la plupart des parutions relevées (dont la v3 de arXiv 2606.08892, 2611.10620, 2610.12445,
  2606.12618). Absents du dépôt au 12 novembre, par recherche de chaînes : le billet de Redwood Research du 25 septembre
  2026 (« Continual learning might make your blocking monitors nearly useless »), TASTE, « AI Organizations… »,
  « Automated Weak-to-Strong Researcher », « Forecasting Rare Language Model Behaviors » ; et la prémisse de Hebbar
  (« exactly how suspicious a benign model would look ») n'apparaît dans aucune lecture.
- TASTE n'est pas public : accès sur demande par formulaire (contact externe : Lazar envoie).
