# BirthdayParadox

## Description
Probably many have heard about the birthday paradox. A paradox that defies human intuition.
Probability theory says that if there are more than 23 people in a group, then the probability of at least two people having the same birthday is more than 50% (50.73%). And if there are 70 people, then the probability of coincidence of birthdays exceeds 99.9%.
This program selects a given number of people, assigns a random birthday to each of them and conducts a statistical experiment - how often people with the same birthdays meet with the given parameters.

## Setting
For setting, 2 parameters are used in the main program file.
1) countOfExperiments - number of experiments. The larger the number, the longer the statistics will be calculated, but the more accurate the result will be. Recommended value - 1000
2) countOfHumans - the number of people in the group. The default is 23.

## Conclusions

Thanks to this program, you can verify the plausibility of this paradox. You will really see that if there are 23 people in a group, then the probability of at least two people having the same birthday is more than 50%, and if there are 70 of them, then the probability will be more than 99.9% at all

## Experimental data

```
| Count Of Humans: 23
| Count Of Experiments: 10000
| Final Probability: 0.5119
```

```
| Count Of Humans: 26
| Count Of Experiments: 10000
| Final Probability: 0.5911
```

```
| Count Of Humans: 38
| Count Of Experiments: 10000
| Final Probability: 0.8647
```

```
| Count Of Humans: 70
| Count Of Experiments: 10000
| Final Probability: 0.9988
```
