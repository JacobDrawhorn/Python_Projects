import sqlite3

list_ = ['information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdx', 'myPhoto.jpg']

#create a data structure
conn = sqlite3.connect('example.db')
c = conn.cursor()

#Create table
c.execute('''Create TABLE if not exists server("sites")''')

#Insert links into table
def data_entry():
    for item in list_:
        c.execute("INSERT INTO server(sites) VALUES(?)", [item])
    conn.commit()

data_entry()  # ==> call the function

#query .txt
x = c.execute("SELECT * FROM server WHERE sites LIKE '%txt'")
rows = x
for row in rows:
    print(row)

conn.close()
