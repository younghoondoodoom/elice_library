# 3기_도서관대출서비스_최영훈

## Azure: http://elice-kdt-3rd-vm-103.koreacentral.cloudapp.azure.com

## 사전 작업
    -전체 파일 구조 및 환경 구성
    -데이터 베이스 구성
    -데이터 베이스 초기화는 load_data.py에 구현되어있음.

## 0. 전체 관리
    -버튼 색 변경

## 1. 메인 페이지
    -_navbar.html, base.html 구성
    -메인 페이지 구성(이미지 첨부)
    -main 관련 구성은 main_view.py에 구성
    -대여하기 구현 완료(재고 없으면 빌릴 수 없다 구현)
    -책은 개인당 1종류당 1권씩만 빌릴 수 있는 기능 구현
    -페이지네이션 기능 추가
    -검색 기능 추가

## 2. 회원 관리
    -회원 관련 구성은 user_view.py에 구성
    -회원 가입, 로그인, 로그아웃 구현(email형식, 비밀번호 형식 구현 아직)
    -email형식, 비밀번호 형식 조건 구현. views/forms.py에 조건을 작성

## 3. 상세 페이지
    -책 상세 관련 구성은 detail_view.py에 구성
    -이미지, 상세 설명 등 책 상세 내용을 구현
    -댓글 기능 구현.(가장 빠른 댓글 맨 위로 위치 구현)
    -detail 페이지 안에서 이미지 띄우는거 관련해서 모르는거 생김.
    -대여하기 기능 추가

## 4. 반납 페이지
    -반납 관련 구성은 turn_view.py에 구성
    -이미지, 대여 일자, 반납 일자, 반납 버튼 구현
    -반납 기능 구현(재고가 +1 되고, 대여 기록에서 삭제)
    -검색 기능 추가
    
## 5. 대여 기록 페이지
    -대여 기록 페이지의 구성은 history_view.py에 구성
    -사용자가 지금까지 대여했던 기록을 historyinfo 테이블에 담아서 띄움.
    -재대여 기능 추가


# 사용 방법

## 0. requirement.txt 설치
    pip install -r requirements.txt

## 1. 데이터베이스 초기화 및 틀 형성
    python3 migration.py or python migration.py

## 2. 데이터베이스에 기본 데이터 삽입
    python3 load_data.py or python load_data.py

## 3. 본인의 환경 변수로 SECRET KEY와 DATABASE_URI 설정하기
    서버나 본인 로컬에 config.py를 만들어서 secret key, database_uri, config 설정을 등록한다.

## 4. 실행
    python3 app.py or python app.py
