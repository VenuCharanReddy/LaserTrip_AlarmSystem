# LaserTrip_AlarmSystem

This system is designed to detect movement and trigger an alarm when the laser beam is broken. Please read this instruction manual carefully before use to ensure proper installation and operation of the system.

##Contents:

**System Components:**

The Laser Trip Wire System includes the following components:
Laser emitter(Laser)
Laser receiver(LDR)
Alarm
Power supply
PiCamera
User manual


**Installation:**

a. First, Install the RaspberryPi Os using Imager(recommended 32-bit) and then using putty initialise the VNC viewer. Log-in to VNC Viewer by using username and password. Its better to enable hotspot at the installation of RaspberryPi Os.


b. _**Mounting the Laser Emitter and Receiver:**_  The laser emitter and receiver should be mounted facing each other at the desired distance, with the laser beam passing between them. Use the mounting brackets provided to securely mount the emitter and receiver on opposite sides of the area to be monitored.


c. _**Connecting the Alarm and Power Supply:**_ Connect the alarm and power supply to the laser receiver according to the instructions provided. Ensure that the power supply is connected to a stable power source with the correct voltage and polarity.


d. _**Testing:**_

Test the system by breaking the laser beam between the emitter and receiver. The alarm should sound immediately when the beam is broken. Once the circuit has been tested, you can wire up the components directly to the Raspberry Pi as shown below.


![image](https://github.com/VenuCharanReddy/LaserTrip_AlarmSystem/assets/107487538/17d077cf-632d-4004-bc29-3d3ed7cfd6e6)


Place one leg of the LDR and the long leg of the capacitor into a female-to-female jumper lead. Then tape it up to secure the legs.
Place the remaining legs into jumper leads, then plug it all back into the Raspberry Pi. You can place the Raspberry Pi and components in a housing to conceal them if you wish. Here we have used a plastic box with a hole made in it for the straw. Place your container near a doorway. Then affix the laser pointer to the wall so the beam is focused down the straw.                                         

**Here is the pictorial Sketch of the model**
                            
  
  
  ![image](https://github.com/VenuCharanReddy/LaserTrip_AlarmSystem/assets/107487538/6302bba2-6bfe-4520-be9e-4d9a5903c3fe)

               




e. _**Enable Camera:**_
sudo raspi-config (type the code in terminal)
Select Interface Options and enable the camera. Then use the cam.py code and check whether cam is working. 



f. _**Setting up Email:**_
Using smtplib we have created a email id and created a app password. Using that we are sending a mail by attaching the images captured by PiCamera.
Go through with sent.py



g._**Setting up LiveStream:**_

Follow "live" file in the repository for this...



**Operation:**

The Laser Trip Wire System is designed to detect movement and trigger an alarm when the laser beam is broken. The system can be used for security purposes, such as detecting intruders or for industrial automation purposes to detect movement of machinery.
We hope you find the Laser Trip Wire System useful and reliable for your security or industrial automation needs. If you have any questions or concerns, please contact 

