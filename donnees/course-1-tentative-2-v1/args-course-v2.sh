# Arguments communs de la course 1, tentative 2, sur l orchestrateur v50 (sans étage de tests de mort, sans moisson). Adaptés de args-course-v1.sh (v45) : chemin de l arbre ; étiquette externe gemini-4-argon (v50, changement de contrat 3) ; sans Opus proposeur (décision de Lazar, ≈ 07:20 UTC) : proposeurs Fable 5.1 et Argon, Opus juge seulement ; budget total Claude ramené de 50 à 40 ; autres budgets inchangés.
DOS=/root/ideation-v1; O=$DOS/orchestrateur-v50/arbre; P=$DOS/pieces/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1
ARGS=(--liste-blanche $DOS/liste-blanche-ideation-v4-session-depot-v1.json --question $P/question-collisionneur-priorites-sept-questions-v3.md)
for f in extraits-v1/brief-notre-marque-v1.md extraits-v1/questions-section-A-v1.md extraits-v1/classement-v2-sections-1-a-4-v1.md \
  extraits-v1/anteriorite-Q{1,2,3,4,5,6,7,pont}-sections-1-a-3-v1.md anteriorite-coevolution-et-boite-blanche-v1.md \
  anteriorite-universalite-metriques-v1.md conception-pole-scientifique-v1.md integration-proposeurs-ia-v1.md; do ARGS+=(--piece $P/$f); done
CORPUS=$(ls $P/corpus-primaire-v1/extrait-*.md $P/corpus-primaire-v2/extrait-*.md $P/corpus-primaire-v3/extrait-*.md)
for f in $CORPUS; do ARGS+=(--piece $f); done
for f in extraits-v1/anteriorite-Q{1,2,3,4,5,6,7,pont}-sections-1-a-3-v1.md anteriorite-coevolution-et-boite-blanche-v1.md; do ARGS+=(--piece-juge $P/$f); done
for f in $CORPUS; do ARGS+=(--piece-juge $f); done
ARGS+=(--materiau $P/preideation-interne-v1/fiches-anonymes.md --seconde-passe
  --attestation-materiau $DOS/attestation-materiau-v1.json --temoins $DOS/temoins/temoins-ideation-tiers-v1.json
  --proposeur fable=claude-fable-5-1
  --juge juge-fable=claude-fable-5-1 --juge juge-opus=claude-opus-5-5
  --proposeur-externe argon=gemini-4-argon --juge-externe argon-juge=gemini-4-argon
  --commande-externe "/usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v3.sh"
  --budget 'proposeur_ideation|claude-fable-5-1=9.3'
  --budget 'juge_ideation|claude-opus-5-5=4' --budget 'juge_ideation|claude-fable-5-1=7'
  --budget 'proposeur_ideation|gemini-4-argon=2.5' --budget-passe-2-externe-usd 3.1 --budget 'juge_ideation|gemini-4-argon=3.5'
  --budget-total-usd 40 --budget-externe-usd 12.8 --budget-controle-externe-usd 3.1
  --prix-entree-usd-par-million-jetons 8.3 --taille-max-consigne-externe 1490000
  --taille-max-pieces 750000 --nombre 8 --graine 20261028 --delai-session-s 3600 --delai-commande-s 1800
  --racine-depot /home/user/controle-ia-travail)
