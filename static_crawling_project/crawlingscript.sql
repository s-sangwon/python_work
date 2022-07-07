-- ũ�Ѹ���ũ��Ʈ.sql
-- ���̹� ��ȭ�� ���� ���� ������ ũ�Ѹ� ��� ����� ���̺� ��ũ��Ʈ

-- Movie ��ü ���� ����� ���̺� �����
-- ���̺�� : movie
-- ��ü �ʵ��� ���̺� �÷��� ��ġ��Ŵ(__ ������)
-- rank : pk, ������ �÷��� not null
-- �÷� comment ����
create table movie (
    title varchar2(100) not null,
    star_point NUMBER(7,2) not null,
    age_grade varchar2(30),
    rank NUMBER CONSTRAINT PK_MOVIE_RANK PRIMARY KEY
);
DROP TABLE MOVIE;

COMMENT ON COLUMN MOVIE.TITLE IS '��ȭ����';
COMMENT ON COLUMN MOVIE.star_point IS '����';
COMMENT ON COLUMN MOVIE.age_grade IS '�������� ���� ����';
COMMENT ON COLUMN MOVIE.rank IS '����';