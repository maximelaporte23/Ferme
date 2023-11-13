# Equipe Ferme

### Jeux python par Vincent Poulailleau
Développement du PlayerGameClient par Dellau Landry, Gonzalez Célia, Laporte Maxime et Madelpech Aimy

# Mise en place du projet
### Travail en local

Nous avons créer un repository de l'équipe "Ferme", qui contient le projet de la ferme écologique Chronobio.
Pour cela nous avons besoin de créer un environnement virtuel "venv" qui nous permet de lancer nos programmes et d'avoir l'image du jeux.

- Pour installer l'environnement virtuel : `python -m venv venv`

### Création d'un dépot privé

Nous avons créer notre repository "Ferme" qui contient un dossier "chronobio" ceci nous permet de pouvoir lancer notre compétition en mode réseau.

### Installation des outils
- Pour nous permettre de lancer la simulation dans l'environnement virtuel de la meilleure des façons, il est important d'avoir une version de python la plus récente car les versions antérieur à python3.10 ne lancent pas le plateau de jeu de la simulation.
- Installation de python3.10: `pip install python3.10`
- Installation des requirements pour les dépendances: `python3 -m pip install -r requirements.txt`

### Lancement la simulation

- Afin de lancer la simulation du jeu, nous devons rentrer dans l'environnement virtuel en allant dans le projet Chronobio : `./chronobio/`

- Activer l'environnement virtuel installer précédement : `source . venv/bin/activate`

    -> Lorsque l'envrironnement vituelle est créer nous avons le (venv) qui s'affiche à gauche du terminal pour nous assurer que nous sommes bien en vituel.

- Enfin, pour pour lancer l'interface du jeu il faut lancer le : `./competition.sh`

### Arrêt de la simulation
- Pour mettre fin à la simulation du jeu, exécutez la commande suivante dans le répertoire du projet chronobio. Utilisez le terminal pour lancer le script : `python killal.py`.
ou
`ctrl+c`

## Automatisation des tests :

### Installations de Pytest

Documentation de [PyTest](https://pypi.org/project/pytest/).

Le fichier d'installation de pytest :
`pip install -r requirements-test.txt`

Voici le contenu présent dans le fichier requirements:
```
flake8==3.9.0
pytest==7.2.2
pytest-cov==4.0.0
pre-commit==3.5.0
```

Ensuite, pour installer le module qui permet de lancer les tests en local:
`pip install pytest`

Enfin, la documentation python_coverage:

- [Pytest-cov 4.1.0 ](https://pypi.org/project/pytest-cov/)

Nous avons créer dans notre repo un dossier "github" puis un workflow ou nous avons intégrer un fichier qui nous permet de pouvoir automatiser des tests dans le workflow de github.
[run_test.yml](/.github/workflows/run_test.yml).



### Installation de `mypy`:

[MyPy](https://pypi.org/project/mypy/):`pip install mypy`

Mypy permet d'aider le programmeur à bien formater le code.

##  GitHub Actions et qualimétrie

Installation de [Flake8](https://flake8.pycqa.org/en/latest/):

Nous avons ajouté GitHub Action qui nous permet de lancer un script run_flake8.yml dont flake8 nous permet de faire de l'intégration continu dans pytest.
Celui-ci permet l'intégrité de notre code et qui vérifie les normes:


### Installation des pré-commit
Pré-commit nous sert à détecter et à reformater le code si il y a des erreurs de formattage.
Dans le répertoire .github dans le répertoire de "ferme", nous avons mis dans le dossier workflows, le fichier `run_test.yml`, ce fichier permet de vérfifier nos dépendances et les hooks du projet qui sont installés lors des pré-commit.
Ceci est lancé dans le fichier qui a été créer à la racine du projet ferme : `.pre-commit-config.yml`.

### Tests des pré-commit

La commande qui permet de lancer les pre-commit dans les fichiers les fichiers sans faire de commit précedement : `pre-commit run --all-files`


# Stratégie

### Théorie :

Lors du développement du projet nous devions prendre en compte plusieurs éléments :
• Achat des champs 
• Achat des tracteurs 
• Gestion des employés 
• Gestion des licenciements 
• Gestion des déplacements 
• Gestion production soupe 
• Vente de légumes du champ

### Gestion champs/tracteurs
Nous avons choisi d'acquérir 5 champs, entraînant une dépense de 50 000 €, ainsi que l'achat de 5 tracteurs pour un montant de 150 000 €, ce qui équivaut à une dépense totale de 200 000 € au jour 0.

### Gestion de l’emprunt
Nous empruntons 150 000€.

### Gestion des employés
Pour la gestion des employés nous avons opté pour la stratégie suivante:
• Licenciement le 30 du mois
• Embauche le 30 du mois
Nous embauchons 39 salariés le jour 0.

### Gestion des licenciements
Pour licencier plusieurs fois en 5 ans, l’optimisation est celle ci-dessous :
Nous avons simulé la gestion des licenciements sur différentes périodes, telles que 6 mois, 9 mois, 1 an, 2 ans, etc. À la suite de cette simulation des coûts, nous avons conclu que la durée optimale pour la gestion des licenciements est d'1 an et 4 mois.

### Explication de notre base
Lorsque nous avons une équipe d'employés sur un champ, les actions suivantes sont effectuées :
• 1 employé plante 1 des 5 légumes (Le légume planté est celui le moins présent dans le stock)
• 5 employés arrosent chaque champ 
• 1 tracteur par champ
Quand un tracteur est mobilisé sur un champ, c'est dans le but de stocker la récolte dans l'usine. Les 3 cuisiniers produisent en permanence des soupes. Ensuite, après une période de 4 ans (48 mois), 4 cuisiniers supplémentaires sont embauchés pour épuiser les stocks dans l'usine à soupe.

### Gestion de la production soupe
Initialement, nous avons évalué la capacité optimale de stockage des légumes pour déterminer le nombre d'employés requis. Nous stockons jusqu'à 90 000 légumes, en l'absence de catastrophes naturelles. Avec une production de soupe utilisant 5 légumes, cela équivaut à une consommation de 18 000 légumes.

Nous avons engagé trois cuisiniers pour augmenter le stock de légumes dans l'usine à soupe. À la fin de la dernière année, nous avons recruté 4 cuisiniers supplémentaires dans le but de liquider les stocks et d'optimiser les bénéfices.

### Scores obtenus
Mode Local : 4 040 041
Mode Réseau : 3 996 030
