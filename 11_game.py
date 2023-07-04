








def message_creator(text):
   # Escribe tu solución 👇
    message_creator = {
        'computadora': 'con mi computadora puedo programar usando python',
        'celular': 'en mi celular puedo aprender usando la app de platzi',
        'cable_hdmi': 'con este cable vere mis clases de platzi mejor'}
    
    if text in message_creator  :
       return  message_creator[text]
    
text = 'computadora'
response = message_creator(text)
print(response)