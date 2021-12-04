# You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
# of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
# run to university. You jog the first mile at 7mph; then run the next two at15mph; before
# jogging the last at 7mph again. Will this be quicker or slower than the bus?

Bus=(4/(25/60)+2*10)
print("The total time taken by Bus is:",Bus,"mph")
Jogging=(1/(7/60)+2/(15/60)+1/(7/60))
print("The total time taken by Jogging is:",Jogging,"mph")
if Bus>Jogging:
    print("Bus is faster")
else:
    print("Jogging is faster")