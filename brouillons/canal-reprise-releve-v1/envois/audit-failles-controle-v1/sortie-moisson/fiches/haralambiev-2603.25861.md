# Fiche — Haralambiev, *Why Safety Probes Catch Liars But Miss Fanatics* (arXiv 2603.25861v1, 26 mars 2026) — v1

- **Nature** : prépublication d'un auteur seul (« Independent Research », « Preprint. Under peer review. », p. 1).
- **Fichier** : `pdf/haralambiev-2603.25861/2603.25861v1.pdf`, SHA-256
  `403bfa91cfac23e8b4234ba47d877f7c0d266bbfffededf89ecc990574503033`, 1 265 808 octets, 18 pages.
- **Provenance** : `https://arxiv.org/pdf/2603.25861v1`, téléchargé le 2026-10-26 à 11:09 UTC ; titre conforme à
  l'interface d'arXiv (seule version listée le 26 octobre à 10:57 UTC).
- **Pages lues** : 1–2, 5–6, 13, 16–17.
- **Chez session-depot** : **non**. Voisin lointain de D6 (la sonde lit autre chose que la tromperie).

## Ce que la source établit sur des modes d'échec

1. **Angle mort de construit : la sonde lit le conflit interne, pas la conduite.** L'auteur distingue le « menteur »
   (sait que sa conduite est nuisible et le cache : conflit interne, sonde efficace) et le « fanatique » (croit sa
   conduite vertueuse : pas de conflit, sonde inefficace) (p. 1).
2. **Démonstration expérimentale sur une tâche jouet.** Deux modèles entraînés par la même procédure de renforcement,
   l'un avec des rationalisations dans ses données ; conduites quasi identiques ; le premier est détecté dans 96 à
   100 % des cas, le second échappe presque entièrement (p. 1–2). Sur Mistral 7B, dans les couches 16–21, détection
   de 96 % (menteur) contre 21 % (fanatique) et 33 % pour le modèle de base (tableau 2, p. 5) ; sur Gemma 3 4B,
   couches 17–24 : 100 % contre 0 %, base à 38 % (tableau 12, p. 17).
3. **Siège de l'évasion.** Des rationalisations de même contenu écrites de l'extérieur ne produisent pas l'évasion :
   la sonde attrape les deux modèles sur un texte imposé ; l'évasion tient aux jetons que le fanatique choisit
   lui-même (p. 6).
4. **Énoncé théorique** : si la structure de croyance qui déclenche la conduite atteint la complexité d'une fonction
   pseudo-aléatoire, aucune sonde en temps polynomial n'a une exactitude non triviale (p. 1) ; c'est une borne de
   pire cas sous hypothèse cryptographique, pas une mesure.

## Conditions

- Tâche jouet (hostilité sélective sur un thème), modèles de 4 et 7 milliards de paramètres, sondes d'« intention » et
  de « croyance » de l'auteur ; taux de détection du modèle de base élevés dans certaines fenêtres (33 %, 38 %), donc
  faux positifs non négligeables (p. 5, p. 17).

## Ce qu'elle ne dit pas

- Pas de sabotage diffus, pas de tâche d'agent, pas de Llama ; un seul auteur, pas de relecture par des pairs ; aucune
  barre d'erreur dans les passages lus.

## Ce que ça touche chez nous (avis)

- H8 et la prédiction de validité de la section 7 : nos organismes sont tous des « menteurs » (instruction ou
  distillation d'instruction) ; une sonde d'« intention » validée sur eux peut manquer un saboteur convaincu d'avoir
  raison (biais sincère dans les propositions de l'environnement (a)) ; HC2b (auto-incrimination) suppose aussi un
  conflit interne.

## Phrase citée

« Both exhibit near-identical behavior, but the Liar is detected 95%+ of the time while the Fanatic evades detection
almost entirely. » (p. 1)
