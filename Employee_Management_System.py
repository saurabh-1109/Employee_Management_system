import mysql.connector 

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SAURABH@20",
    database="emp"
)

def check_employee(employee_id):

    #query to select all rows from employee table
    sql = 'SELECT * FROM employees WHERE id=%s'

    #making cursor buffered
    cursor = con.cursor(buffered=True)
    data = (employee_id,)

    #executing sql query
    cursor.execute(sql,data)

    #fetching 1st row to check employee exitsts
    employee = cursor.fetchone()

    #closing the cursor
    cursor.close()

    #if found return true else false
    return employee is not None 

def add_employee():
    #Emplyee id creation
    Id = input("Enter Employee Id : ")

    #checking if employee exist IF found
    if check_employee(Id):
        print(" \n Employee already exists.")
        return
    
    #if not found
    else :
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee salary: ")

    sql = 'INSERT INTO employees(id, name, position, salary) VALUES (%s, %s, %s, %s)'
    data = (Id, Name, Post, Salary)
    cursor = con.cursor()

    try:
        #executing sql command
        cursor.execute(sql,data)

        #comminting transaction
        con.commit()
        print("Employee Added Successfully")
    
    except mysql.connector.Error as err:
        print(f"Error : {err}")
        con.rollback()
    
    finally:
        cursor.close()

def remove_employee():
    Id = input("Enter Employee Id: ")

    # Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist.")
        return
    
    else:
        # Query to delete employee from the employees table
        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        cursor = con.cursor()

        try:
            cursor.execute(sql, data)
            con.commit()
            print("Employee Removed Successfully")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()
        
        finally:
            # Closing the cursor
            cursor.close()

def promote_employee():
    Id = input("Enter Employee's Id: ")

    # Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    else:
        try:
            Amount = float(input("Enter increase in Salary: "))

            # Query to Fetch Salary of Employee with given Id
            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            data = (Id,)
            cursor = con.cursor()

            # Executing the SQL Query
            cursor.execute(sql_select, data)

            # Fetching Salary of Employee with given Id
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount

            # Query to Update Salary of Employee with given Id
            sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
            data_update = (new_salary, Id)

            # Executing the SQL Query to update salary
            cursor.execute(sql_update, data_update)

            # Committing the transaction
            con.commit()
            print("Employee Promoted Successfully")

        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            con.rollback()

        finally:
            # Closing the cursor
            cursor.close()

def search_employee():
    try:
        id = int(input("Enter Employee Id :"))
        # #query to select all rows from employee table
        sql = 'SELECT * FROM employees WHERE id=%s'
        cursor = con.cursor()

        cursor.execute(sql,(id,))

        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ",employee[0])
            print("Employee Name : ",employee[1])
            print("Employee Post : ",employee[2])
            print("Employee Salary : ",employee[3])
            print("------------------------------------")
    except mysql.connector.Error as err:
        print(f"error : {err}")
    
    finally:
        cursor.close()
        
def display_employee():
    try:  
        sql = 'SELECT * FROM employees'
        cursor = con.cursor()

        cursor.execute(sql)

        employees = cursor.fetchall()
        for employee in employees:
                print("Employee Id : ",employee[0])
                print("Employee Name : ",employee[1])
                print("Employee Post : ",employee[2])
                print("Employee Salary : ",employee[3])
                print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"error : {err}")
    
    finally:
        cursor.close()
        
        
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Search Employees")
        print("6 to Exit")
        
        # Taking choice from user
        ch = input("Enter your Choice: ")
        print("-------------------------------------------")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
           display_employee()
        elif ch == '5':
            search_employee()
        elif ch == '6':
            print("Exiting the programm...")
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    menu()