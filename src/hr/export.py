import json

def to_json_file(export_file, users):
    json.dump(users, export_file, indent=4)
    export_file.close()

if __name__ == '__main__':
    import sys
    users = [{'name': 'misostack', 'id':1001}]
    to_json_file(sys.stdout, users)
    import os
    file_path = './tmp/users.json'
    os.makedirs('./tmp', exist_ok=True)
    file = open(file=file_path, mode='w', newline='')
    to_json_file(file, users)
