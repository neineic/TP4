import os

GOOD_COMMIT = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
BAD_COMMIT = "c1a4be04b972b6c17db242fc37752ad517c29402"

# Lancer git bisect entre le mauvais et le bon commit
os.system(f"git bisect start {BAD_COMMIT} {GOOD_COMMIT}")

# Tester chaque commit avec la commande de tests
os.system("git bisect run python manage.py test")

# Revenir à l'état normal du repo à la fin
os.system("git bisect reset")
