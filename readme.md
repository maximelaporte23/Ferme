# Projet Ferme

### By Dellau Landry, Gonzalez Célia, Laporte Maxime et Madelpech Aimy

# Mise en place du projet
### Travail en local

Nous avons créer un repository de l'équipe "Ferme", qui contient le projet de la ferme écologique Chronobio.
Pour cela nous avons besoin de créer un environnement virtuel "venv" qui nous permet de lancer nos programmes et d'avoir l'image du jeux.

- Pour installer l'environnement virtuel : `python -m venv venv`

### Création d'un dépot privé

Nous avons créer notre repository "Ferme" qui contient un dossier "chronobio" ceci nous permet de pouvoir lancer notre compétition en mode réseau.

### Installation des outils
- Pour nous permettre de lancer la simulation dans l'environnement virtuel de la meilleure des façons, il est important d'avoir une version de python la plus récente car les versions antérieur à python3.10 ne lancent pas la simulation.
- Installation de python3.10: `pip install python3.10`
- Installation des requirements pour les dépendances: `python3 -m pip install -r requirements.txt`

### Lancement la simulation

- Afin de lancer la simulation du jeu, nous devons rentrer dans l'environnement virtuel en allant dans le projet Chronobio : `./chronobio/`

- Activer l'environnement virtuel installer précédement : `source venv/bin/activate`

    -> Lorsque l'envrironnement vituelle est créer nous avons le (venv) qui s'affiche à gauche du terminal pour nous assurer que nous sommes bien en vituel.

- Enfin, pour pour lancer l'interface du jeu il faut lancer le : `./competition.sh`

### Arrêt de la simulation
- Afin d'interrompre la simulation du jeux la ligne de commande à exécuter est dans le chemin du projet chronobio et il faut lancer dans le terminal le script : `python killal.py`

# GitHub Actions
## Installations de pytest

Pour installer le module des tests:
`pip install pytest`

Nous avons créer dans notre repo un dossier "github" puis un workflow ou nous avons intégrer un fichier qui nous permet de pouvoir automatiser des tests.
```
/.github/workflows/run_test.yml
```

# Gestion des Tests
### Outils de formatage de code

Pour pouvoir vérifier l'intégrité de notre code nous avons installé des des dépendances qui vérifie les normes, tel que la pep20 par exemple, avcec Flake8 ou ruff.

    `pip install flake8`
    `pip install ruff`

Installation de `mypy`:

    `pip install mypy`

Ceci sont des aides de formatage de code.

### Installation des pré-commit
Pré-commit nous sert à détecter et à reformater le code si il y a des erreurs de formattage.
Dans le répertoire .github dans le répertoire de "ferme", nous avons mis dans le dossier workflows, le fichier `run_test.yml`



### Installation des Utilisation de pytest
### Utilisation de outils dans le projet
### Tests des pré-commit

### Navigation dans le projet

# Installation des pré-commit
### Installation des Utilisation de pytest
### Utilisation de outils dans le projet
### Tests des pré-commit



# Le plan d'action



# Théorie VS Pratique

### Théorie :

Lors du développement du projet nous devions prendre en compte plusieurs éléments :
    • Achat champs 
    • Achat tracteurs 
    • Gestion des employés 
    • Gestion des licenciements 
    • Gestion des déplacements 
    • Gestion production soupe 
    • Vente de légumes du champ

### Gestion champs/tracteurs
Nous avons opté pour un achat des 5 champs soit une dépense de 50 000€ et l'achat de 5 tracteurs soit 150 000€, soit un total de 200 000€ lors du jour 0.

### Gestion des employés
Pour la gestion des employés nous avons opté pour la stratégie suivante:
    • Licenciement le 30 du mois (à tester le 29)
    • Embauche le 30 du mois
Nous embauchons 40 salariés le jour 0.

### Gestion des licenciements
Pour licencier une fois en 5 ans :
Pour la gestion des licenciements, nous avons calculé le pourcentage d’augmentation pour chaque mois et nous en avons déduit que de licencier les ouvriers à 30 mois (2,5 ans) est le plus optimal.

Pour licencier plusieurs fois en 5 ans, l’optimisation est celle ci-dessous :
Pour la gestion des licenciements nous avons fait une simulation sur plusieurs durées tels que 6 mois, 7 mois, 1an, 2ans... Au final lors de cette simulation de coût nous en avons déduit que le coût de revient optimal est une gestion de licenciement sur une durée de 1 an et 3 mois.

### Explication pattern
Lorsque nous avons un groupe d'employés sur un champ nous avons les actions suivantes effectuées :
    • 1 employé plante 1 des 5 légumes (Dès qu’un légume est planté, le prochain dans la liste est planté, un légume après l’autre)
    • 5 employés arrosent le champ 
Lorsqu'un tracteur est appelé sur un champ c'est pour stocker la récolte dans l'usine. Les 4 cuisiniers produisent en permanence des soupes. Ensuite, au bout de 4 ans, 3 cuisiniers supplémentaires sont embauchés pour vider les stocks dans l’usine à soupe.

### Gestion de la production soupe
Dans un premier temps, nous avons déterminé le nombre de légumes que nous arrivons à stocker au mieux afin de déterminer le nombre d’employé nécessaire. Nous produisons 90000 légumes au mieux, sans catastrophes naturelles. Pour une production de soupe de 5 légumes, cela fait un consommation de 18000 légumes. Nous avons donc employé 6 cuisiniers afin d’exploiter au mieux le stock de l’usine.

Nous avons employé 3 cuisiniers dans un premier temps afin de gonfler les stocks de légumes dans l’usine à soupe. Au bout de la dernière année, nous embauchons 5 cuisiniers afin de vider les stocks et d’augmenter les bénéfices.

### Scores obtenus
Mode Local : 3 500 000
Mode Réseau : 2 000 000