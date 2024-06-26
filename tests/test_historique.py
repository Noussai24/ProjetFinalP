from app.api.v1.historique import Historique


def test_arroseplante_jour_de_pluie():
    """
    Teste la fonction ArrosePlante avec un cas où il pleut tous les jours
    """
    # Données d'entrée
    pays = "France"
    dt = "2024-06-15"
    endt = "2024-06-15"

    # Exécution de la fonction
    data = Historique.ArrosePlante(pays, dt, endt)

    # Vérification du type de retour
    assert isinstance(data, list)

    # Vérification du nombre de jours
    assert len(data) == 1

    # Vérification des données du jour
    assert data[0]["date"] == "2024-06-15"
    assert data[0]["meteo du jour"] == "il pleut"


def test_arroseplante_jour_sans_pluie():
    """
    Teste la fonction ArrosePlante avec un cas où il ne pleut pas
    """
    # Données d'entrée
    pays = "France"
    dt = "2024-06-25"
    endt = "2024-06-25"

    # Exécution de la fonction
    data = Historique.ArrosePlante(pays, dt, endt)

    # Vérification du type de retour
    assert isinstance(data, list)

    # Vérification du nombre de jours
    assert len(data) == 1

    # Vérification des données du jour
    assert data[0]["date"] == "2024-06-25"
    assert data[0]["meteo du jour"] == "il pleut pas il faut arroser les plantes"
