
secret_api_key = '5sdf56s65fs6d4f6sd5f6s5df6ssd6f5sd2f1ef4zefr4'
user_name      = input("Enter user name")

class CountUser():
  def __init__(self):
    self.user_count = 0

  def add_user(self):
    self.user_count += 1

count = CountUser()

def welcome_new_user(count, user_name):
  count.add_user()

  answer  = "Welcome " + user_name + " !!"
  answer += " You are the {count_obj.user_count}th user :)"

  return answer.format(
    count_obj = count
  )

print(welcome_new_user(count, user_name))