import mysql.connector
import codecs

class DBConnection:
    def __init__(self): #constructor
        self.mydb = mysql.connector.connect(host="192.168.64.3",user="22TinnaM",password="test",database="test")
        self.mycursor = self.mydb.cursor()

    def getAllTag(self):
        self.list = []
        self.sql = "select * from tags"
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchall()
        for i in self.results:
            self.list.append(i)
        return self.list
    def addtag(self,tagname_info):
        self.sql = "insert into tags (tagname) VALUES ('" + tagname_info + "')"
        self.mycursor.execute(self.sql)
        self.mydb.commit()
    def deletetag(self, tagid_info):
        self.sql = "delete from tags where tagid = '" + tagid_info + "'"
        self.mycursor.execute(self.sql)
        self.mydb.commit()
    def updatetag(self, tagid_info, tagname_info):
        self.sql = "update tags set tagname = '" + tagname_info + "'  where tagid = '" + tagid_info + "'"
        self.mycursor.execute(self.sql)
        self.mydb.commit()
    def getAllTest(self):
        self.list = []
        self.sql = "select * from mytests"
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchall()
        for i in self.results:
            self.list.append(i)
        return self.list
    def deleteTest(self, testid_info):
        self.sql = "delete from mytests where testid = '" + testid_info + "'"
        self.mycursor.execute(self.sql)
        self.mydb.commit()
    def getAllquestion(self):
        self.sql = "select * from newpastpaper"
        # print(self.sql)
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchall()
        self.list = []
        for i in self.results:
            self.list.append(i)
        return self.list
    def getLevel_paperstyle_topic_sub(self, paperlevel,selecttopic, selectsubtopic, paperstyle):
        self.tempstr = ""
        self.tempstr2=""
        if len(selecttopic) <= 0:
            self.tempstr = "'" + self.tempstr + "'"
        else:
            for i in range (len(selecttopic)):
                if i == len(selecttopic)-1:
                    self.tempstr = self.tempstr + "'" + selecttopic[i]+ "'"
                else:
                    self.tempstr = self.tempstr + "'" + selecttopic[i]+ "',"
        if len(selectsubtopic)<= 0:
            self.tempstr2="'"+self.tempstr2+"'"
        else:
            for i in range (len(selectsubtopic)):
                if i == len(selectsubtopic)-1:
                    self.tempstr2 = self.tempstr2 + "'" + selectsubtopic[i]+ "'"
                else:
                    self.tempstr2 = self.tempstr2 + "'" + selectsubtopic[i]+ "',"

        self.sql="select * from newpastpaper where level in ('" + paperlevel +"') and topic in (" + self.tempstr + ") and subtopic in (" + self.tempstr2 + ") and Exam_paper_style in ('" + paperstyle + "')"
        # print(self.sql)
        self.mycursor.execute(self.sql)
        self.results=self.mycursor.fetchall()
        self.list=[]
        for i in self.results:
            self.list.append(i)
        return self.list
    def getLevel_paperstyle_topic(self, paperlevel, selecttopic, paperstyle):
        self.tempstr = ""
        if len(selecttopic) <= 0:
            self.tempstr = "'" + self.tempstr + "'"
        else:
            for i in range(len(selecttopic)):
                if i == len(selecttopic) - 1:
                    self.tempstr = self.tempstr + "'" + selecttopic[i] + "'"
                else:
                    self.tempstr = self.tempstr + "'" + selecttopic[i] + "',"
        self.sql = "select * from newpastpaper where level in ('" + paperlevel + "') and topic in (" + self.tempstr + ") and Exam_paper_style in ('" + paperstyle + "')"
        # print(self.sql)
        self.mycursor.execute(self.sql)
        self.results = self.mycursor.fetchall()
        self.list = []
        for i in self.results:
            self.list.append(i)
        return self.list
    def getPaperstyle_topic(self,selecttopic, paperstyle):
        self.tempstr = ""
        if len(selecttopic) <= 0:
            self.tempstr = "'" + self.tempstr + "'"
        else:
            for i in range (len(selecttopic)):
                if i == len(selecttopic)-1:
                    self.tempstr = self.tempstr + "'" + selecttopic[i]+ "'"
                else:
                    self.tempstr = self.tempstr + "'" + selecttopic[i]+ "',"

        self.sql="select * from newpastpaper where topic in (" + self.tempstr + ") and Exam_paper_style in ('" + paperstyle + "')"
        # print(self.sql)
        self.mycursor.execute(self.sql)
        self.results=self.mycursor.fetchall()
        self.list=[]
        for i in self.results:
            self.list.append(i)
        return self.list
    def getTestnames(self):
        self.sql="select * from mytests"
        self.mycursor.execute(self.sql)
        self.results=self.mycursor.fetchall()
        self.list=[]
        for i in self.results:
            self.list.append(i[1])
        return tuple(self.list)
    def getQid(self, question):
        # tempstr=""
        # if len(question) <= 0:
        #     self.tempstr = "'" + self.tempstr + "'"
        # else:
        #     for i in range (len(question)):
        #         if i == len(question)-1:
        #             self.tempstr = self.tempstr + "'" + question[i]+ "'"
        #         else:
        #             self.tempstr = self.tempstr + "'" + question[i]+ "',"

        self.sql = "select No from newpastpaper where question in (" + question + ")"
        print(self.sql)
