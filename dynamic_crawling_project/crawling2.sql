-- crawling2.sql
-- ���� ��ũ�Ѹ� ��� ����� ���̺� ��ũ��Ʈ


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

COMMENT ON COLUMN TOUR.TOUR_ID IS '����';
COMMENT ON COLUMN TOUR.title IS '��ǰ��';
COMMENT ON COLUMN TOUR.price IS '��ǰ����';
COMMENT ON COLUMN TOUR.img IS '�����';
COMMENT ON COLUMN TOUR.link IS '��ũURL';
COMMENT ON COLUMN TOUR.tperiod IS '����Ⱓ';
COMMENT ON COLUMN TOUR.dperiod IS '��߱Ⱓ';
COMMENT ON COLUMN TOUR.content IS '��ǰ����';

CREATE SEQUENCE SEQ_TOUR
START WITH 1
INCREMENT BY 1
NOCYCLE
NOCACHE
NOMAXVALUE;
