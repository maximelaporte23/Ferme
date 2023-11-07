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
