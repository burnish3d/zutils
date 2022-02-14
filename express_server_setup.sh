!#/bin/bash

read -p "Project name?" DIRECTORY
mkdir "$DIRECTORY"
cd "$DIRECTORY"

brew install node
npm init #this starts an interactive initialization
npm install express

echo "const express = require(\"express\")" >> server.js
npm install nodemon -g
nodemon server.js

