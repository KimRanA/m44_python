# GIT
## 기본 명령어
1. git 저장소 (repository) 초기화
  	***bash
  	git init*******

  ~~~bash
  $ git init
  ~~~

  - 원하는 폴더를 저장소로 만들게 되면, `git bash` 에서는 (master)라고 표기된다.
  - 그리고 숨김 폴더로 `.git/`이 생성이 된다.

2. 커밋할 목록에 담기(Staging Area)

   ~~~bash
   $ git add .
   ~~~

   - 현재 작업 공간(Working Directory / Tree) 의 변경사항을 커밋할 목록에 추가한다.(add)
   - 리눅스에서 현재 디렉토리(폴더)를 표기하는 방법으로, 현재 내 폴더에 있는 파일의 변경사항을 전부 추가한다.
   - 단일 파일만 추가하려면 git add "파일이름"
   - 폴더를 추가하려면 git add "폴더이름/"

3.  커밋하기

   ~~~bash
   $ git commit -m '_____'
   ~~~

   - 커밋을 할 때에는 해당하는 버전의 이력을 의미하는 메시지를 반드시 적어준다.
   - 메시지는 지금 버전을 쉽게 이해할 수 있도록 작성한다.
   - 커밋은 현재 코드의 상태를 스냅샷 찍는 것이다. (언제든지 되돌아 갈 수 있도록.)

4.  로그 확인하기

   ~~~bash
   $ git log
   
   commit 40d60443a1ed7120351d6ef5fc4d4b51c41a6fc3 (HEAD -> master)
   Author: KimRanA <triple3dimple@gmail.com>
   Date:   Fri May 24 10:45:08 2019 +0900
   
       <EB><A7><88><ED><81><AC><C3><AB><EB><AA><A8><EB><91><90> stage<EC><97><90> <EC><98><AC><EB><A6><AC><EA><B8><B0>
   
   commit b1662dc18075183b1450f0ab9bf70e5cb85f428c
   ~~~

   - 현재까지 커밋된 이력을 모두 확인할 수 있다.

5.  git 상태 확인하기

   ~~~bash
   $ git status
   ~~~

   - CLI(Command Line Interface) 현재 상태를 알기 위해 반드시 명령어를 통해 확인한다.
   - 커밋할 목록에 담겨 있는지, untracked 인지, 커밋할 내역이 있는지 등등 다양한 정보를 알려준다.

## 원격 저장소 활용하기

1. 원격 저장소(remote repository) 등록하기

   ~~~bash
   $ git remote add origin _____ 경로_____
   ~~~

   - 원격 저장소(romote)를 등록(add)한다. origin 이름으로 git hub 경로를.

   - 최초에 한번만 등록하면 된다.

   - 아래의 명령어로 현재 등록된 원격 저장소를 확인할 수 있다.

     ~~~bash
     $ git remote --v
     $ git remote --v
     orgin   https://github.com/KimRanA/m44_python.git (fetch)
     orgin   https://github.com/KimRanA/m44_python.git (push)
     origin  https://github.com/KimRanA/m44_python.git (fetch)
     origin  https://github.com/KimRanA/m44_python.git (push)
     ~~~

2. 원격 저장소에 올리기(push)

   ~~~bash
   $ git push origin master
   ~~~

   - git! 올려줘(push) origin이라는 이름의 원격저장소에 master 로!

3. 원격 저장소로부터 가져오기(pull)

   ~~~bash
   $ git pull origin master
   ~~~

   - push는 올리는 거고, pull은 가져오는 것임.

## 원격 저장소 복제(clone)하기

~~~bash
$ git clone _____경로_____
~~~

- 다운 받기를 원하는 폴더에서 git bash를 열고(우클릭 git bash) 위의 명령어를 입력한다.
- 경로는 github 에서 우측에 있는 초록색 버튼을 누르면 나타난다.

***