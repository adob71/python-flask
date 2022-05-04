# https://app.codility.com/programmers/trainings/5/parking_bill/

E = input("You entered the car parking lot at time [10:00]") or "10:00"
L = input("You left the car parking lot at time [13:21]") or "13:21"

def solution(E, L):
    EH = E[0:2]
    EM = E[3:5]
    LH = L[0:2]
    LM = L[3:5]
    H=int(LH)-int(EH)
    M=int(LM)-int(EM)
    print ("Parking time :",H,"hours",M,"minutes")

    entrance_fee=2
    the_first=0
    each_successive=0

    if H>0:
        the_first=3
        H=H-1

    while H > 0:
        each_successive=each_successive+4
        H=H-1

    if M>0:
        each_successive=each_successive+4

    parkingbill=entrance_fee+the_first+each_successive
    return parkingbill

print("Parking bill : $", solution(E, L))
