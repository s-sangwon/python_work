-- crawling2.sql
-- 동적 웹크롤링 결과 저장용 테이블 스크립트


DROP TABLE TOUR CASCADE CONSTRAINTS;

CREATE TABLE TOUR (
        TOUR_ID NUMBER,
        title VARCHAR2(300),
        price VARCHAR2(20) ,
        img  VARCHAR2(500)  ,
        link VARCHAR2(1000)         ,
        tperiod   VARCHAR2(100)       ,
        dperiod   VARCHAR2(100)      ,
        content   VARCHAR2(4000)                   

);

COMMENT ON COLUMN TOUR.TOUR_ID IS '순번';
COMMENT ON COLUMN TOUR.title IS '상품명';
COMMENT ON COLUMN TOUR.price IS '상품가격';
COMMENT ON COLUMN TOUR.img IS '썸네일';
COMMENT ON COLUMN TOUR.link IS '링크URL';
COMMENT ON COLUMN TOUR.tperiod IS '여행기간';
COMMENT ON COLUMN TOUR.dperiod IS '출발기간';
COMMENT ON COLUMN TOUR.content IS '상품설명';

CREATE SEQUENCE SEQ_TOUR
START WITH 1
INCREMENT BY 1
NOCYCLE
NOCACHE
NOMAXVALUE;
