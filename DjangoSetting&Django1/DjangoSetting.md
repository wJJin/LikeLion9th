$ - 사용자의 명령 입력을 기다리는 표시 (prompt)
~ - 물결은 home directory
. - working directory (작업중인 현재 위치)
/ - root directory (모든 디렉터리의 시작점)
.. - 상위 디렉토리 (상대적인 위치)

절대 경로: root directory부터 모든 경로를 작성한 것
상대 경로: root가 아닌 특정 directory(일반적으로 현재 위치)를 기준으로 작성 ex) ../sample/test.py

외워야 할 명령어
pwd: printworkingdirectory / 현재 위치를 알려준다.
man: manual / 명령어 설명서, man[알고 싶은 명령어]
ls: list / 디렉터리의 목록을 보여준다.
옵션a: 숨김파일까지 보여줌, 옵션 l:상세하게 보여줌, 옵션 F: 파일인지 디렉터리인지 알려줌
cd: changedirectory / 현재 위치(working directory)를 이동해줌, cd[이동하고 싶은 위치] 
clear: 터미널 청소기

옵션: "-"로 시작해서 영문 대소문자로 구성. 명령어의 기능을 구체화. 명령어에 따라 없을 수도 있다. ex> ls-l ls-a ls-al ls-la
인자: 명령어의 수행시 대상이 될 파일이나 디렉터리. 명령어에 따라 필요 없을 수도 있고 필수일 수도 있다. ex) cp[인자1][인자2]


history: 직전에 입력했던 명령어들을 보여줌
tab 버튼: 명령어나 디렉터리 자동완성

python -m venv [가상환경명]: 가상환경 만들기
source [가상환경명]/Script/activate: 가상환경 실행
pip install django: django 설치
django-admin startproject [프로젝트 이름]: django 프로젝트 만들기
cd로 만든 프로젝트 안으로 들어온 뒤
python manage.py runserver: django 서버 가동