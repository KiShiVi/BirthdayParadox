import random

#########################################
#               Settings                #
#########################################
countOfExperiments = 10000              #
countOfHumans = 23                      #
#########################################

countOfWins = 0
humans = []
_flag = False

for k in range(countOfExperiments):
    humans = []
    _flag = False

    for i in range(countOfHumans):
        humans.append(random.randint(1, 365))

    # for i in range(countOfHumans):
    #     print('Human #' + str(i) + ': ' + str(humans[i]))

    for i in range(len(humans)):
        if _flag:
            break
        for j in range(i + 1, len(humans)):
            if i == j:
                continue
            if humans[i] == humans[j]:
                # print('Human #' + str(i) + ' & Human #' + str(j) + ' celebrate a birthday on the same day!!!')
                countOfWins += 1
                _flag = True
                break

print('| Count Of Humans: ' + str(countOfHumans))
print('| Count Of Experiments: ' + str(countOfExperiments))
print('| Final Probability: ' + str(countOfWins / countOfExperiments))
