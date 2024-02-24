import requests

def obtener_Personajes(): 
    url = "https://api.disneyapi.dev/character"  # la URL de la API a utilizar
    respuesta = requests.get(url)  # hacemos la solicitud GET a nuestra URL API
    
    # Verificamos el estatus de la solicitud, una respuesta 200 significa éxito
    if respuesta.status_code == 200: 
        return respuesta.json()  # guardamos en un JSON
    else:
        return None 

def mostrar_personaje(personaje): 
    #Obtenemos el valor key, si esta existe nos devuelve esa información
    print("\nNombre:", personaje.get('name', 'Nombre no disponible'))
    
    films = ', '.join(personaje.get('films', []))
    # Devuelve el dato si existe, de lo contrario, muestra un mensaje indicando que no hay información
    print("Películas:", films if films else 'No hay información sobre películas') 
    
    tv_shows = ', '.join(personaje.get('tvShows', []))
    print("Series de TV:", tv_shows if tv_shows else 'No hay información sobre series de TV')
    
    video_games = ', '.join(personaje.get('videoGames', []))
    print("Videojuegos:", video_games if video_games else 'No hay información sobre videojuegos')
    
    park_attractions = ', '.join(personaje.get('parkAttractions', []))
    print("Atracciones en parques:", park_attractions if park_attractions else 'No hay información sobre atracciones en parques')
    
    allies = ', '.join(personaje.get('allies', []))
    print("Aliados:", allies if allies else 'No hay información sobre aliados')
    
    enemies = ', '.join(personaje.get('enemies', []))
    print("Enemigos:", enemies if enemies else 'No hay información sobre enemigos')
    
    print("URL de origen:", personaje.get('sourceUrl', 'URL no disponible'))
    
    print("Imagen:", personaje.get('imageUrl', 'Imagen no disponible'))


personajes = obtener_Personajes()  # Obtenemos los personajes de la API

if personajes is not None: 
    lista_personajes = personajes['data']
    
    # Iteramos sobre cada personaje en la lista, enumerando desde 1
    for i, personaje in enumerate(lista_personajes, start=1):
        print(f"\nPersonaje {i}:")
        mostrar_personaje(personaje)  # Mostramos el nombre y los detalles del personaje actual
        
        # Preguntamos al usuario si desea ver más personajes
        respuesta = input("\n¿Quieres ver más personajes? (s/n): ").strip().lower()
        if respuesta != 's':  # Si la respuesta no es 's', salimos del bucle
            break
else: 
    print("Hubo un error al usar la API")  # Si hubo un error al usar la API, mostramos un mensaje de error

