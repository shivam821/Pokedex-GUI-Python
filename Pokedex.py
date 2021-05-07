#Pokedex 
# import Pillow - Python Imaging Library
# import urllib3 - HTTP client for Python

#Libraries:
import pypokedex
import PIL.Image,PIL.ImageTk
import tkinter as tk 
import urllib3
from io import BytesIO


# pokemon = pypokedex.get(name = "pikachu")
# print(pokemon.name)
# print(pokemon.dex)
# print(pokemon.types)
# print(pokemon.sprites.front.get("default"))

#GUI
window = tk.Tk()
window.iconbitmap(r'C:\Users\Shivam\Desktop\idlex-1.18\pokeball.ico')
window.geometry("700x600")
window.title("Pokedox")
window.config(padx = 10, pady = 10)

tittle_label = tk.Label(window, text = "Pokemon")
tittle_label.config(font=("Arial",32))
tittle_label.pack(padx=10,pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10,pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial",20))
pokemon_information.pack(padx=10,pady=10)

pokemon_information_1 = tk.Label(window)
pokemon_information_1.config(font=("Arial",20))
pokemon_information_1.pack(padx=10,pady=10)

pokemon_information_2 = tk.Label(window)
pokemon_information_2.config(font=("Arial",20))
pokemon_information_2.pack(padx=10,pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial",20))
pokemon_image.pack(padx=10,pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name = text_id_name.get(1.0,"end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET',pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image = img )
    pokemon_image.image = img

    pokemon_information.config(text=f"Poke Dex Number:{pokemon.dex}".title())
    pokemon_information_1.config(text=f"Pokemon Name :{pokemon.name}".title())
    #pokemon_information_2.config(text=" - ".join([t for t in pokemon.types]))
    pokemon_information_2.config(text=f"Pokemon Type :{pokemon.types}".title())





label_id_name = tk.Label(window,text="Enter ID or Name")
label_id_name.config(font=("Arial",20))
label_id_name.pack(padx=10,pady=10)

text_id_name = tk.Text(window,height=1)
text_id_name.config(font=("Arial",20))
text_id_name.pack(padx=10,pady=10)

btn_laod = tk.Button(window,text="Load Pokemon", command = load_pokemon)
btn_laod.config(font=("Arial",20))
btn_laod.pack(padx=10,pady=10)

window.mainloop()