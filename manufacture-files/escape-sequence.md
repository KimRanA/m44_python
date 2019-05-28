#Escape sequence

- '\n' : LF(Line Feed) -> 주로 Unix 계통에서 개행을 쓸 때 사용
    커서에 위치를 그대로 두고
- '\r' : CR(Carriage Return) -> Max OS before x
    현재 위치에서 커서 위치를 맨 앞으로 옮김
- '\r\n' : CR + LF -> Windows

일반적으로는 '\n'과 '\r\n' 을 사용한다.

- '\t' : 탭 문자
- '\\' : 백슬레쉬(\)를 쓰기 위해서
- '\'' , '\"' : 따옴표(' or ")를 쓰기 위해서