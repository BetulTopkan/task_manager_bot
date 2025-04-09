from database import Database
import os

def test_add_task():
    
    db = Database("test_tasks.db")
    
 
    task_id = db.add_task("Test görevi")
    
    
    tasks = db.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0][1] == "Test görevi"
    assert tasks[0][2] == 0  
    
   
    os.remove("test_tasks.db") 