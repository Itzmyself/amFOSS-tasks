import os
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
import requests

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.w = None
        self.current_pokemon = None
        self.captured_pokemon = []

        self.setWindowTitle("Pokédex")
        self.setFixedSize(850, 500)

        # Background Label
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 850, 500)
        pixmap = QPixmap("../assets/landing.jpg")  # Path to your image
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        # Widgets
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 55, 200, 40)
        self.textbox.setStyleSheet("border: 1px solid #BA263E; font: 16px; font-family: 'Times New Roman', serif;")

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(40, 5, 600, 70)
        label1.setStyleSheet("font-family: 'Times New Roman', serif; font: bold 18px; color: #FFFFFF; padding: 10px;")

        # Buttons with hover effects
        self.enter_button = QPushButton("SEARCH", self)
        self.enter_button.setGeometry(50, 300, 160, 43)
        self.enter_button.clicked.connect(self.fetch_pokemon_data)
        self.enter_button.setStyleSheet(self.get_button_stylesheet())

        self.capture_button = QPushButton("CAPTURE", self)
        self.capture_button.setGeometry(50, 350, 160, 43)
        self.capture_button.clicked.connect(self.capture_pokemon_trigger)
        self.capture_button.setStyleSheet(self.get_button_stylesheet())

        self.display_button = QPushButton("DISPLAY", self)
        self.display_button.setGeometry(50, 400, 160, 43)
        self.display_button.clicked.connect(self.show_captured_pokemon)
        self.display_button.setStyleSheet(self.get_button_stylesheet())

        self.label_name = QLabel(self)
        self.label_name.setGeometry(500, 242, 400, 40)
        self.label_name.setStyleSheet("font-family: 'Times New Roman', serif; font-size: 18px; color: #FFFFFF; padding: 10px;")

        self.label_types = QLabel(self)
        self.label_types.setGeometry(500, 264, 400, 40)
        self.label_types.setStyleSheet("font-family: 'Times New Roman', serif; font-size: 18px; color: #FFFFFF; padding: 10px;")

        self.label_abilities = QLabel(self)
        self.label_abilities.setGeometry(500, 286, 400, 40)
        self.label_abilities.setStyleSheet("font-family: 'Times New Roman', serif; font-size: 18px; color: #FFFFFF; padding: 10px;")

        self.label_stats = QLabel(self)
        self.label_stats.setGeometry(500, 300, 400, 200)
        self.label_stats.setStyleSheet("font-family: 'Times New Roman', serif; font-size: 18px; color: #FFFFFF; padding: 10px; ")

        self.label_image = QLabel(self)
        self.label_image.setGeometry(500, 10, 250, 250)
        self.label_image.setAlignment(Qt.AlignCenter)
        self.label_image.setScaledContents(True)
        

    def get_button_stylesheet(self):
        return """
            QPushButton {
                background-color: black;  /* black background */
                color: white;                /* Text color (white) */
                border: 1px solid #BA263E;     /* Red border */
                font-family: 'Times New Roman', serif;
                padding: 10px;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #BA263E;     /* Red fill on hover */
                color: black;                  /* black text on hover */
            }
            QPushButton:pressed {
                background-color: #880808;     /* Darker Red on press */
            }
        """

    def fetch_pokemon_data(self):
        pokemon_name = self.textbox.text().strip().lower()
        if not pokemon_name:
            print("Please enter a Pokémon name.")
            return

        # Hide the background image
        self.background_label.hide()

        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                self.display_pokemon_data(data)
            else:
                print(f"Pokémon {pokemon_name} not found.")

                self.prompt_window = Notfound(pokemon_name)
                self.prompt_window.show()

        except requests.RequestException as e:
            print(f"Error fetching Pokémon data: {e}")

    def display_pokemon_data(self, data):
        name = data['name'].capitalize()
        types = ", ".join([t['type']['name'] for t in data['types']])
        abilities = ", ".join([a['ability']['name'] for a in data['abilities']])
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        image_url = data['sprites']['other']['official-artwork']['front_default']

        # Display information
        
        self.label_name.setText(f"Name: {name}")
        self.label_types.setText(f"Types: {types}")
        self.label_abilities.setText(f"Abilities: {abilities}")
        stats_text = "<br>".join([f"{key}: {value}" for key, value in stats.items()])
        self.label_stats.setText(f"Stats:<br>{stats_text}")

        # Fetch and display the image (if available)
        if image_url:
            image_data = requests.get(image_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.label_image.setPixmap(pixmap)
            self.current_pokemon = (name, image_url)
        else:
            self.label_image.setPixmap(QPixmap())  # Clear image
            print("No official artwork available for this Pokémon.")
            self.current_pokemon = None

    def capture_pokemon_trigger(self):
        if self.current_pokemon:
            name, image_url = self.current_pokemon
            try:
                # Create directory if it doesn't exist
                capture_dir = "captured_pokemon"
                os.makedirs(capture_dir, exist_ok=True)

                # Save image in the directory
                image_data = requests.get(image_url).content
                image_path = os.path.join(capture_dir, f"{name}.png")
                with open(image_path, "wb") as file:
                    file.write(image_data)
                self.captured_pokemon.append({"name": name, "image_path": image_path})
                print(f"Captured Pokémon: {name}")
                self.prompt_window = PromptWindow(name)
                self.prompt_window.show()

            except requests.RequestException as e:
                print(f"Error saving Pokémon image: {e}")
        else:
            print("No Pokémon to capture.")

    def show_captured_pokemon(self):
        if self.captured_pokemon:
            self.captured_window = CapturedPokemonWindow(self.captured_pokemon)
            self.captured_window.show()
        else:
            print("No Pokémon captured yet.")


class CapturedPokemonWindow(QWidget):
    def __init__(self, pokemon_list):
        super().__init__()
        self.setFixedSize(500, 500)
        self.layout = QVBoxLayout()

        for pokemon in pokemon_list:
            label = QLabel(pokemon['name'])
            image_label = QLabel()
            pixmap = QPixmap(pokemon['image_path'])
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)

            self.layout.addWidget(label)
            self.layout.addWidget(image_label)

        self.setLayout(self.layout)

class PromptWindow(QWidget):
    def __init__(self,name):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Pokémon Captured!")
        
        # Create a label widget
        message = f"CONGRATULATIONS! \nYou have successfully caught {name}!"
        label = QLabel(message, self)
        label.setAlignment(Qt.AlignCenter)  # Center align the label text
        label.setStyleSheet("font: bold 18px ; font-family: 'Times New Roman', serif;")
        label.setGeometry(50, 100, 300, 50)

        # Auto-close after 5 seconds
        QTimer.singleShot(5000, self.close)

class Notfound(QWidget):
    def __init__(self,pokemon_name):
        super().__init__()
        self.setFixedSize(300, 200)
        self.setWindowTitle("Error")
        
        # Create a label widget
        message = f"{pokemon_name} not found!"
        label = QLabel(message, self)
        label.setAlignment(Qt.AlignCenter)  # Center align the label text
        label.setStyleSheet("font: bold 18px ; font-family: 'Times New Roman', serif;")
        label.setGeometry(25, 75, 200, 50)

        # Auto-close after 5 seconds
        QTimer.singleShot(5000, self.close)

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
