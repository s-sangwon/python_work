# notice_class
# notice 객체 정의 스크립트

class Notice():
    __no = 0;
    __title = ''
    __writer = ''
    __date = ''
    __content = ''
    __upfile = ''
    __readcount = 0;

    def __init__(self, no, title, writer, date, content, upfile, readcount):
        self.__no = no
        self.__title = title
        self.__writer = writer
        self.__date = date
        self.__content = content
        self.__upfile = upfile
        self.__readcount = readcount

    def __str__(self):
        return '공지번호 : {}, 공지제목 : {}, 작성자아이디 : {}, 등록날짜 {}\n공지내용 : {}\n' \
               '첨부파일 : {}, 조회수 : {}'.format \
            (self.__no, self.__title, self.__writer, self.__date,
             self.__content, self.__upfile, self.__readcount)
    def get_no(self):
        return self.__no
    def get_title(self):
        return self.__title
    def get_writer(self):
        return self.__writer
    def get_date(self):
        return self.__date
    def get_content(self):
        return self.__content
    def get_upfile(self):
        return self.__upfile
    def get_readcount(self):
        return self.__readcount