-- 크롤링스크립트.sql
-- 네이버 영화상영 정보 제공 페이지 크롤링 결과 저장용 테이블 스크립트

-- Movie 객체 정보 저장용 테이블 만들기
-- 테이블명 : movie
-- 객체 필드명과 테이블 컬럼명 일치시킴(__ 제외함)
-- rank : pk, 나머지 컬럼은 not null
-- 컬럼 comment 지정
create table movie (
    title varchar2(100) not null,
    star_point NUMBER(7,2) not null,
    age_grade varchar2(30),
    rank NUMBER CONSTRAINT PK_MOVIE_RANK PRIMARY KEY
);
DROP TABLE MOVIE;

COMMENT ON COLUMN MOVIE.TITLE IS '영화제목';
COMMENT ON COLUMN MOVIE.star_point IS '평점';
COMMENT ON COLUMN MOVIE.age_grade IS '관람가능 제한 나이';
COMMENT ON COLUMN MOVIE.rank IS '순위';