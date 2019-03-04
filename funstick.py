#!/usr/bin/python3

import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
  print("No joystick found!")
  exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("\n")
print("Joysticks :", pygame.joystick.get_count())
print("     Name :", joystick.get_name())
print("     Axes :", joystick.get_numaxes())
print("  Buttons :", joystick.get_numbuttons())
print("\n")
print("Press a button or move Axle!, Press CTRL+C to end script.")
print("\n")


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
          button_status = joystick.get_button(i)


          #  Welke knop is ingedrukt
          if button_status == True and i == 0:
            # Pressed Button 0
            print(" Button 0 Is Pressed!")

          elif button_status == True and i == 1:
            # Pressed Button 1
            print(" Button 1 Is Pressed!")

          elif button_status == True and i == 2:
            # Pressed Button 2
            print(" Button 2 Is Pressed!")

          elif button_status == True and i == 3:
            # Pressed Button 3
            print(" Button 3 Is Pressed!")

          elif button_status == True and i == 4:
            # Pressed Button 4
            print(" Button 4 Is Pressed!")

          elif button_status == True and i == 5:
            # Pressed Button 5
            print(" Button 5 Is Pressed!")

          elif button_status == True and i == 6:
            # Pressed Button 6
            print(" Button 6 Is Pressed!")

          elif button_status == True and i == 7:
            # Pressed Button 7
            print(" Button 7 Is Pressed!")

          elif button_status == True and i == 8:
            # Pressed Button 8
            print(" Button 8 Is Pressed!")

          elif button_status == True and i == 9:
            # Pressed Button 9
            print(" Button 9 Is Pressed!")

          elif button_status == True and i == 10:
            # Pressed Button 10
            print(" Button 10 Is Pressed!")

          elif button_status == True and i == 11:
            # Pressed Button 11
            print(" Button 11 Is Pressed!")



      # Er wordt een knop losgelaten.
      elif event.type == pygame.JOYBUTTONUP:
         print("Knop: losgelaten!")
         pass

      # Een as wordt bewogen.
      elif event.type == pygame.JOYAXISMOTION:
        # Loop alle beschikbare assen langs.
        for i in range(assen):
          # Haal de waarde van de as op.
          eenas = joystick.get_axis(i)
          # Als een as
          if eenas != 0:
            if i == 0: asrichting = 'X'
            if i == 1: asrichting = 'Y'
            if i == 2: asrichting = 'X'
            if i == 3: asrichting = 'Y'
            print("AS", i, "waarde:", asrichting, eenas)

except KeyboardInterrupt:  
  # PyGame netjes afsluiten wanneer er op CTRL+C is gedrukt.
  pygame.quit()
