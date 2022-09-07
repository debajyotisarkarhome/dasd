import serial
import time 

INPUT_BUFFER_SIZE = 32
INPUT_DATA_SIZE = 32
HEAD_WORD = 0x4020
CHANNEL = 3 #channel = this + 1

'''  Packet structure : 
        b'\xdc'
'''
port = serial.Serial('COM11', 115200, timeout=0.01)
while(True):
        for i in range(1000,2000):
                data_array = [b'\x00'] * INPUT_DATA_SIZE
                data_array.insert(0,b' ')
                data_array.insert(0,b'@')
                #print(data_array)
                if(i>=1024 and i<1280):
                        second = 4
                elif(i>=1280 and i<1536):
                        second = 5
                elif(i>=1536 and i<1792):
                        second = 6
                elif(i>=1792 and i<2048):
                        second = 7
                else:
                        second = 3
                first = i - (second<<8)
                # print(first)
                # print(second)
                data_array[CHANNEL*2+2] = bytes([first])
                data_array[CHANNEL*2+3] = bytes([second])
                meaw = b''.join(data_array)
                port.write(meaw)
                print(meaw)
                time.sleep(0.1)


        # for i in range(2000,1000,-1):
        #         data_array = [0] * INPUT_DATA_SIZE
        #         data_array.insert(0,b' ')
        #         data_array.insert(0,b'@')
        #         if(i>=1024 and i<1280):
        #                 second = 4
        #         elif(i>=1280 and i<1536):
        #                 second = 5
        #         elif(i>=1536 and i<1792):
        #                 second = 6
        #         elif(i>=1792 and i<2048):
        #                 second = 7
        #         else:
        #                 second = 3
        #         first = i - (second<<8)
        #         # print(first)
        #         # print(second)
        #         data_array[CHANNEL*2+2] = first
        #         data_array[CHANNEL*2+3] = second
        #         meaw = bytes(data_array)
        #         port.write(meaw)
        #         print(meaw[2*2+2] + (meaw[2*2+3] << 8))
        #         time.sleep(0.1)