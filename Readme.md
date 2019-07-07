# Face Detection with OpenCV and Python

This project concerns the creation of python scripts capable of detecting faces in images or in streaming through a Webcam. For the development of this project, the OpenCV library and the Python programming language were used.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Computer-Vision-Face-Detect-OpenCV/master/Imagens/faces_detected.png)


## Starting the Project

The following instructions will allow you to run, develop and contribute to the project in question. Follow all the steps below to run the Facial Detection project using the OpenCV library and the Python programming language.

### Prerequisites

To run the scripts in  python present in this project, you need to install the following components on your machine:

```
Python 3.0 or higher version.

OpenCV+Contrib.
```

## Execution and Testing

To run and test the face_detect_image.py and face_detect_webcam.py scripts, you should initially open them in your Python development environment.

### Executando o face_detect_image.py

Esse script em python irá fazer a detecção facial de pessoas em uma imagem do tipo jpg. Para esse experimento utilizou-se a imagem "scientists.jpg" presente na pasta "Imagens". Para a correta detecção de faces foi nescessário determinar os parâmetros "scaleFactor", "minSize" e "minNeighbors" na função "detectMultiScale". Para testa-lo basta executá-lo pela própria IDE.

Outra forma de executar o script é via terminal, pelo seguinte comando: 

```
sudo python3 face_detect_image.py
```

### Executando o face_detect_webcam.py

Esse script em python tem como finalidade fazer a detecção facial em streming através de uma webcam. Para testa-lo basta  executá-lo pela própria IDE. 


Outra forma de executar o script é via terminal, pelo seguinte comando:

```
sudo python3 face_detect_webcam.py
```

## Desenvolvido com

* [OpenCV](https://opencv.org/) - Biblioteca de visão computacional desenvolvidade pela Intel em 1999;
* [Python Software Foundation](https://maven.apache.org/) - LIguagem programação;
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE utilizada para desenvolvimento dos scrpts.

## Contribuindo

Por favor, leia Contributing.md para detalhes sobre o processo para enviar pedidos de pull para o desenvolvedor.

## Versão

Para as versões disponíveis, consulte as tags neste repositório. 

## Autores

* **Estanislau de Sena Filho** - *Computer Engineering Student at* [CEFET-MG](http://www.cefetmg.br/)

## Licença

Este não é um projeto licenciado. Sua finalidade é única excluisiva para estudo e aprendizagem sobre visão computacional.

## Agradecimentos

* Jones Granatyr e Gabriel Alves


