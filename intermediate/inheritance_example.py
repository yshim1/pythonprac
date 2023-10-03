class School:

  def __init__(self, level, name, numberOfStudents):
    self.level = level
    self.name = name
    self.numberOfStudents = numberOfStudents
  
  def get_level(self):
    return self.level

  def get_name(self):
    return self.name
  
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents
  
  def __repr__(self):
    print('A {} school named {} with {} students'.format(self.level, self.name, self.numberOfStudents))
  
# pb = School('High', 'Paint Branch', 1000)
# print(pb.get_level())
# print(pb.get_name())
# print(pb.get_numberOfStudents())
# pb.set_numberOfStudents(4000)
# print(pb.get_numberOfStudents())
# pb.__repr__()
class PrimarySchool(School):
  def __init__(self, level, name, numberOfStudents, pickupPolicy):
    super().__init__(level, name, numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    print('The pickup policy is {}'.format(self.pickupPolicy))
    super().__repr__()
    

primschool = PrimarySchool('Primary','Bsville', 300, 'Pickup after 2:45')
# print(primschool.get_name())
# print(primschool.get_numberOfStudents())
# print(primschool.get_pickupPolicy())
# print(primschool.get_level())
# primschool.__repr__()

class HighSchool(School):
  def __init__(self, level, name, numberOfStudents, sportsTeams):
    super().__init__(level, name, numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    super().__repr__()
    print('These are our sports teams: {}'.format(self.sportsTeams))

hs = HighSchool('High', 'Paint Branch', 3000, ['Soccer', 'Basketball', 'Football'])
# print(hs.get_name())
# print(hs.get_numberOfStudents())
# print(hs.get_level())
# print(hs.get_sportsTeams())
# hs.__repr__()


