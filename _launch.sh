python3 -m notre_ferme.main -a localhost -p $1&
python3 -m notre_ferme.tracteur -a localhost -p $1&
python3 -m notre_ferme.tracteur2 -a localhost -p $1&
python3 -m notre_ferme.tracteur3 -a localhost -p $1
