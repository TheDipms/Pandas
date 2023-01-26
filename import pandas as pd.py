import pandas as pd
import random as shuffle
 
topics ={'Liste'['Tuple', 'List', 'Dictionary', 'For Loop', 'Github', 'Print', 'Random', 'While', 'If']}
student={'Liste'['Tayeb', 'Oscar', 'Antoine', 'Anis', 'Victor', 'Souleyman', 'Etienne', 'Nael']}
association=(topics,student)
df=pd.DataFrame(topics)
df=pd.DataFrame(student)
df=pd.DataFrame(association)
df.to_csv('association.csv')



