from avtomobil.avto import Avto

avto1 = Avto('GM', 'Malibu', 'qora', 2020, 30000, 1000)

print(f'{avto1.get_km()} km')
print(f'ID: {avto1.get_id()}')

avto1.add_km(100)
print(f'{avto1.get_km()} km')

print(f'Avtomobillar soni: {Avto.get_num_avto()}')
