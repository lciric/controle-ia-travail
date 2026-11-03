#!/bin/bash
# (Kit Ibrahim Q1, v1, dérivé par substitution de noms du kit Kirchner Q2 v2 — branche outils/course-kirchner-q2-v1, 53e1f738 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions et de kits antérieurs ci-dessous sont héritées.)
# (Kit Ibrahim Q1, v1, dérivé à l'octet près des substitutions de nom du kit Heimersheim — branche outils/course-heimersheim-v1 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions antérieures ci-dessous sont celles du kit Heimersheim.)
# Autorité de certification FACTICE de la répétition de la course Ibrahim Q1 (sous-agent de session-depot, 3 novembre 2026), v1,
# dérivée de nuit/repetition/autorite_factice_v1.sh (inchangé) : certificat serveur pour les quatre hôtes des relais
# (api.anthropic.com, api.openai.com, api.moonshot.ai, generativelanguage.googleapis.com) et marqueur
# AUTORITE-FACTICE-DE-REPETITION qu'exige le mode `repeter` du lanceur. Seul un SSL_CERT_FILE pointé sur ca.pem fait confiance à
# ce certificat : aucune connexion TLS vers un vrai serveur ne peut aboutir avec cette autorité.
# Usage : bash autorite_factice_ibrahim_v1.sh DOSSIER_NEUF
set -euo pipefail
D="${1:?dossier neuf}"; [ ! -e "$D" ] || { echo "$D existe déjà" >&2; exit 2; }
mkdir -p "$D" && cd "$D"
openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -out ca.pem -days 2 -subj "/CN=Autorite factice de repetition Ibrahim" \
  -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign" -addext "subjectKeyIdentifier=hash" 2>/dev/null
openssl req -newkey rsa:2048 -nodes -keyout cle.pem -out req.csr -subj "/CN=faux-amont-repetition-kirchner" 2>/dev/null
printf '%s\n' "subjectAltName=DNS:api.anthropic.com,DNS:api.openai.com,DNS:api.moonshot.ai,DNS:generativelanguage.googleapis.com" \
  "basicConstraints=critical,CA:FALSE" "keyUsage=critical,digitalSignature,keyEncipherment" "extendedKeyUsage=serverAuth" \
  "authorityKeyIdentifier=keyid,issuer" "subjectKeyIdentifier=hash" > ext.cnf
openssl x509 -req -in req.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out cert.pem -days 2 -extfile ext.cnf 2>/dev/null
echo "Autorité FACTICE de répétition : ne reconnaît que le faux mandataire de la répétition (aucun vrai serveur)." > AUTORITE-FACTICE-DE-REPETITION
echo "autorité factice créée dans $PWD"
