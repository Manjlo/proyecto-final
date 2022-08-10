from models.movie import Movie
import json



def create_new_register(jsonfile , movie:Movie):
	with open(jsonfile, 'w') as f:
		data = json.load(f)
		data['movies'].append(movie.__dict__)
		json.dump(data, f)
		f.close()

	print(data)

