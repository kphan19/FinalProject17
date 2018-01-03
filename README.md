# FinalProject17
# Before playing, player can take a quiz to have a certain character class for different advantages
# The player wakes up in a room (start) and begins their journey to leave
# Starting room will have basic items to begin with based on what character class they're in

# Functions for maintanence
def print_slow(str, speed):
  """prints the text letter by letter"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
      
def cls():
  """clears screen"""
    os.system('cls' if os.name=='nt' else 'clear')
    
def check_answer(self, question, answers):
        answer = " "
        while answer not in answers:
            answer = input(question).lower()
        return answer
        
