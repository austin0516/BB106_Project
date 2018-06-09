#MAIN
import csv  
import pymysql  


def main():
    conn = pymysql.connect(host='localhost',port=3306,user='test',passwd='test',db='test',charset='utf8')
    print(conn)

    cur = conn.cursor()  
    print(cur)  
    with open('analyse.csv') as csvfile:  
        sp = csv.DictReader(csvfile)  
        for row in sp:  
    #         sql = '''insert into table_name (Method) values ("aaa");''' 
            sql = '''insert into text_mining_table (title,url,picture) values ("%s","%s","%s");'''%(str(row['title']),str(row['url']),str(row['picture'])) 
            print(sql)  
            cur.execute(sql)  
    conn.commit()   
    cur.close()
    
    

if __name__=="__main__":
    main()