# Mash-up Django Study

## 안내사항

안녕하세요! Mash-Up 8기 Django 스터디입니다!

Django스터디 내용은 Mash-Up의 면접 합/불여부와 관계없이, 지원자 모두와 공유됩니다  
모임시간 및 장소 등은 별도의 카카오톡 방에서 공지되지만, 나머지 내용에 대해서는 아래 도구들을 사용합니다.

- [Slack) 스터디 소통 채널](mashup-django.slack.com)
- [GitHub) 스터디 중앙 저장소](https://github.com/mash-up-kr/8th-DjangoStudy)



## 스터디 진행

### 1번째 모임

- 운영방침 정하기
  - 지각, 결석 패널티
    - 지각
      - 10분이내: 1000원
      - ~1시간: 3000원
      - 1시간 뒤는 결석
    - 결석: 5000원
  - 매주 수업내용 정리 및 블로그에 공유
    - [1주차: 김승현](https://velog.io/@ssseungzz7/pyenv와-pyenv-virtualenv를-사용한-파이썬-개발-환경-구성하기-p3k15vjigb)
- 셸/파이썬 개발환경 설정
  - zsh, oh-my-zsh설치
  - pyenv설치, 파이썬 및 가상환경 설정
  - PyCharm에서 새 프로젝트 실행 및 사용할 Interpreter설정
- 다음주 숙제 설명
  - SQL
  - CSS선택자



### 2번째 모임

- 네이버 웹툰 크롤링 실습
- 2주차 정리 및 공유
  - 이미림, 김대윤
- 다음주 숙제
  - 크롤러 개선



### 3번째 모임

- DjangoGirls Tutorial



## 진행방식

### 스터디 시작 전

- 예습 개발환경 세팅
  - Jupyter Notebook을 설치 후, 실습코드들을 실행
    - 구글에 검색시 운영체제별로 설치방법이 다양하게 나옴
  - 파이썬은 3.x버전을 사용, 가능하다면 최신 (3.7)버전을 사용
- 프로그래밍/파이썬 기본지식 (개개인이 아래 자료를 보고 각자 학습)
  **모든 코드는 손으로 직접 쳐보도록 한다 (눈으로 훑어만 보면 늘지 않습니다!!!)**
  - [(추천도서) Try! Helloworld 파이썬](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791160501063&orderClick=LAG&Kc=)
    - 초보자가 보기에는 가장 괜찮았습니다
  - [점프 투 파이썬](https://wikidocs.net/book/1)
  - [파이썬 코딩도장](https://dojang.io/course/view.php?id=7)
    - 가장 어렵습니다
      - 모르는 문제가 있다면 일단 넘어가며 학습
    - Unit 19, 21, 28, 31, 32, 33, 39, 40, 41, 46, 47은 하지 않아도 무관



### 파이썬 과제

#### 1주차 (~ 9/15)

점프 투 파이썬 기준, 05-1 클래스 이전까지 공부한 JupyterNotebook내용을 제출
(다른 도서나 사이트를 사용할 경우, 클래스와 인스턴스가 나오기 전까지)  
[GitHub Gist](https://gist.github.com/) 에 내용을 정리, 링크를 제출

#### 2주차 (~ 9/22)

클래스와 인스턴스 연습문제



### 스터디 준비사항

- 파이썬 학습현황 체크
  - 파이썬 활용, 클래스와 인스턴스, 파일 입출력에 관한 과제가 나갈 예정입니다
- 시스템 운영체제 변경 및 초기화  
  시작시 개발환경 세팅에는 많은 시간이 소요되며, 윈도에서는 예상치 못한 오류를 많이 만납니다  
  리눅스와 맥OS만 사용하도록 합니다  
  **어떠한 경우에도 시스템은 초기화하고 오셔야합니다**  
  - 맥북 사용자들은 하이시에라 또는 모하비 버전으로 시스템 초기화 후, 아래 명령어 실행
    - 터미널에서 `xcode-select --install` 미리 실행
    - [brew설치](https://brew.sh/index_ko)
      - `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  - 일반 노트북 사용자들은 우분투 리눅스 18.04버전으로 OS변경(또는 파티션 분할하여 멀티부팅)  
    이후 아래 명령어들 실행하고 오세요
    - `sudo apt -y update`
    - `sudo apt -y dist-upgrade`
  - 공통사항으로, PyCharm CE(Community Edition)을 설치해오세요
    - https://www.jetbrains.com/pycharm/download/



### 스터디 커리큘럼

- 크롤링 프로젝트
  - 네이버 웹툰 크롤링
    - [requests](https://2.python-requests.org/en/master/)
    - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Django
  - (숙제) [SQL Tutorial](https://www.w3schools.com/sql/)
  - [DjangoGirls 튜토리얼](https://tutorial.djangogirls.org/ko/)
  - DB모델 구현
    - 필드의 종류
    - 테이블 간 관계 구현
  - Admin 커스터마이징
  - ORM
    - 크롤링한 데이터를 Django모델을 사용해 DB에 저장
- DRF
  - [튜토리얼](https://www.django-rest-framework.org/tutorial/quickstart/)
  - 크롤링한 데이터를 제공하는 API제작
    - [Token로그인](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
  - 문서화
- 배포
  - 소스코드를 EC2에 업로드
  - screen을 사용해서 EC2에 runserver하기




## 프로젝트 점검사항

유저가 업로드하는 정적파일이 git에 포함되었는지 확인

- Django의 MEDIA_ROOT



pip package정보를 제공하는 requirements.txt파일이 있는지 확인

- pip freeze > requirements.txt

