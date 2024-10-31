
camal_name= input('enter you camal case name:')
def covert_to_snake(camal_name):
  word=" "
  snake=" "
  j=0

  for n in range(len(camal_name)):
    if camal_name[n].isupper():
      snake += "_" + camal_name[n].lower()

    else:
      snake += camal_name[n]

  print(f'The snake case of your camal case is{snake}')