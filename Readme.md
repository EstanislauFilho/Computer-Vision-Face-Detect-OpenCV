# Detecção de Faces com OpenCV e Python

Este projeto conciste na criação de scripts em python capazes de fazer a detecção de faces em imagens ou em streaming por meio de uma Webcam. Para desenvolvimento deste projeto utilizou-se a biblioteca OpenCV e a linguagem de programação Python.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Computer-Vision-Face-Detect-OpenCV/master/Imagens/faces_detected.png)


## Iniciando o Projeto

As instruções a seguir permitirá que você possa executar, desenvolver e contribuir para o projeto em questão. Siga todas as etapas a seguir para executar o projeto de Detecção Facial utilizando a biblioteca OpenCV e a linguagem de programação Python.

### Pré-requisitos

Para executar os scripts em Python presentes nesse projeto, você precisa instalar em sua máquina os seguintes componentes:

```
Python 3.0 ou superior.

IDE de sua preferência.

OpenCV+contrib.
```

## Execução e Testes

Para executar e testar os scripts face_detect_image.py e face_detect_webcam.py, você inicialmente deve abri-los em seu ambiente de desenvolvimento em Python.

### Executando o face_detect_image.py

Esse script em python irá fazer a detecção facial de pessoas em uma imagem do tipo jpg. Para esse experimento utilizou-se a imagem '''scientists.jpg''' presente na pasta '''Imagens'''. Para a correta detecção de faces foi nescessário determinar os parâmetros '''scaleFactor''', '''minSize''' e '''minNeighbors''' na função '''detectMultiScale'''. Para testa-lo basta executá-lo na própria IDE.

Outra forma de executar o script é via terminal, pelo seguinte comando: 

```
sudo python3 face_detect_image.py
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

