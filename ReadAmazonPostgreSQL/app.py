import psycopg2

def execute_query():
     # define your db connection string
        conn = psycopg2.connect(dbname='postgres',
                               user='elevateuadmin',
                               password='elevateuadmin2023',
                               host='elevateu-dev.cpdi379tec7f.us-east-1.rds.amazonaws.com',
                               port='5432',
                               sslmode='require')
        try:
                # actual sql statement
                sql_query = "SELECT * FROM employees"
                cur = conn.cursor()
                # cursor to excute the above sql statement
                cur.execute(sql_query)
                results = cur.fetchall()
                print(results)
                cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
              print("no success", error)
        finally:
             if  cur is not None:
                     cur.close()
        print("end")

if __name__ == '__main__':
    execute_query()
