from user import User, Privileges, Admin

admin1 = Admin('Joe', 'Shmoe', 'jshmoe', 'Marketing')
admin1.privileges.show_privileges()