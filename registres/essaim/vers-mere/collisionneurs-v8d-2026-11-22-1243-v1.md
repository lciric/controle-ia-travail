# Collisionneurs v8d, compte rendu 50 : papier A (mode isolé) fini ; v8k « à corriger »

Écrit à 2026-11-22T12:43:44Z (`date -u`).

- `runs/collisionneur-protocole-x-papier-a-isole-v1-20261122-112512` : fini au code 0 à 12:43:09Z ; `verifier` après : tient. 16 essais, une coupure reprise une fois. Dépense : **14,29 USD** (GO-2026-11-22-17, plafond 45). Par clé : RR_ANTHROPIC_API_KEY_LUC 6,30 ; GEMINI_API_KEY 6,69 ; OPENAI_API_KEY_2 1,29. La voie 2 passe au papier B.
- **v8k** : contre-lue par un Opus neuf (`docs/notes/collisionneur-v9/verification-collisionneur-v9-v8k-opus-v1.md`), verdict « à corriger ». Sans option, elle se comporte comme la v8j (120 compositions comparées), et les valeurs citées sont confirmées. Cinq bloquants :
  1. Kimi doit être borné à 128 000 jetons sous `--sortie-max` (ta décision) ;
  2. les délais sous `--sortie-max` doivent couvrir 128 000 jetons ;
  3. Opus 4.6 doit recevoir la réflexion adaptative (sans elle, il ne réfléchit pas, selon la documentation d'Anthropic) ;
  4. l'absence de réglage d'effort pour Astra doit être déclarée ;
  5. deux gardes d'argent n'ont pas d'essai.
  Non-bloquants portés aussi : refus des redirections, qui pourraient emporter une clé vers un autre hôte (défaut ancien, présent sur tous les chemins) ; préfixe de `--cle-anthropic` ; effort de Kimi ; `--sortie-max` scellé dans la composition et lu par le devis de reprise. Les corrections vont dans une **v8l**, par le même développeur, puis à la vérification du même contre-lecteur.
- **Délais sous `--sortie-max` : aucun fournisseur ne documente de débit.** Je propose un délai de 10 800 secondes (trois heures) par appel pour toutes les espèces, déclaré supposé et journalisé. Un délai long ne coûte que de l'attente, alors qu'une coupure se paie au pire. **À ton mot**, ou bien donne une autre valeur.
