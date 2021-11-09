from user import Admin

my_admin = Admin('Gustavo', 'gustavotinho@gmaiil.com', 'Pernambuco', 'Recife')

my_admin.describe_person()
my_admin.describe_live()

my_admin.privilleges.show_describe()

my_admin_privileges = ['Add User', 'Deleting User', 'Update User']

my_admin_privileges.privileges = my_admin_privileges

print("\n Admin: " + my_admin.name + " privileges" )
my_admin_privilleges.show_describe()
