import pickle

class IntegerListManager:
    def __init__(self, filename='data.pkl'):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self):
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def run(self):
        user_input = input('Zadej čísla: ')
        int_list = [int(item) for item in user_input.split()]
        filename = 'data.pkl'
        self.save_data(int_list)
        loaded_list = self.load_data()
        print(f'Načtena data ze souboru: {loaded_list}')

if __name__ == '__main__':
    manager = IntegerListManager()
    manager.run()