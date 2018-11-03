# Mash-up Django Study

## 진행방식

### 스터디 시작 전

- 예습 개발환경 세팅
  - Jupyter Notebook을 설치 후, 실습코드들을 실행
    - 구글에 검색시 운영체제별로 설치방법이 다양하게 나옴
  - 파이썬은 3.x버전을 사용, 가능하다면 최신 (3.7)버전을 사용
- 프로그래밍/파이썬 기본지식 (개개인이 아래 자료를 보고 각자 학습)
  **모든 코드는 손으로 직접 쳐보도록 한다 (눈으로 훑어만 보면 늘지 않습니다)**
  - [점프 투 파이썬](https://wikidocs.net/book/1)
  - [파이썬 코딩도장](https://dojang.io/course/view.php?id=7)
    - Unit 19, 21, 28, 31, 32, 33, 39, 40, 41, 46, 47은 하지 않아도 무관



### 스터디 준비사항

- 시스템 운영체제 변경 및 초기화
  시작시 개발환경 세팅에는 많은 시간이 소요되며, 윈도에서는 예상치 못한 오류를 많이 만납니다
  리눅스와 맥OS만 사용하도록 합니다
  **어떠한 경우에도 시스템은 초기화하고 오셔야합니다**
  - 맥북 사용자들은 하이시에라 또는 모하비 버전으로 시스템 초기화
    - 초기화 후, 터미널에서 `xcode-select --install` 미리 실행
  - 일반 노트북 사용자들은 우분투 리눅스 18.04버전으로 OS변경
- 파이썬 학습현황 체크
  - 파이썬 활용, 클래스와 인스턴스, 파일 입출력에 관한 과제가 나갈 예정입니다



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

