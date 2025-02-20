import unittest
import os
import tempfile
from src.navigator import list_aiff_files


class TestNavigator(unittest.TestCase):
    def setUp(self):
        """
        Configura um diretório temporário para os testes
        """
        self.test_dir = tempfile .TemporaryDirectory()
        self.create_test_files()

    
    def create_test_files(self):
        """
        Cria arquivos de teste no diretório temporário
        """
        self.files = [
            "test1.aiff",
            "test2.aiff",
            "not_aiff.mp3",
            "random.txt"
        ]

        for file in self.files:
            with open(os.path.join(self.test_dir.name, file), 'w') as f:
                f.write("test")  # Criando arquivos vazios para testar


    def test_list_aiff_files(self):
        """
        Testa se apenas os arquivos .aiff são listados 
        """

        expected_files = [
            os.path.join(self.test_dir.name, "test1.aiff"),
            os.path.join(self.test_dir.name, "test2.aiff")
        ]

        result = list_aiff_files(self.test_dir.name)

        self.assertCountEqual(result, expected_files)  # Verifica se listas contêm os mesmos elementos


    def tearDown(self):
        """
        Remove o diretório temporário após os testes
        """
        self.test_dir.cleanup()

    
if __name__ == '__main__':
    unittest.main()