# LaserTrip_AlarmSystem
ECS Project for IOT Hackathon


This system is designed to detect movement and trigger an alarm when the laser beam is broken. Please read this instruction manual carefully before use to ensure proper installation and operation of the system.

Contents:

System Components
Installation
Operation
Troubleshooting


System Components:

The Laser Trip Wire System includes the following components:

Laser emitter(Laser)
Laser receiver(LDR)
Alarm
Power supply
Mounting brackets
User manual

Installation:
a. Mounting the Laser Emitter and Receiver:

The laser emitter and receiver should be mounted facing each other at the desired distance, with the laser beam passing between them. Use the mounting brackets provided to securely mount the emitter and receiver on opposite sides of the area to be monitored.

b. Connecting the Alarm and Power Supply:

Connect the alarm and power supply to the laser receiver according to the instructions provided. Ensure that the power supply is connected to a stable power source with the correct voltage and polarity.

c. Testing:

Test the system by breaking the laser beam between the emitter and receiver. The alarm should sound immediately when the beam is broken. If the system does not work properly, refer to the troubleshooting section of this manual.

Once the circuit has been tested, you can wire up the components directly to the Raspberry Pi as shown below.
Place one leg of the LDR and the long leg of the capacitor into a female-to-female jumper lead. Then tape it up to secure the legs.
Place the remaining legs into jumper leads, then plug it all back into the Raspberry Pi.

You can place the Raspberry Pi and components in a housing to conceal them if you wish. Here we have used a plastic box with a hole made in it for the straw:
Place your container near a doorway. Then affix the laser pointer to the wall so the beam is focused down the straw.
Now run the code and test your laser tripwire.
If you want to run your code as soon as the Raspberry Pi boots up, then have a look at the instructions below for automating tasks with Cron.

Operation:
The Laser Trip Wire System is designed to detect movement and trigger an alarm when the laser beam is broken. The system can be used for security purposes, such as detecting intruders or for industrial automation purposes to detect movement of machinery.


Safety Precautions:
a. The laser beam emitted by the Laser Trip Wire System is harmful to the eyes. Do not look directly at the laser beam or expose others to the beam.
b. Keep the Laser Trip Wire System out of reach of children and unauthorized personnel.
c. Use caution when installing and testing the system to avoid injury or damage to the components.
d. Ensure the system is installed and operated in compliance with all applicable laws and regulations.

We hope you find the Laser Trip Wire System useful and reliable for your security or industrial automation needs. If you have any questions or concerns, please contact 

Best regards,
Team Destiny
