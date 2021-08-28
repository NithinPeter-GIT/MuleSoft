import sqlite3
con = sqlite3.connect('movies.db')

cur = con.cursor()

cur.execute("INSERT INTO movies (movie_name, lead_actor, lead_actress, year_of_release, director_name) VALUES ('Iron Man', 'Robert Downey Jr', 'Gwyneth Paltrow', 2008, 'Jon Favreau')")
con.commit()


for row in cur.execute('select * from movies'):
        print(row)

print ("\n")

cur.execute("select * from movies where lead_actor='Tom Hanks'")
print(cur.fetchall())

con.close()
