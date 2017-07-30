import sqlite3
conn=sqlite3.connect('experiment5')
curs=conn.cursor()
cmd="Create table books(book_id int not null primary key, title_id int(20), location char(3), genre char(4), foreign key(title_id) references titles(title_id))"
curs.execute(cmd)
cmd="create table titles(title_id int not null primary key,title char(20), isbn char(20), pub_id int(3), pub_year int(20), foreign key(pub_id) references publishers(pub_id))"
curs.execute(cmd)
cmd="create table publishers(pub_id int not null primary key, name char(20), streetad char(20), suitenum int(3), zipcode_id int(4), foreign key(zipcode_id) references zipcodes(zipcode_id))"
curs.execute(cmd)
cmd="create table zipcodes(zipcode_id int not null primary key, city char(20), state char(20), zipcode int(5))"
curs.execute(cmd)
cmd="create table authorstitle(authortitle_id int not null primary key, author_id int(4), title_id int(20), foreign key(title_id) references titles(title_id), foreign key(author_id) references authors(author_id))"
curs.execute(cmd)
cmd="create table authors(author_id int not null primary key, firstname char(20), middle char(20), last char(20))"
curs.execute(cmd)
curs.execute("insert into authors values(1,'akhil','kumar','jain')")
curs.execute("insert into authorstitle values(1,1,1)")
curs.execute("insert into zipcodes values(1,'gwalior','mp',487)")
curs.execute("insert into publishers values(1,'rahul','gst',2,603)")
curs.execute("insert into titles values(1,'god','hhe',90,2015)")
ch=int(input("enter choice 1. for insertion. 2.updation. 3.deletion 4.quit"))
while(ch!=4):      
    if(ch==1):
        id=int(input("enter books_id\n"))
        tid=int(input("enter title_id\n"))
        loc=(input("enter location\n"))
        gen=(input("enter char for genre\n"))
        curs.execute("insert into books values(?,?,?,?)",[id,tid,loc,gen])
    elif(ch==2):
        o=int(input("enter old book_id\n"))
        n=int(input("enter new book_id\n"))
        curs.execute("update books set book_id=? where book_id=?",[n,o])
    elif(ch==3):
        o=int(input("enter book_id\n"))
        curs.execute("delete from books where book_id=?",[o])
    elif(ch==4):
        break
    ch=int(input("enter choice 1. for insertion. 2.updation. 3.deletion 4.quit"))
curs.execute("select * from books")
m=curs.fetchall()    
print(m)
    
       
       
       
       

