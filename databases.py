import sqlite3
conn=sqlite3.connect('demo123')
curs=conn.cursor()
cmd="Create table books(bookid int not null primary key, titleid int(20), location char(3), genre char(4), foreign key(titleid) references titles(titleid))"
curs.execute(cmd)
cmd="create table titles(titleid int not null primary key,title char(20), isbn char(20), pubid int(3), pubyear int(20), foreign key(pubid) references publishers(pubid))"
curs.execute(cmd)
cmd="create table publishers(pubid int not null primary key, name char(20), streetad char(20), suitenum int(3), zipcodeid int(4), foreign key(zipcodeid) references zipcodes(zipcodeid))"
curs.execute(cmd)
cmd="create table zipcodes(zipcodeid int not null primary key, city char(20), state char(20), zipcode int(5))"
curs.execute(cmd)
cmd="create table authorstitle(authortitleid int not null primary key, authorid int(4), titleid int(20), foreign key(titleid) references titles(titleid), foreign key(authorid) references authors(authorid))"
curs.execute(cmd)
cmd="create table authors(authorid int not null primary key, firstname char(20), middle char(20), last char(20))"
curs.execute(cmd)
curs.execute("insert into authors values(1,'sh','al','in')")
curs.execute("insert into authorstitle values(1,1,1)")
curs.execute("insert into zipcodes values(1,'sh','al',603)")
curs.execute("insert into publishers values(1,'sh','al',2,603)")
curs.execute("insert into titles values(1,'sh','al',90,2015)")
ch=int(input("enter choice 1. for insertion. 2.updation. 3.deletion 4.quit "))
while(ch!=4):      
    if(ch==1):
        id=int(input("enter books id"))
        tid=int(input("enter titleid"))
        loc=(input("enter location"))
        gen=(input("enter char for genre"))
        curs.execute("insert into books values(?,?,?,?)",[id,tid,loc,gen])
    elif(ch==2):
        o=int(input("enter old bookid"))
        n=int(input("enter new bookid"))
        curs.execute("update books set bookid=? where bookid=?",[n,o])
    elif(ch==3):
        o=int(input("enter bookid"))
        curs.execute("delete from books where bookid=?",[o])
    elif(ch==4):
        break
    ch=int(input("enter choice 1. for insertion. 2.updation. 3.deletion 4.quit"))
curs.execute("select * from books")
m=curs.fetchall()    
print(m)
    
       
       
       
       

