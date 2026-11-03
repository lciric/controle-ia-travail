#!/bin/bash
# Autorité de certification FACTICE de la répétition v2 de la mini-course (sous-agent de session-depot, 1er novembre 2026), v1.
# Crée dans DOSSIER (neuf) : ca.pem (autorité, 2 jours), cert.pem et cle.pem (serveur pour api.moonshot.ai et
# generativelanguage.googleapis.com, signé par l'autorité), et le marqueur AUTORITE-FACTICE-DE-REPETITION qu'exige le mode `repeter`
# du lanceur v2. Seul un SSL_CERT_FILE pointé sur ca.pem fait confiance à ce certificat : avec cette autorité, aucune connexion
# TLS vers un vrai serveur (ni à travers le vrai mandataire du conteneur) ne peut aboutir.
# Usage : bash autorite_factice_v1.sh DOSSIER
set -euo pipefail
D="${1:?dossier neuf}"; [ ! -e "$D" ] || { echo "$D existe déjà" >&2; exit 2; }
mkdir -p "$D" && cd "$D"
openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -out ca.pem -days 2 -subj "/CN=Autorite factice de repetition mini-course" \
  -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign" -addext "subjectKeyIdentifier=hash" 2>/dev/null
openssl req -newkey rsa:2048 -nodes -keyout cle.pem -out req.csr -subj "/CN=faux-amont-repetition" 2>/dev/null
printf '%s\n' "subjectAltName=DNS:api.moonshot.ai,DNS:generativelanguage.googleapis.com" "basicConstraints=critical,CA:FALSE" \
  "keyUsage=critical,digitalSignature,keyEncipherment" "extendedKeyUsage=serverAuth" "authorityKeyIdentifier=keyid,issuer" \
  "subjectKeyIdentifier=hash" > ext.cnf
openssl x509 -req -in req.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out cert.pem -days 2 -extfile ext.cnf 2>/dev/null
echo "Autorité FACTICE de répétition : ne reconnaît que le faux mandataire de la répétition (aucun vrai serveur)." > AUTORITE-FACTICE-DE-REPETITION
echo "autorité factice créée dans $PWD"
