import random

print(random.randint(0, 10))  #peame kasutama random et näidata ära kust moodulist tuleb käsk

from random import randint  # impordime moodulist käsu

#või

from random import * #importib kõik käsud moodulist ranodm
print(randint(0, 10))  # käsk pole mooduliga seotud, saab ilma random. eesliiteta kasutada
