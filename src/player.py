import pygame

# Inicializa o mixer de áudio, que é responsável por carregar e reproduzir sons
pygame.mixer.init()

class MusicPlayer:
    """
    A classe MusicPlayer encapsula as funcionalidades de áudio.
    """
    def __init__(self):
        """
        Método que configura a inicialização
        """
        pass

    def load(self, file_path):
        """
        Função que recebe o caminho completo do arquivo de áudio e carrega o arquivo de música no mixer. Preparando o arquivo para reprodução.
        """

        # Carregando o arquivo de audio no mixer
        pygame.mixer.music.load(file_path)

    def play(self):
        """
        Inicia a reprodução do arquivo de audio carregado no mixer
        """
        pygame.mixer.music.play()

    def stop(self):
        """
        Para a reprodução atual, se nenhuma música estiver sendo reproduzida, o método não faz nada.
        """
        pygame.mixer.music.stop()