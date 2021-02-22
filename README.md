# PiFish

 # Tail
                if GPIO.input(pin1) and not pin1_old:
                                print("ON")
                                kit.motor2.throttle = 1
                                pin1_old = True
                                time.sleep(0.1)

                if not GPIO.input(pin1) and pin1_old:
                                print("OFF")
                                kit.motor2.throttle = -1
                                pin1_old = False
                                time.sleep(0.1)

