import pickle

def save_data(data, filename):
    with open(filename, 'wb') as file:
        return pickle.dump(data, file)

def load_data(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main():
    user_input = input('Enter lists of integers: ')
    int_list = [int(item) for item in user_input.split()]

    filename = 'data.pkl'

    save_data(int_list, filename)

    loaded_list = load_data(filename)

    print('Data loaded from file: ', loaded_list)

if __name__ == '__main__':
    main()