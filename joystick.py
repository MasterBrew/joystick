1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
#!/usr/bin/env python
 
# Importeer PyGame bibliotheek.
import pygame
 
# Initialiseer de Joystick(s).
pygame.init()
pygame.joystick.init()
 
# Kijk of er een joystick of controller aangesloten is.
if pygame.joystick.get_count() == 0:
  # Er is geen joystick of controller gevonden.
  print "Er is geen joystick gevonden!"
  exit()
 
joystick = pygame.joystick.Joystick(0)
joystick.init()
 
# Informatie over de Joystick of controller
print "Joysticks gevonden:", pygame.joystick.get_count(), "(", joystick.get_name(), ")"
print "Specs: assen:", joystick.get_numaxes(), ", knoppen:", joystick.get_numbuttons()
print "Druk op de knoppen of draai aan de assen!, druk op CTRL+C om het script te eindigen."
# Haal het aantal knoppen en assen op.
knoppen = joystick.get_numbuttons()
assen = joystick.get_numaxes()
asrichting = 0
 
try:
  # Oneindige loop, druk op CTRL+C om het script te eindigen.
  while True:
    # Interrupt trigger voor PyGame.
    for event in pygame.event.get():
 
      # Er wordt een knop ingedrukt.
      if event.type == pygame.JOYBUTTONDOWN:
        # Loop alle beschikbare knoppen langs.
        for i in range(knoppen):
          # Haal de waarde van de knop op.
          knop = joystick.get_button(i)
          # Kijk of deze knop is ingedrukt.
          if knop == 1:
            # Deze knop is ingedrukt.
            print "Knop:", i, "ingedrukt!"
 
      # Er wordt een knop losgelaten.
      elif event.type == pygame.JOYBUTTONUP:
         print "Knop: losgelaten!"
 
      # Een as wordt bewogen.
      elif event.type == pygame.JOYAXISMOTION:
        # Loop alle beschikbare assen langs.
        for i in range(assen):
          # Haal de waarde van de as op.
          eenas = joystick.get_axis(i)
          # Als een as
          if eenas <> 0:
            if i == 0: asrichting = 'X'
            if i == 1: asrichting = 'Y'
            if i == 2: asrichting = 'X'
            if i == 3: asrichting = 'Y'
            print "AS", i, "waarde:", asrichting, eenas
 
except KeyboardInterrupt:  
  # PyGame netjes afsluiten wanneer er op CTRL+C is gedrukt.
  pygame.quit()