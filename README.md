# Markovian Decision Process

### Table Contents

- [What is MDP?](#heading)
  * [Before Start](#sub-heading)
  * [MDP Structure](#sub-heading)
  * [MDP Structure Example I](#sub-heading)
    + [State:](#sub-sub-heading)
    + [Action:](#sub-sub-heading)
    + [Reward:](#sub-sub-heading)
    + [Policy:](#sub-sub-heading)
  * [MDP Structure Example II](#sub-heading)
    + [State:](#sub-sub-heading)
    + [Action:](#sub-sub-heading)
    + [Reward:](#sub-sub-heading)
    + [Policy:](#sub-sub-heading)
- [How to solve MDP?](#heading)
  * [Value Iteration](#sub-heading-1)
    + [Discounting](#sub-sub-heading-1)
  * [Policy Iteration](#sub-heading-1)
- [Conclusion](#heading-2)


<!-- toc -->

## What is MDP?
### Before Start
假設你現在如下圖所示，你想找一條路徑使你可以拿到右邊那個寶石，但卻不會掉進前面的火堆當中。
我們很明顯的可以知道說我們只要往右一格然後再依直向著寶石的方向走，就絕對不會掉進火堆當中，且一定可以拿到寶石了。

![](https://i.imgur.com/09WGHv1.png)

但如果你和下圖一樣，你根本不知道寶石在哪或是陷阱在哪，你無法去找出一條好的路徑使你完成目標對吧。

![](https://i.imgur.com/kfBlqMB.png)

所以我們要來探討 MDP 這個方法，此方法可以讓我們找出一個最好的路徑來完成目標。

### MDP Structure

首先我們先來看看下面這張圖，我來稍微解釋一下，我們從 Agent 這個地方開始看起，我們可以把他想成是自己或是決策的人，而前面有兩個箭頭指向 Agent，第一條是 state(S~i~)，代表著我現在所在的狀態，第二條則是 reward(R~i~)，代表著我從上一個狀態所得到的獎賞或是懲罰，而從 Agent 也有一條指向 Environment ，這代表著我們做了一個 action (A~i~)，使得我們到達了一個新的狀態，而這個新狀態又會在產生一個 state(S~i~) 和 reward(R~i~) 給 Agent，然後一直重複循環，最後你可以得出一個結論就是當面對不同 State 時，你可以得出一個最好的 Action，使得最後 Reward 最高，此稱為一個 Policy。

聽完上面的解釋是不是還是不太懂呢? 那我這邊舉個範例好了，假設如上圖，你現在處在一個迷宮當中，你所要做的是你要選擇你下一步該往哪走，那這個我們就稱為 action (A~i~)，而你現在所在的位置就可以想成是一個 state(S~i~)，那至於 reward(R~i~) 的部分就像是說你如果走到了死路，你就必須要花更多力氣回到會走過的路，這就可能是懲罰的部分，反之，當你感覺你離終點越來越近了，那你應該就可以得到獎賞。看完這個範例應該有對這個架構有更多的了解對吧，因為在迷宮當中，你每走一步如果都照著這樣的架構去走的話，你說不定真的可以找到最好的方法並走到終點對吧! 那假如迷宮可以用這個方式來完成，那說不定我們也可以把 MDP 實作在日常生活中對吧，像是我有做一個 Project 是在對於排球比賽去做最佳的 Policy 來使得得分效率最高(最後會有介紹)。

![](https://i.imgur.com/zeejbtZ.png)

**Warning: 但也並非所有情況都可以使用 MDP ， MDP 全名為 Markovian Decision Process ，之所以為 Markovian 正是因為它必須滿足一個重要的條件才可以使用這個方法，那就是每個 State 和 State 之間必須互相獨立，也就是不會影響，因此在可以在每個 State 找到最佳的 Action。**

### MDP Structure Example I
#### State:
假設你現在開著一輛車，如下圖所示，你的車會有三個狀態，分別代表車子所處的狀態，有正常、稍熱、過熱，當你車子達到過熱這個階段時，你車子就壞了，也就不能繼續駛行了。
#### Action:
當車子在不同狀態時，你可以有兩種的 Action ，分別是 Slow 和 Fast ，代表你駛行的速度。
#### Reward:
你所選則駛行的速度也影響到你的 Reward 部分，因為你駛的快，你車子可以更快到達目的地，所以當 Action 為 Slow 時， Reward 為 1，但當為 Fast 時， Reward 為 2。
#### Policy:
你想讓此車在最有效率的方式下駛行，因此你就要找到一個 Policy 使得在每個 State 有最佳 Action，來得到最高的 Reward。
![](https://i.imgur.com/GWdUVch.png)

### MDP Structure Example II
這是第二個 Example ，而我們接下來也會用下列的 Example 去解我們的 MDP。假設你現在處在下圖地圖上，你想要拿到鑽石並避開有火的地方，你的目標是找到每個位置的走法。
#### State:
除了不能走的地方、有寶石、和火焰的地方以外，其餘的地方都可以看成一個 State。
#### Action:
Action 當然可以是前後左右，但值得注意的是，有些地方可能沒有 4 種走法，像是 Start 的位置就只能向上或向右。
#### Reward:
這個 Example 的 Reward 就是寶石+1、火焰-1。
#### Policy:
因此最好的 Policy 就是找到每個位置的最佳 Action 。

![](https://i.imgur.com/kh63B4g.png)![](https://i.imgur.com/oifyXOS.png)


## How to solve MDP?
介紹完了 MDP ，當然就是要開始介紹要怎麼解 MDP 了，以下我們會介紹兩種不同的方式去解 MDP ，當然你可以自己去選擇喜歡的方式，不過對於各種情況的不同，會有較好的方式，以下我都會一一做介紹。

首先在開始之前我們要先知道一件事，請看下圖，藍色三角形代表者一個 state ，而箭頭指出去代表著一個 action ，而綠色圓圈代表著當你決定要走此 Action 後到真的走了之前的一個狀態，為甚麼要有這個狀態呢? 是因為當你決定好走這個 action ，但有可能有其它意外導致跟原本預期的不一樣，那這時可能就會走另一個 action ，這之後會繼續延深，所以現在只要知道說我從 s(state) 走了一個 a(action) 到達了 s'(state) 後，這整個稱為一個 T(s,a,s')(transition) ，並會從這當中取得 R(s,a,s')reward。

![](https://i.imgur.com/OmMXJy9.png)
### Value Iteration
知道上面的這個流程之後，我們可以給每個 state 一個值，代表此 state 目前的狀態好壞，因為知道這個後我可以推測下一次這個 state 的好壞，就這樣往前推就可以推到很後面去了，這就是 value iteration 的想法。

![](https://i.imgur.com/Rau1Gpf.png)
那我們來看看下面這個式子，V~k~(s') 代表在 state s' 時的值，V~k+1~(s) 代表在 state s 時的值，再來我們可以列出此式子表示每次 state 在做更新的方式，首先先看 R(s, a, s')，這就是上面所提到的 reward 的部分，因為我們要找出最好的 policy 就是要找出 reward 最好的，因此每次在做 state 值更新時，主要就是根據 reward 去看，那前面 T(s, a, s') 就是 state 和 state 之間的轉移，最後再用 max 去找出當下最好的 action ，這就是一次的 value iteration ，這大概就是 value iteration 的核心架構。

![](https://i.imgur.com/EnvsxDw.png)
接下來的就是要一直去算出每個 state 的值，當你一直往下算之後，你就可以看到很遠的 state 情況了，如下圖所示。

![](https://i.imgur.com/yNXgPvX.png)
#### Discounting
那其實這樣你可能會發現有問題的產生，那就是我的 reward 會不會一直加一直加到無限大，那這時候我們需要探討到收斂的問題，看看下圖，我們到底該選擇哪一條路線呢? 兩個都是走完可以拿到4個寶石，我該走左邊還右邊呢? 

![](https://i.imgur.com/Nt8lDPp.png)
基本上應該是要選擇左邊的會比較好吧，雖然最後都可以拿到同樣數量的寶石，但假設我們只走了三步呢? 或者我們每走一步會消耗一定的體力，所以是不是越早拿到越好? 因此我們可以給越後面拿到的 reward 一個 discount ，向下圖這樣我們把後面的 state 多乘上一個介於 0 到 1 的值，這樣可以保證先得到會比後得到來的好。

![](https://i.imgur.com/RQhy4Sc.png)
那假設是如此的話，我們就要把 value iteration 多乘上一個值在V~K~(s')，使得可以有 discount 的作用，也因此如此，我們可以使得 state 的值可以達到收斂，就不會有 value 越加越大的問題了。

![](https://i.imgur.com/FFWaYcM.png)
上述都已經教完 value iteration 的一些架構和觀念了，那接下來我們只要把以下演算法帶入電腦中讓他跑，那基本上就可以得出每個 state 最佳 action 或是說最好的 policy。
一開始先把每個 state 的 value 設為 0，然後就用 for loop 去一直跑，因為它會收斂，所以不用跑太久 state 的值的變化會越來越小，那底下第一行代表的就是上述所提到的，state 的 value 的更新，第二行則是把當下最好的 action 存起來，因為我們的目標是找到一個最好的 policy 對吧，所以要把每個 state 最好的 action 給記錄起來。 

![](https://i.imgur.com/lzy63cy.png)
### Policy Iteration
Policy Iteration 其實和 Value Iteration 很類似，但唯一不同的地方是他除去了 max ，並且它是去給定一個 policy 然後算他的 value ，而下一次它會去算每一個 state 的最佳 action 然後放入下次 policy 當中，這樣一值重複直到當前的 policy 和上次 policy 相同時，就結束，這個方法看似跟 value iteration 很像，但其實它可以比 value iteration 更快收斂。

![](https://i.imgur.com/RAQ40qg.png)
![](https://i.imgur.com/HnQ6lMm.png)

## Conclusion
希望各位看得懂上面 MDP 的整個流程，從一開始建 Model 到解 MDP ，其實也是可以用 Linear Programming 的方式去解 MDP ，但我這裡主要講解如何使用 Dynamic Programming 去解 MDP，這樣會比較好理解跟直觀。 

















