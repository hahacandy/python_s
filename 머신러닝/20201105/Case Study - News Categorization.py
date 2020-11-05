import os

def get_file_list(dir_name):
    return os.listdir(dir_name)

if __name__ == "__main__":
        dir_name = "news_data"
        file_list = get_file_list(dir_name)
        file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
        print(file_list)

