import time
import sys
import os

# Ajouter le chemin vers le répertoire contenant votre module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app/api/v1')))

# Importer la fonction à tester
from app.api.v1.alert import recommandation_vetements

def test_performance():
    # Ville pour laquelle vous souhaitez tester la fonction
    city = "Paris"
    
    # Mesure du temps d'exécution pour la ville
    start_time = time.time()
    message = recommandation_vetements(city)
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Affichage des résultats
    print(f"Ville: {city}")
    print(f"Recommandation: {message}")
    print(f"Temps d'exécution: {execution_time:.6f} secondes")
    print("-" * 50)
    
    # Assertion pour vérifier que le message retourné n'est pas None
    assert message is not None, f"Aucune recommandation n'a été retournée pour {city}"

# Condition pour exécuter le test directement avec pytest
if __name__ == "__main__":
    test_performance()
