services = {
'id' : 1,
'name': 'desarrollo de app',
'precio': 400,
'tools': ["laptop","servidores","pizarra digital"]
}
print('id' in services)
#insertar valor en el id
services['id'] = 2
services.pop('id')
services['tools'].append ('celular')
#imprimir diciconario
print(services.items())
print(services.keys())
print(services.values())

print(services['name'])

print(services['tools'][1])

pasajero = [
{'id' : 1,'nombre': 'Cristian','address': 'avenidad','fecha': '2023-02-11'}
{'id' : 2,'nombre': 'Edison','address': 'calderon','fecha': '2023-02-11'}
{'id' : 3,'nombre': 'carlos','address': 'comite del pueblo','fecha': '2023-02-11'}
{'id' : 4,'nombre': 'josue','address': 'asolanda','fecha': '2023-02-11'}
{'id' : 5,'nombre': 'David','address': 'san rafael','fecha': '2023-02-11'}
]

