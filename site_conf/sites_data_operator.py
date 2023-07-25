import json
import pickle


def json_to_dat():
    with open("sites.json", "r") as f:
        all_dat = json.load(f)
        with open("sites.dat.new", 'wb') as wf:
            pickle.dump(all_dat, wf)


def data_to_json():
    with open("sites.dat", "rb") as f:
        all_data = pickle.load(f)
        with open("sites.json", "w") as wf:
            json.dump(all_data, wf, indent=4)


if __name__ == '__main__':
    # data_to_json()
    json_to_dat()
    # with open("sites.dat.new", "rb") as f:
    #     all = pickle.load(f)
    #     print(all)