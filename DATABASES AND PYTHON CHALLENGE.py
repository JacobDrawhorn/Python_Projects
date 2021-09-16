import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript("""
        CREATE TABLE Roster(
        Name,
        Species,
        IQ
    );

    insert into Roster(Name, Species, IQ)
    values (
        'Jean-Baptiste Zorg',
        'Human',
        122
    );

    insert into Roster(Name, Species, IQ)
    values (
        'Korben Dallas',
        'Meat Popsicle',
        100
    );

    insert into Roster(Name, Species, IQ)
    values (
        'Aknot',
        'Mangalore',
        -5
    );

    UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas';
    """)
cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
for row in cur.fetchall():
    print(row)
    
    
con.close()
