# -*- coding: utf-8 -*-
"""난생처음_실습_5장.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DQwmvJ4EDVubkPX1DOTxCAPSlklI8cJ8

# **5장. 데이터베이스**
"""

#데이터베이스(Database) : 여러 사람이 공동으로 검색하거나 운영할 수 있도록 연관된 데이터들을 구조적으로
#                        통합해서 컴퓨터에 저장한 데이터의 집합
#관계형 DBMS : 오라클 DB2, MS SQL, MySQL, SQL Server, 엑세스 등

#조인(JOIN)
# 1. 내부 조인 : 두 테이블의 공통 속성을 이용하여 테이블을 합하는 방법, ON 다음에 적은 조건과 일치하는
#               데이터를 중심으로 결과를 출력함. INNER를 생략해도 기본적으로 내부조인.
# 2. 외부 조인 : 내부조인과 달리 두 테이블 사이에 공통 속성이 없을 때 두 테이블을 하나로 합하는 방법
# - 왼쪽 외부조인(LEFT OUTER JOIN) : 왼쪽 테이블을 기준으로 해서 오른쪽 테이블의 해당 속성 값을 NULL
#                                   로 채워서 결과를 출력함.

# 부속 질의(Subquery)
# - 하나의 SQL문 안에 다른 SQL문이 들어있는 것.
# - 다른 테이블에서 가져온 데이터로 현재 테이블에 있는 정보를 찾거나 가공할 때 사용.

# NULL 검색
# 예시) SELECT * FROM 학생 WHERE 생년월일 IS NULL;
# NULL이 아닌 값 검색 : IS NOT NULL

# 집합 연산자
# - UNION : 합집합, 두 테이블을 수직으로 합하여 출력. 중복되는 값은 한 번씩만
# - INTERSECT : 교집합
# - EXCEPT : 차집합



















