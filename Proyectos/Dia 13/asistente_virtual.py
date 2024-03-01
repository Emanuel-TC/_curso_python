# import pyttsx
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro micrófno y devolver el audo como texto
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el micrógno
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzóla grabación
        print("Ya puedes hablar")

        # guardar lo que escuche
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-mx')

            # prueba de que pudo ingresar
            print(f"Dijiste {pedido}")

            # devolver pedido
            return pedido
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print("Ups, no entendí")

            # devolver el error
            return "sigo esperando"
        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendió el audio
            print("Ups, no hay servicio")

            # devolver el error
            return "sigo esperando"
        # error inesperado
        except:

            # prueba de que no comprendió el audio
            print("Ups, algo ha salido mal")

            # devolver el error
            return "sigo esperando"

transformar_audio_en_texto()
