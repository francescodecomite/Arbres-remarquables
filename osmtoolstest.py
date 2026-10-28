import pyrosm
import matplotlib

available_places = pyrosm.data.available
print(available_places.keys())
# print('Leeds available from providers:','Leeds' in available_places['cities'])
