# Markov Decision Process

### Table Contents

- [What is MDP?](#heading-1)
  * [Before Start](#sub-heading-1)
  * [MDP Structure](#sub-heading-2)
  * [MDP Structure Example I](#sub-heading-3)
    + [State:](#sub-sub-heading-1)
    + [Action:](#sub-sub-heading-2)
    + [Reward:](#sub-sub-heading-3)
    + [Policy:](#sub-sub-heading-4)
  * [MDP Structure Example II](#sub-heading-4)
    + [State:](#sub-sub-heading-5)
    + [Action:](#sub-sub-heading-6)
    + [Reward:](#sub-sub-heading-7)
    + [Policy:](#sub-sub-heading-8)
- [How to solve MDP?](#heading-2)
  * [Value Iteration](#sub-heading-5)
    + [Discounting](#sub-sub-heading-9)
  * [Policy Iteration](#sub-heading-6)
  * [Value Iteration vs Policy Iteration](#sub-heading-7)
- [Conclusion](#heading-3)
- [Demo](#heading-4)
- [Reference](#heading-5)


<!-- toc -->

## What is MDP? <a name="heading-1"></a>
### Before Start <a name="sub-heading-1"></a>
If you are the robot under this situation, you would like to find a path to get the diamond, but not to drop into the fire. How will you do? We can obviously find that the robot can just go right and then keep goint straight, then it will get the diamond and not doping into the fire.

![](https://i.imgur.com/09WGHv1.png)

But if you're in this situation, you actually don't know what's going on, you don't know where's the diamond, where's the trap, you can't find a way to reach your goal.

![](https://i.imgur.com/kfBlqMB.png)

 



So, we're going to talk about MDP(Markov Decision Process), and through this method, we can find a best solution or path for us to reach the goal.

### MDP Structure <a name="sub-heading-2"></a>
First, I'd like to introduce the structure of the MDP. As following picture shows, first, take a look at the Agent, it can represent to who makes dicision or the robot. And there are two lines point to it, the first line is for state(S~i~), which means the state that your in. The other one is for reward(R~i~), which represent the reward or penalty that you get from the previous state to new state. And there is one more line point out to the environment, this means that the agent do one action(A~i~) and get to a new state, and the agent will get a new state(S~i+1~) and a new reward(R~i+1~), repeat and repeat.
Finally, you can get some conclusion is that when the agent face to different situation or state, it will find an action, also get a reward from it, and this we called the policy.

![](https://i.imgur.com/zeejbtZ.png)

Let me give an example here, if you are in a maze, what you are going to do is to find next step right? So, you can go straight, left, right, or back. And this we called the action(A~i~), and where you are standing or position is the state(S~i~). For the reward(R~i~) is something like if you are far away from the end, maybe you get some bad reward. On the contrary, if you are near to the end, you probably get the good reward. So, after looking this example,we probably have a better understand in MDP right? MDP is actually a good method for you to make decision in the daily life, and at the end of the introduction, I will demo a volleyball project that I done before.

**Warning: Not all the situatuion is suitable in MDP. For MDP, "markov" means actions depends only on current state.**



### MDP Structure Example I <a name="sub-heading-3"></a>
As following picture shows, we want to let the car moves as far as it could and also as fast as it could.
#### State: <a name="sub-sub-heading-1"></a>
If you are driving a car, and your car will have three states which represents the status of your car. Blue car is cool, red car is warm, and gray car is overheated, when you get to the state overheated, then it's over.

#### Action: <a name="sub-sub-heading-2"></a>
When your in any state without overheated, you can have two actions, one for diving slow, and the other one for fast.

#### Reward: <a name="sub-sub-heading-3"></a>
Just as what I said before, what you choose will affect to your reward. So, when you choose to dirve fast, you can get to the destination faster, you get a reward (+2), but it may get to the state overheated. On the other hand, if you drive slower, you get a smaller reward (+1), but never go to the state overheated.

#### Policy: <a name="sub-sub-heading-4"></a>
So, if you want to let the car move more efficiently, you have to find a best policy so that you get a best reward by an action in any states.

![](https://i.imgur.com/GWdUVch.png)

### MDP Structure Example II <a name="sub-heading-4"></a>
This is the second example. Assume that you're in the place just like below, and the goal is to get the diamond and avoid to get to the fire, and find a direction in each positions or rectangles.

#### State: <a name="sub-sub-heading-5"></a>
Except the block, the diamond, and the fire, others rectangles can be a state.


#### Action: <a name="sub-sub-heading-6"></a>
Action can absolutely be up, down, left, and reight. But some places may only have one or two direction, just like the starting point.

#### Reward: <a name="sub-sub-heading-7"></a>
The reward for this example is if you get the diamond(+1), and get to the fire(-1).
Also, you can add more advance is that if you walk one more step, you get a -0.1 reward, so that the robot will find the way faster.

#### Policy: <a name="sub-sub-heading-8"></a>
The best policy is to find the best action in every positions or states.

![](https://i.imgur.com/kh63B4g.png)![](https://i.imgur.com/oifyXOS.png)


## How to solve MDP? <a name="heading-2"></a>
After introducing the MDP structure, we're going to start talking about more and how to solve it. I will talk about two ways for you to solve MDP, of course, you can choose whatever you like. But in different situations, there will be a better ways for it.
First, before we start, we should know one thing. Take a look at the picture below, the blue triangle represent a state. And the arrow pointed out represent an action, and if you choose the solid line, you will get to a green circle. This is a fake state which means if you decide to take this action to the state before you really do so.
Why do I say that? That's because you may face some problems after you make the action, then you might not take the action that you choose before. This is much more complexity, but we should know one thing  definitely is that if we start from state s to state s' by taking action a, and this we called a transition T(s,a,s'), also we get a reward R(s,a,s').

![](https://i.imgur.com/OmMXJy9.png)
### Value Iteration <a name="sub-heading-5"></a>
The first method I would like to mentioned is Value Iteration.
After knowing whats going on on the top, we can give a value in every state, so that it can represent all the rewards of this state. Then if we want to calculate the state's value in the future, we have to know the state's value in the past right? So we can try using dynamic programming, this is what value iteration do.

![](https://i.imgur.com/Rau1Gpf.png)
Let's take a look at this formula, V~k~(s') represent the value of state s' and V~k+1~(s) represent the value of state s in the next iteration, and now we can have this formula to represent the update of value. First, take a look at R(s, a, s'), this is what we discuss on the top, the reward part. Because if we want to find the best policy then the reward should be the highest in each iteration. T(s, a, s') is the transition from state s to state s'. Finally, just take the maximum in every action, you can probably get the best policy in every state in each iteration. Until it converge, you get the best policy.

![](https://i.imgur.com/EnvsxDw.png)
So, this picture below is same us what we are doing, iterate it until it converge.


![](https://i.imgur.com/yNXgPvX.png)
#### Discounting <a name="sub-sub-heading-9"></a>
Actually, so how can this be converge? The value probably increase in every iteration right? As a result, we have to talk about the discounting. Look the picture below, If you are the robot what will you choose, will you choose the left one to get one diamond in each step, or get four diamonds in the last step. Which way will you choose? 

![](https://i.imgur.com/Nt8lDPp.png)
Basically, you will choose left, because they both can get the same number of diamonds, but maybe the robot walk three steps only right? How does it happen? The battery can be dead, or out of energy. So, it is clearly that get the reward faster is greater than future. But, here is another example is if there are five diamonds in the right path but in the last step. This is hard to choose. Therefore, we can give a discount to the future state, like discount equals to 0.9 etc. And we can make sure that now is better than future.

![](https://i.imgur.com/RQhy4Sc.png)

And so for that, we can just add a discount before V~K~(s'), then we can have the effect of what I mentioned above. Also, if you look at the forumla down, it can actually be converge after some iterations.( I will not mentioned the provement here. )

![](https://i.imgur.com/FFWaYcM.png)
This is all about Value Iteration, then we just need to run this algorithm or method in the PC, basically, we can get the best action or best policy.

First, let all the state initial to zero, and then run a loop. In the loop, you just need to do two things, calaulate the maximun reward for every action in each state, and update the value of the state. Just keep doing so until every state is converge. The second line represent the policy, so in each state and each iteration, there will be a best action and be recorded.

![](https://i.imgur.com/lzy63cy.png)
### Policy Iteration <a name="sub-heading-6"></a>
Now, we're going to talk about second method to solve MDP. Policy Iteration is similar to Value Iteration, but the only different is that Policy Iteration delete the maximun. How does that works? Policy Iteration will initially gives a policy, and in every iteration, you can change a policy if the value is bigger. So, when you run many times you can get a policy that have the biggest value in every state nad that's the best solution. What's more, actually Policy Iteration can converge more faster than Value Iteration.

![](https://i.imgur.com/RAQ40qg.png)
![](https://i.imgur.com/HnQ6lMm.png)

### Value Iteration vs Policy Iteration <a name="sub-heading-7"></a>
As we known, Policy Iteration converges more faster than Value Iteration, but in different cases, we still can use Value Iteration. For example, if you have fewer action, it's quite easy to take maximum in every action, so Value Iteration is fine. Contrary, if you have lots of actions or you just get a fair policy, you probably use Policy Iteration will be better.

## Conclusion <a name="heading-3"></a>
Hope everyone knows what's going on from creating the MDP model to solve it. Actually, there are many ways to solve MDP, even the Linear Programming can solves it. But here I just want to talk about using Dynamic Programming to solve it. Because it's easy to understand and more intuitive.
 
 
## Demo <a name="heading-4"></a>
Because I played volleyball in my free time, so I did an interesting things in my demo project. I use MDP to do volleyball analysis, and let the coach or player to give the right person or possion to spike. Lets get started. I will introduce the state first, the state represent the teams is winning or losing, just like this, I have five states, losing a lot(score losing under 4), losing a little(score losing 2 ~ 3), middle(-1 ~ +1), winning a little(score winning 2 ~ 3), winning a lot(score winning above 4). For the action, look at the picture below, there will be six actions which represent the position that going to spike. ![](https://i.imgur.com/TJ7QOzj.png)
And the most difficult is that to define the reward, the most simple thing is if get a point you get reward +1, if you did not, -1, but that isn't enough, you may not get the score or lose the score right? So, I add some small reward for morale in some situation. Also, it's hard to get the data instead, so I watch each game plays and record it. Finally this is what I get.
![](https://i.imgur.com/DTYijpG.png)
As above shows, this game is [China vs Italy - Full Match | FINALS | Women's Volleyball World Grand Prix 2015 ](https://www.youtube.com/watch?v=sa8HAWtPKKs), and I use the MDP to run that in each state you get a best action so that the value of all states could be the largest. And so like in the first line, its shows that when China team is losing a lot, they should probably give the ball to position 6 and can get better result, or like if they're team is winning a liitle bit, they can give the ball to position 
3 to get the better reward.
Here is the [sample code](https://github.com/tyler8812/Markovian-Decision-Process/blob/master/mdp.py), but maybe isn't works for you. My suggestion is that if you really want to understand what is MDP, just write a simple project in your daily life, you can probably understand what's going on. 


 ## Reference <a name="heading-5"></a>
[Dan Klein, Pieter Abbeel, John Schulman, Yan (Rocky)
Duan and Xi (Peter) Chen for CS188 Intro to AI at UC
Berkeley. ](http://ai.berkeley.edu/)
[OR Coure in NCKU taught by professor Lee.](http://140.116.86.229/)

















