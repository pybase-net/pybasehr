import os
if os.name == 'nt':
    class PwdStruct():
        def __init__(self, pw_name, pw_uid, pw_dir, pw_shell):
            self._pw_name = pw_name
            self._pw_uid = pw_uid
            self._pw_dir = pw_dir
            self._pw_shell = pw_shell

        @property
        def pw_name(self):
            return self._pw_name
        
        @property
        def pw_uid(self):
            return self._pw_uid

        @property
        def pw_dir(self):
            return self._pw_dir
        
        @property
        def pw_shell(self):
            return self._pw_shell
        
    class Pwd():
        def getpwall(self):
            return [ PwdStruct(pw_name='misostack', pw_uid=1005, pw_dir='/users/misostack/home', pw_shell= '/usr/bin/bash')]
    pwd = Pwd()
else:
    import pwd

def fetch_users():
    users = []
    for user in pwd.getpwall():
        if user.pw_uid >= 1000 and 'home' in user.pw_dir:
            users.append({
              'name': user.pw_name,
              'id': user.pw_uid,
              'home': user.pw_dir,
              'shell': user.pw_shell,
            })
    return users

if __name__ == "__main__":
    users = fetch_users()    
    for user in users:
        print(user)