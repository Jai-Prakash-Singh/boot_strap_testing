def python_session():
from pymongo import Connection

def pymongo_session():
    databaseName = "sample_database"
    connection = Connection()
    
    db = connection[databaseName]
    employees = db['employees']
    
    person1 = { "name" : "John Doe",
        "age" : 25, "dept": 101, "languages":["English","German","Japanese"] }
	
    person2 = { "name" : "Jane Doe",
        "age" : 27, "languages":["English","Spanish","French"] }
	
    print "clearing"
    employees.remove()
    
    print "saving"
    employees.save(person1)
    employees.save(person2)
    
    print "searching"
    
    for e in employees.find():
        print e["name"] + " " + unicode(e["languages"])

    for e in employees.find({"name":"John Doe"}):
        print e



if __name__=="__main__":
    pymongo_session()
