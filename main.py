from user import User

user_1 = User('Shandy')

# CASE 1 - DONE
# user_1.check_benefit()

# CASE 2 - DONE
# user_1.check_plan(user_1.username)

# CASE 3
user_1.upgrade_plan(user_1.username, 'Premium Plan')