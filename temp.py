from decouple import config
key_env  =config('SECRET_ACCESS_KEY')
id_env  =config('ACCESS_KEY_ID')
print(key_env,id_env)