# 🎞 Dubbing Project (TTS Programming) <img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>

> `Google TextToSpeech API`를 이용하여 텍스트를 한국어 음성 파일로 변환한 후 `moviepy`와 `ImageMagick`을 이용하여 영문 자막 생성 및 한국어 더빙이 된 영상을 만드는 프로젝트입니다.

## 구현 과정

* SSML을 통해 원본 동영상의 자막을 [ssmlTest.ssml](https://github.com/W00hyun-Kim/DubbingProject/tree/main/data) 파일로 만들어준다.
* Anaconda를 통한 가상환경을 만들어 google API활용해 ssml파일을 한국어 음성파일([output.mp3](https://github.com/W00hyun-Kim/DubbingProject/tree/main/data))로 변환해준다.   
* moviepy 라이브러리를 통해 한국어 음성파일과 원본 파일을 합쳐 새로운 파일([result.mp4](https://github.com/W00hyun-Kim/DubbingProject/tree/main/data))을 만든다.
* ImageMagick 라이브러리를 통해 합쳐준 영상과 자막파일([subtitle.srt](https://github.com/W00hyun-Kim/DubbingProject/tree/main/data))을 합쳐준다.
* 최종결과 [dubbingf.mp4](https://github.com/W00hyun-Kim/DubbingProject/tree/main/result)를 write해준다.


## 결과 영상

아래 영상은 화면 녹화 영상이기에 소리와 함께 듣기 위해서는 result directory에 dubbing_result.mp4를 실행하여 확인 부탁드립니다.

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/95575122/167306870-6af033c8-6a20-4a28-b37e-69a14be2c36b.gif)




## 정보

김우현 – [https://woohyun.tistory.com/](https://woohyun.tistory.com/) – woohyun9509@gmail.com

Apache License 2.0 라이센스를 준수하며 ``LICENSE``에서 자세한 정보를 확인할 수 있습니다.

