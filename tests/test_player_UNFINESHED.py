import unittest
from src.player import MusicPlayer
import pygame
import os


class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        """Configura o player para os testes."""
        self.player = MusicPlayer()
        self.test_file = os.path.join(os.path.dirname(__file__), "assets\\test_audio.aiff")

    def test_load(self):
        """Testa se o arquivo pode ser carregado sem erros."""
        try:
            self.player.load(self.test_file)
        except pygame.error as e:
            self.fail(f"Falha ao carregar o arquivo: {e}")

    def test_play(self):
        """Testa se o player pode iniciar a reprodução."""
        self.player.load(self.test_file)
        try:
            self.player.play()
        except pygame.error as e:
            self.fail(f"Falha ao reproduzir o arquivo: {e}")

    def test_stop(self):
        """Testa se o player pode parar a reprodução."""
        self.player.load(self.test_file)
        self.player.play()
        try:
            self.player.stop()
        except pygame.error as e:
            self.fail(f"Falha ao parar a reprodução: {e}")

    def tearDown(self):
        """Remove o arquivo de teste."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()