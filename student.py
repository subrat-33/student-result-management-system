class Student:
  
  def calculate_total(self,math,science, english):
    total = math + science + english
    return total
  
  def calculate_percentage(self, total):
    percentage = (total /300) * 100
    return percentage
  
  def calculate_grade(self, percentage):
    if percentage >= 90:
      return "A"
    elif percentage >= 75:
      return "B"
    elif percentage >= 60:
      return "C"
    else:
      return "D"