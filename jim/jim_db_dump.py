#MAIN
import csv  
import pymysql

def main():
    conn = pymysql.connect(host='localhost',port=3306,user='test',passwd='test',db='test')  
    print(conn)  
    cur = conn.cursor()  
    print(cur)  
    with open('ETF_liu.csv') as csvfile:  
        sp = csv.DictReader(csvfile)  
        for row in sp:  
    #         sql = '''insert into new_etf (Method) values ("aaa");''' 
            sql = '''insert into liu_table (Stockcode,Method,Fitnessvalue_withoutGA,Fitnessvalue_withGA,Picture_withGA,GA_picture) values ("%s","%s",%f,%f,"%s","%s");'''%(str(row['Stockcode']),str(row['Method']),float(row['Fitnessvalue_withoutGA']),float(row['Fitnessvalue_withGA']),str(row['Picture_withGA']),str(row['GA_picture'])) 
            print(sql)  
            cur.execute(sql)  
    conn.commit()   
    cur.close()  
    

if __name__=="__main__":
    main()
